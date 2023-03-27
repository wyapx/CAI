import asyncio
import pickle
import sys
import time

from typing import Callable, Any, Coroutine

from cai.log import logger
from cai.storage import Storage
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


async def _connect_async_stdin() -> Callable[[str], Coroutine[Any, Any, bytes]]:
    loop = asyncio.get_running_loop()

    async def _win32(prompt: str = "") -> bytes:
        return (await asyncio.to_thread(input, prompt)).encode()

    async def _asyncio(prompt: str = "") -> bytes:
        reader = asyncio.StreamReader()
        protocol = asyncio.StreamReaderProtocol(reader)
        await loop.connect_read_pipe(lambda: protocol, sys.stdin)
        sys.stdout.write(prompt)
        return await reader.readline()

    if sys.platform == "win32":
        return _win32
    else:
        return _asyncio


class LoginResolver:
    def __init__(self, client: Client, use_cache=True):
        self._client = client
        self._logger = logger.getChild("login_resolver")
        self.use_cache = use_cache
        self.login_cache_file = Storage.cache_dir / f"{client.uin}_token.session"

    async def _login(self, *, exc=None):
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
            return await self._login(exc=e)

    async def on_api_response_err(self, client: Client, exc: ApiResponseError):
        raise

    async def on_login_slider_needed(self, client: Client, exc: LoginSliderNeeded):
        url = exc.verify_url.replace("ssl.captcha.qq.com", "txhelper.glitch.me")
        print("本次操作需要进行滑块验证(留空可使用TxCaptchaHelper)")
        print("验证地址:", url)
        async_input = await _connect_async_stdin()
        ticket = (await async_input("输入获取到的验证码 -> ")).strip()
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
                choice = (await async_read("Choose: ")).strip().decode()
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
            sms_code = (await async_read("Please enter the sms_code: ")).strip().decode()
            await client.submit_sms(sms_code)
        elif way == "url":
            await client.close()
            print(f"Go to {exc.verify_url} to verify device!")
            print()
            await async_read("Press ENTER after verification to continue login...")

    async def on_login_sms_request_error(self, client: Client, exc: LoginSMSRequestError):
        raise

    async def on_login_account_frozen_error(self, client: Client, exc: LoginAccountFrozen):
        raise

    async def login(self):
        await self.before_login()

        try:
            if self.login_cache_file.is_file() and self.use_cache:
                self._logger.info("Cache found, trying to fast-login")
                with open(self.login_cache_file, "rb") as f:
                    token: dict = pickle.load(f)

                if all((
                    self._client.device_type == token.pop("DeviceType"),
                    time.time() < token.pop("ExpireTime")
                )):
                    await self._client.token_login(token)
                else:
                    self._logger.warning("Cache is expired or device_type changed, ignore")
                    self.use_cache = False
        except:
            if self._client.connected:
                await self._client.close()
                await asyncio.sleep(1)
            self._logger.exception("fast-login failed")
            self.login_cache_file.unlink(missing_ok=True)
            self.use_cache = False

        if not self._client.connected:
            await self._login()

        self._logger.info("登录成功!")
        await self.after_login()

    async def before_login(self):
        pass

    async def after_login(self):
        with open(self.login_cache_file, "wb") as f:
            f.write(self._client.dump_token())
        self._logger.info("fast-login token saved")
