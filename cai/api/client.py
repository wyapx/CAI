"""Application Session APIs.

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
from cai.client import Session
from cai.settings.device import get_device
from cai.pb.msf.msg.svc import PbSendMsgResp
from cai.client.highway import HighWaySession
from cai.settings.protocol import get_protocol, get_apk_info
from cai.client.message_service.encoders import build_msg, make_msg_pkg
from cai.client.message_service.models import (
    Element,
    ImageElement,
    VoiceElement, GroupMessage, VideoElement, PrivateMessage,
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


def _make_session(uin: int, passwd: Union[str, bytes], protocol: Optional[str] = None) -> Session:
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
    return Session(uin, passwd, device, apk_info)


class Client(_Login, _Friend, _Group, _Events):
    def __init__(
        self,
        uin: int,
        passwd: Union[str, bytes],
        protocol: Optional[str] = None,
    ):
        session = _make_session(uin, passwd, protocol=protocol)
        self.session = session
        self._highway_session = HighWaySession(session, logger=log.highway)
        self._msg_fut: Dict[int, asyncio.Future] = {}  # rand: seq
        self.add_event_listener(self._internal_handler)

    async def _internal_handler(self, _, ev):
        if isinstance(ev, GroupMessage):
            if ev.rand in self._msg_fut:
                self._msg_fut[ev.rand].set_result(ev.seq)

    @property
    def connected(self) -> bool:
        return self.session.connected

    @property
    def status(self) -> Optional[OnlineStatus]:
        return self.session.status

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
        seq, rand, fut = self.session.next_seq(), random.randint(1000, 1000000), asyncio.Future()
        self._msg_fut[rand] = fut
        try:
            resp: PbSendMsgResp = PbSendMsgResp.FromString(
                (
                    await self.session.send_unipkg_and_wait(
                        "MessageSvc.PbSendMsg",
                        make_msg_pkg(
                            seq,
                            rand,
                            build_msg(msg),
                            group_id=gid
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

    async def send_friend_msg(self, uin: int, msg: Sequence[Element]) -> Tuple[int, int, int]:
        # todo: split long msg
        seq, rand = (
            self.session.next_friend_seq(),
            random.randint(1000, 1000000)
        )
        resp: PbSendMsgResp = PbSendMsgResp.FromString(
            (
                await self.session.send_unipkg_and_wait(
                    "MessageSvc.PbSendMsg",
                    make_msg_pkg(
                        seq,
                        rand,
                        build_msg(msg),
                        uin=uin
                    ).SerializeToString(),
                    seq=seq
                )
            ).data
        )
        if resp.result == 0:
            return (
                seq,
                rand,
                resp.send_time
            )
        else:
            raise BotException(resp.result, resp.errmsg)

    async def upload_image(self, group_id: int, file: BinaryIO, as_emoji=False) -> ImageElement:
        image = await self._highway_session.upload_image(file, group_id)
        image.is_emoji = as_emoji
        return image

    async def upload_voice(self, group_id: int, file: BinaryIO) -> VoiceElement:
        return await self._highway_session.upload_voice(file, group_id)

    async def upload_video(self, group_id: int, file: BinaryIO, thumb: BinaryIO) -> VideoElement:
        return await self._highway_session.upload_video(file, thumb, group_id)

    async def close(self) -> NoReturn:
        """Stop Session"""
        await self.session.close()

    async def set_status(
        self,
        status: Union[int, OnlineStatus],
        battery_status: Optional[int] = None,
        is_power_connected: bool = False,
    ) -> NoReturn:
        """Change session status.

        This function wraps the :meth:`~cai.session.session.Session.register`
        method of the session.

        Args:
            status (OnlineStatus): Status want to change.
            battery_status (Optional[int], optional): Battery capacity.
                Defaults to None.
            is_power_connected (bool, optional): Is power connected to phone.
                Defaults to False.

        Raises:
            RuntimeError: Session already exists and is running.
            RuntimeError: Password not provided when login a new account.
            ApiResponseError: Invalid API request.
            RegisterException: Register Failed.
        """
        await self.session.set_status(
            status,
            battery_status,
            is_power_connected,
        )


__all__ = ["Client"]
