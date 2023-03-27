"""Application Login APIs.

:Copyright: Copyright (C) 2021-2021  cscs181
:License: AGPL-3.0 or later. See `LICENSE`_ for detail.

.. _LICENSE:
    https://github.com/cscs181/CAI/blob/master/LICENSE
"""
import pickle
import time

from cai.exceptions import LoginException

from .base import BaseAPI


class Login(BaseAPI):
    async def login(self):
        """Create a new session (or use an existing one) and login.

        This function wraps the :meth:`~cai.session.session.Session.login` method of the session.

        Raises:
            LoginSliderException: Need slider ticket.
            LoginCaptchaException: Need captcha image.
        """
        await self.session.connect()
        try:
            await self._executor("login")
        except LoginException:
            raise  # user handle required
        except Exception:
            await self.session.close()
            raise

    async def token_login(self, token: dict):
        await self.session.connect()
        try:
            await self._executor("token_login", token)
        except LoginException:
            raise  # user handle required
        except Exception:
            await self.session.close()
            raise

    def dump_token(self) -> bytes:
        siginfo = self.session._siginfo.to_dict()
        siginfo["ExpireTime"] = int(time.time() + (86400 * 5))  # 5d
        siginfo["DeviceType"] = self.session.apk_info.device_type
        return pickle.dumps(siginfo)

    async def submit_captcha(self, captcha: str, captcha_sign: bytes) -> bool:
        """Submit captcha data to login.

        This function wraps the :meth:`~cai.session.session.Session.submit_captcha`
        method of the session.

        Args:
            captcha (str): Captcha data to submit.
            captcha_sign (bytes): Captcha sign received when login.

        Raises:
            LoginSliderException: Need slider ticket.
            LoginCaptchaException: Need captcha image.
        """
        try:
            await self._executor("submit_captcha", captcha, captcha_sign)
        except LoginException:
            await self.session.close()
            raise
        return True

    async def submit_slider_ticket(self, ticket: str) -> bool:
        """Submit slider ticket to login.

        This function wraps the :meth:`~cai.session.session.Session.submit_slider_ticket`
        method of the session.

        Args:
            ticket (str): Slider ticket to submit.

        Raises:
            LoginSliderException: Need slider ticket.
            LoginCaptchaException: Need captcha image.
        """
        await self._executor("submit_slider_ticket", ticket)
        return True

    async def request_sms(self) -> bool:
        """Request sms code message to login.

        This function wraps the :meth:`~cai.session.session.Session.request_sms`
        method of the session.

        Args:
            uin (Optional[int], optional): Account of the session want to login.
                Defaults to None.

        Raises:
            LoginSMSRequestError: Too many SMS messages were sent.
        """
        try:
            return await self.session.request_sms()
        except LoginException:
            await self.session.close()
            raise

    async def submit_sms(self, sms_code: str) -> bool:
        """Submit sms code to login.

        This function wraps the :meth:`~cai.session.session.Session.submit_sms`
        method of the session.

        Args:
            sms_code (str): SMS code to submit.

        Raises:
            LoginSliderException: Need slider ticket.
            LoginCaptchaException: Need captcha image.
        """
        try:
            await self._executor("submit_sms", sms_code)
        except LoginException:
            await self.session.close()
            raise
        return True


__all__ = ["Login"]
