import asyncio
import functools
import pickle
import sys
import time

from typing import Callable, Any, Coroutine, Sequence, AnyStr

from cai.log import logger
from cai.storage import Storage
from cai.api.client import Client
from cai.utils.httpcat import HttpCat
from cai.settings.device import (
    get_device,
    save_device,
    new_device,
    new_imei,
    new_android_id,
    new_mac_address
)
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
        print(prompt, end="")
        return await reader.readline()

    if sys.platform == "win32":
        return _win32
    else:
        return _asyncio


async def chooser(description: str, options: Sequence[AnyStr], default: int = None) -> int:
    async_stdin = await _connect_async_stdin()
    while True:
        print(description)
        for k, v in enumerate(options):
            print(f"  {k+1}:{v}")

        i = await async_stdin(
            ">>" if default is None else
            f"[{default}]>>"
        )
        if not i and default is not None:
            return default
        elif not i:
            print(f"输入有误，请重新选择")
            continue

        try:
            i = int(i)
        except ValueError:
            print(f"输入有误，请重新选择")
            continue

        if 0 < i <= len(options):
            return i
        else:
            print(f"输入有误，请重新选择")


class LoginResolver:
    def __init__(self, client: Client, use_cache=True):
        self._client = client
        self._logger = logger.getChild("login_resolver")
        self.use_cache = use_cache
        self.login_cache_file = Storage.cache_dir / f"{client.uin}_token.session"

    async def _login(self, *, exc=None) -> bool:
        client = self._client
        try:
            if exc:
                if isinstance(exc, LoginSliderNeeded):
                    await self.on_login_slider_needed(client, exc)
                elif isinstance(exc, LoginCaptchaNeeded):
                    await self.on_login_captcha_needed(client, exc)
                elif isinstance(exc, LoginDeviceLocked):
                    await self.on_login_device_locked(client, exc)
                else:
                    raise
            await client.login()
        except (
            LoginDeviceLocked,
            LoginSliderNeeded,
            LoginCaptchaNeeded
        ) as e:  # recoverable
            return await self._login(exc=e)

        except (LoginException, ApiResponseError) as e:  # unrecoverable
            await self.unrecoverable_login_exception(e, client)
            return False

        return True

    @functools.singledispatchmethod
    async def unrecoverable_login_exception(self, exc: LoginException, client: Client):
        if exc.status == 1:  # wrong password
            self._logger.critical(exc.message)
        elif exc.status == 235:  # outdated client
            r = await chooser(
                "账号被风控（过期的客户端）\n"
                "可能需要调整设备信息：",
                (
                    "重新生成device.json（会清除所有信息）",
                    "只对部分信息进行重新生成（实验性功能）"
                )
            )
            if r == 1:
                save_device(
                    client.uin,
                    new_device(),
                    backup=True
                )
            elif r == 2:
                device = get_device(client.uin)
                device.imei = new_imei()
                device.android_id = new_android_id()
                device.mac_address = new_mac_address()
                save_device(client.uin, device, backup=True)
            print("已重新生成，将在下次启动生效")
        else:
            raise

    @unrecoverable_login_exception.register
    async def _login_sms_request_error(self, _exc: LoginSMSRequestError, _client: Client):
        self._logger.critical(f"验证短信发送间隔过短，请稍候再试")

    @unrecoverable_login_exception.register
    async def _login_account_frozen_error(self, exc: LoginAccountFrozen, _client: Client):
        self._logger.critical(f"账号 {exc.uin} 已被冻结，请使用QQ客户端查看详情")

    @unrecoverable_login_exception.register
    async def _api_response_error(self, exc: ApiResponseError, client: Client):
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
        print("发现设备锁")
        if exc.sms_phone or exc.verify_url:
            r = await chooser(
                "需要使用以下方法进行设备锁验证：",
                [
                    i
                    for i in (
                        "进入QQ官方网站进行验证" if exc.verify_url else None,
                        f"发送验证码到{exc.sms_phone}上" if exc.sms_phone else None
                    ) if i
                ]
            )
            if r == 1 and exc.verify_url:
                way = "url"
            elif r == 2 and exc.sms_phone:
                way = "sms"
            else:
                raise ValueError(f"choice {r} is not support yet")
        else:
            raise AssertionError("没有可用的验证方式")

        if way == "sms":
            await client.request_sms()
            print(f"验证码已经发送到{exc.sms_phone}!")
            sms_code = (await async_read("输入你获取到的验证码: ")).strip().decode()
            await client.submit_sms(sms_code)
        elif way == "url":
            await client.close()
            print(f"请到 {exc.verify_url} 完成验证")
            print()
            await async_read("完成验证后，按下回车键以继续")

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
            self._logger.exception("fast-login failed")
            if self._client.connected:
                await self._client.close()
                await asyncio.sleep(1)

            self.login_cache_file.unlink(missing_ok=True)
            self.use_cache = False

        if not self.use_cache or not self._client.connected:
            if not await self._login():
                await self._client.close()
                return

        await self.after_login()

    async def before_login(self):
        pass

    async def after_login(self):
        self._logger.info("登录成功!")

        with open(self.login_cache_file, "wb") as f:
            f.write(self._client.dump_token())
        self._logger.info("fast-login token saved")
