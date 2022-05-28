"""Example Code for Friend/Group.

:Copyright: Copyright (C) 2021-2021  cscs181
:License: AGPL-3.0 or later. See `LICENSE`_ for detail.

.. _LICENSE:
    https://github.com/cscs181/CAI/blob/master/LICENSE
"""
import logging
import os
import asyncio
import sys

from cai.api.client import Client


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
    await asyncio.sleep(2)  # wait for a moment
    try:
        await run(ci)
    finally:
        await ci.close()


async def run(ci: Client):
    # friend
    friend_list = await ci.get_friend_list()
    friend_group_list = await ci.get_friend_group_list()
    print("========== friends ==========", *friend_list, sep="\n")
    print("========== friend groups ==========", *friend_group_list, sep="\n")
    example_friend = friend_list[0]
    # friend = await cai.get_friend(friend_uin)
    print("========== example friend ==========")
    print("uin: ", example_friend.uin)
    print("nick: ", example_friend.nick)
    print("remark: ", example_friend.remark)
    print("group: ", await example_friend.get_group())

    group_list = await ci.get_group_list()
    print("\n========== group list ==========", *group_list, sep="\n")
    example_group = group_list[0]
    # group = await cai.get_group(group_id)
    print("========== example group ==========")
    print("group id: ", example_group.group_id)
    print("group name: ", example_group.group_name)
    print("group owner: ", example_group.group_owner_uin)
    example_group_member_list = await example_group.get_members()
    print(
        "========== example group members ==========",
        *example_group_member_list,
        sep="\n",
    )


if __name__ == '__main__':
    logging.basicConfig(  # Optional
        level=logging.DEBUG,
        handlers=[logging.StreamHandler(sys.stdout)],
        format="%(asctime)s %(name)s[%(levelname)s]: %(message)s",
    )

    asyncio.run(main())
