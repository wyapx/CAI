"""Example Code for Login.

:Copyright: Copyright (C) 2021-2021  cscs181
:License: AGPL-3.0 or later. See `LICENSE`_ for detail.

.. _LICENSE:
    https://github.com/cscs181/CAI/blob/master/LICENSE
"""
import os
import sys
import asyncio
import logging
from io import BytesIO

from PIL import Image
from cai import Client, LoginSliderNeeded, LoginCaptchaNeeded, LoginDeviceLocked


async def login_resolver(client: Client, exception: Exception):
    if isinstance(exception, LoginSliderNeeded):
        print("Verify url:", exception.verify_url.replace("ssl.captcha.qq.com", "txhelper.glitch.me"))
        ticket = input("Please enter the ticket: ").strip()
        try:
            await client.submit_slider_ticket(ticket)
            print("Login Success!")
            await asyncio.sleep(3)
        except Exception as e:
            await login_resolver(client, e)
    elif isinstance(exception, LoginCaptchaNeeded):
        print("Captcha:")
        image = Image.open(BytesIO(exception.captcha_image))
        image.show()
        captcha = input("Please enter the captcha: ").strip()
        try:
            await client.submit_captcha(captcha, exception.captcha_sign)
            print("Login Success!")
            await asyncio.sleep(3)
        except Exception as e:
            await login_resolver(client, e)
    elif isinstance(exception, LoginDeviceLocked):
        print("Device lock detected!")
        if exception.sms_phone or exception.verify_url:
            while True:
                print(
                    "Choose a method to verity: \n",
                    " ".join([
                        f"1. Send sms message to {exception.sms_phone}.\n" if exception.sms_phone else "",
                        f"2. Verify device by url.\n" if exception.verify_url else ""
                    ])
                )
                choice = input(
                    f"Choose: "
                )
                if "1" in choice and exception.sms_phone:
                    way = "sms"
                    break
                elif "2" in choice and exception.verify_url:
                    way = "url"
                    break
                print(f"'{choice}' is invalid!")
        else:
            raise AssertionError("No way to verify device...")

        if way == "sms":
            await client.request_sms()
            print(f"SMS was sent to {exception.sms_phone}!")
            sms_code = input("Please enter the sms_code: ").strip()
            try:
                await client.submit_sms(sms_code)
            except Exception as e:
                await login_resolver(client, e)
        elif way == "url":
            print(f"Go to {exception.verify_url} to verify device!")
            input("Press ENTER after verification to continue login...")
            try:
                await client.login()
            except Exception as e:
                await login_resolver(client, e)
    else:
        # LoginAccountFrozen, LoginException, ApiResponseError, etc...
        raise


async def listener(ci, ev):
    print(ev)  # print all event


async def main():
    account = os.getenv("ACCOUNT", "")
    password = os.getenv("PASSWORD", "")
    assert password and account, ValueError("account or password not set")

    ci = Client(
        int(account),
        password,
        protocol="ANDROID_PHONE"  # or use IPAD,ANDROID_WATCH,MACOS
    )

    try:
        await ci.login()
    except Exception as e:
        await login_resolver(ci, e)
    ci.add_event_listener(listener)
    await ci.session.wait_closed()


if __name__ == '__main__':
    logging.basicConfig(  # Optional
        level=logging.DEBUG,
        handlers=[logging.StreamHandler(sys.stdout)],
        format="%(asctime)s %(name)s[%(levelname)s]: %(message)s",
    )

    asyncio.run(main())
