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

from cai import Client
from cai.contrib.login_resolver import LoginResolver
from cai.settings.protocol import Protocols


async def listener(ci, ev):
    print(ev)  # print all event


async def main():
    account = os.getenv("ACCOUNT", "")
    password = os.getenv("PASSWORD", "")
    assert password and account, ValueError("account or password not set")

    ci = Client(
        int(account),
        password,
        protocol=Protocols.Android.PHONE  # or use IPAD,ANDROID_WATCH,MACOS
    )

    await LoginResolver(ci).login()
    ci.add_event_listener(listener)
    await ci.session.wait_closed()


if __name__ == '__main__':
    logging.basicConfig(  # Optional
        level=logging.DEBUG,
        handlers=[logging.StreamHandler(sys.stdout)],
        format="%(asctime)s %(name)s[%(levelname)s]: %(message)s",
    )

    asyncio.run(main())
