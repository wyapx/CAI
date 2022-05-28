"""Example Code for Message.

:Copyright: Copyright (C) 2021-2021  cscs181
:License: AGPL-3.0 or later. See `LICENSE`_ for detail.

.. _LICENSE:
    https://github.com/cscs181/CAI/blob/master/LICENSE
"""
import logging
import os
import asyncio
import sys

from cai import Client
from cai.client import Event
from cai.client.events.common import PrivateMessage, GroupMessage


async def main():
    account = os.getenv("ACCOUNT", "")
    password = os.getenv("PASSWORD", "")
    assert password and account, ValueError("account or password not set")

    ci = Client(
        int(account),
        password,
        protocol="ANDROID_PHONE"  # or use IPAD,ANDROID_WATCH,MACOS
    )

    await ci.login()

    ci.add_event_listener(listen_message)
    await ci.session.wait_closed()


async def listen_message(client: Client, event: Event):
    if isinstance(event, PrivateMessage):
        print("Private Message received from", event.from_uin)
        print("Private Message elements:", event.message)
    elif isinstance(event, GroupMessage):
        print(
            f"Group Message received from {event.group_name}({event.group_id})"
        )
        print("Group Message elements:", event.message)


if __name__ == '__main__':
    logging.basicConfig(  # Optional
        level=logging.DEBUG,
        handlers=[logging.StreamHandler(sys.stdout)],
        format="%(asctime)s %(name)s[%(levelname)s]: %(message)s",
    )

    asyncio.run(main())
