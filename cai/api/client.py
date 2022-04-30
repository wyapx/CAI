"""Application Client APIs.

:Copyright: Copyright (C) 2021-2021  cscs181
:License: AGPL-3.0 or later. See `LICENSE`_ for detail.

.. _LICENSE:
    https://github.com/cscs181/CAI/blob/master/LICENSE
"""
import asyncio
import hashlib
import random
from typing import Union, BinaryIO, Optional, Sequence, Tuple, Dict, NoReturn

from cai import log
from cai.client import OnlineStatus
from cai.client import Client as client_t
from cai.settings.device import get_device
from cai.pb.msf.msg.svc import PbSendMsgResp
from cai.client.highway import HighWaySession
from cai.settings.protocol import get_protocol, get_apk_info
from cai.client.message_service.encoders import build_msg, make_group_msg_pkg
from cai.client.message_service.models import (
    Element,
    ImageElement,
    VoiceElement, GroupMessage,
)

from .group import Group as _Group
from .login import Login as _Login
from .flow import Events as _Events
from .friend import Friend as _Friend
from .error import (
    BotMutedException,
    AtAllLimitException,
    GroupMsgLimitException,
    BotException,
)


def _make_client(uin: int, passwd: Union[str, bytes], protocol: Optional[str] = None) -> client_t:
    if not (isinstance(passwd, bytes) and len(passwd) == 16):
        # not a valid md5 passwd
        if isinstance(passwd, bytes):
            passwd = hashlib.md5(passwd).digest()
        else:
            passwd = hashlib.md5(passwd.encode()).digest()
    device = get_device(uin)
    if not protocol:
        apk_info = get_protocol(uin)
    else:
        apk_info = get_apk_info(protocol)
    return client_t(uin, passwd, device, apk_info)


class Client(_Login, _Friend, _Group, _Events):
    def __init__(
        self,
        uin: int,
        passwd: Union[str, bytes],
        protocol: Optional[str] = None,
        *, max_reconnections=5
    ):
        client = _make_client(uin, passwd, protocol)
        client._max_reconnections = max(max_reconnections, 0)

        self.client = client
        self._highway_session = HighWaySession(client, logger=log.highway)
        self._msg_fut: Dict[int, asyncio.Future] = {}  # rand: seq
        self.add_event_listener(self._internal_handler)

    async def _internal_handler(self, _, ev):
        if isinstance(ev, GroupMessage):
            if ev.rand in self._msg_fut:
                self._msg_fut[ev.rand].set_result(ev.seq)

    @property
    def connected(self) -> bool:
        return self.client.connected

    @property
    def status(self) -> Optional[OnlineStatus]:
        return self.client.status

    async def send_group_msg(self, gid: int, msg: Sequence[Element]) -> Tuple[int, int, int]:
        """
        Return:
            Tuple [
                sequence(int),
                random(int),
                send_time(int)
            ]
        """
        # todo: split long msg
        seq, rand, fut = self.client.next_seq(), random.randint(1000, 1000000), asyncio.Future()
        self._msg_fut[rand] = fut
        try:
            resp: PbSendMsgResp = PbSendMsgResp.FromString(
                (
                    await self.client.send_unipkg_and_wait(
                        "MessageSvc.PbSendMsg",
                        make_group_msg_pkg(
                            seq, gid, rand, build_msg(msg)
                        ).SerializeToString(),
                        seq=seq
                    )
                ).data
            )

            if resp.result == 0:
                return (
                    await asyncio.wait_for(fut, 5),
                    rand,
                    resp.send_time
                )
            elif resp.result == 120:
                raise BotMutedException
            elif resp.result == 121:
                raise AtAllLimitException
            elif resp.result == 299:
                raise GroupMsgLimitException
            else:
                raise BotException(resp.result, resp.errmsg)
        finally:
            del self._msg_fut[rand]

    async def upload_image(self, group_id: int, file: BinaryIO) -> ImageElement:
        return await self._highway_session.upload_image(file, group_id)

    async def upload_voice(self, group_id: int, file: BinaryIO) -> VoiceElement:
        return await self._highway_session.upload_voice(file, group_id)

    async def close(self) -> NoReturn:
        """Stop Client"""
        await self.client.close()

    async def set_status(
        self,
        status: Union[int, OnlineStatus],
        battery_status: Optional[int] = None,
        is_power_connected: bool = False,
    ) -> NoReturn:
        """Change client status.

        This function wraps the :meth:`~cai.client.client.Client.register`
        method of the client.

        Args:
            status (OnlineStatus): Status want to change.
            battery_status (Optional[int], optional): Battery capacity.
                Defaults to None.
            is_power_connected (bool, optional): Is power connected to phone.
                Defaults to False.

        Raises:
            RuntimeError: Client already exists and is running.
            RuntimeError: Password not provided when login a new account.
            ApiResponseError: Invalid API request.
            RegisterException: Register Failed.
        """
        await self.client.set_status(
            status,
            battery_status,
            is_power_connected,
        )


__all__ = ["Client"]
