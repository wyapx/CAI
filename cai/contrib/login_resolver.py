import asyncio
import sys

from cai.api.client import Client
from cai.utils.httpcat import HttpCat
from cai.exceptions import (
    LoginException,
    LoginDeviceLocked,
    LoginSliderNeeded,
    LoginCaptchaNeeded,
    LoginAccountFrozen,
    LoginSMSRequestError,
    ApiResponseError
)


async def _connect_async_stdin() -> asyncio.StreamReader:
    loop = asyncio.get_running_loop()
    reader = asyncio.StreamReader()
    protocol = asyncio.StreamReaderProtocol(reader)
    await loop.connect_read_pipe(lambda: protocol, sys.stdin)
    return reader


class LoginResolver:
    def __init__(self, client: Client):
        self._client = client

    async def login(self, *, exc=None):
        client = self._client
        try:
            if exc:
                if isinstance(exc, ApiResponseError):
                    await self.on_api_response_err(client, exc)
                elif isinstance(exc, LoginSliderNeeded):
                    await self.on_login_slider_needed(client, exc)
                elif isinstance(exc, LoginCaptchaNeeded):
                    await self.on_login_captcha_needed(client, exc)
                elif isinstance(exc, LoginDeviceLocked):
                    await self.on_login_device_locked(client, exc)
                elif isinstance(exc, LoginSMSRequestError):
                    await self.on_login_sms_request_error(client, exc)
                elif isinstance(exc, LoginAccountFrozen):
                    await self.on_login_account_frozen_error(client, exc)
                else:
                    raise
            await client.login()
        except (LoginException, ApiResponseError) as e:
            return await self.login(exc=e)
        print("登录成功")

    async def on_api_response_err(self, client: Client, exc: ApiResponseError):
        raise

    async def on_login_slider_needed(self, client: Client, exc: LoginSliderNeeded):
        url = exc.verify_url.replace("ssl.captcha.qq.com", "txhelper.glitch.me")
        print("本次操作需要进行滑块验证(留空可使用TxCaptchaHelper)")
        print("验证地址:", url)
        print("输入获取到的验证码 -> ", end="")
        async_input = await _connect_async_stdin()
        ticket = (await async_input.readline()).strip()
        if not ticket:
            print("将使用TxCaptchaHelper，请等待")
            resp = await HttpCat.request("GET", url)
            print(resp.text())
            for _ in range(100):
                resp = (await HttpCat.request("GET", url)).text()
                if resp.startswith("t"):
                    ticket = resp
                    break
                else:
                    print(".", end="")
                    await asyncio.sleep(5)
            else:
                raise TimeoutError

        await client.submit_slider_ticket(ticket)

    async def on_login_captcha_needed(self, client: Client, exc: LoginCaptchaNeeded):
        raise

    async def on_login_device_locked(self, client: Client, exc: LoginDeviceLocked):
        async_read = await _connect_async_stdin()
        print("Device lock detected!")
        if exc.sms_phone or exc.verify_url:
            while True:
                print(
                    "Choose a method to verity: \n",
                    " ".join([
                        f"1. Send sms message to {exc.sms_phone}.\n" if exc.sms_phone else "",
                        f"2. Verify device by url.\n" if exc.verify_url else ""
                    ])
                )
                print("Choose: ", end="")
                choice = (await async_read.readline()).strip().decode()
                if "1" in choice and exc.sms_phone:
                    way = "sms"
                    break
                elif "2" in choice and exc.verify_url:
                    way = "url"
                    break
                print(f"'{choice}' is invalid!")
        else:
            raise AssertionError("No way to verify device...")

        if way == "sms":
            await client.request_sms()
            print(f"SMS was sent to {exc.sms_phone}!")
            print("Please enter the sms_code: ", end="")
            sms_code = (await async_read.readline()).strip().decode()
            await client.submit_sms(sms_code)
        elif way == "url":
            await client.close()
            print(f"Go to {exc.verify_url} to verify device!")
            print("Press ENTER after verification to continue login...")
            await async_read.readline()

    async def on_login_sms_request_error(self, client: Client, exc: LoginSMSRequestError):
        raise

    async def on_login_account_frozen_error(self, client: Client, exc: LoginAccountFrozen):
        raise

