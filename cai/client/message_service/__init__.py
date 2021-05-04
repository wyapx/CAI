"""MessageSvc Related SDK.

This module is used to build and handle message service related packet.

:Copyright: Copyright (C) 2021-2021  cscs181
:License: AGPL-3.0 or later. See `LICENSE`_ for detail.

.. _LICENSE:
    https://github.com/cscs181/CAI/blob/master/LICENSE
"""

from enum import IntEnum
from typing import List, Union, Optional, TYPE_CHECKING

from cai.log import logger
from cai.utils.binary import Packet
from .decoders import MESSAGE_DECODERS
from cai.client.status_service import OnlineStatus
from cai.client.packet import UniPacket, IncomingPacket
from cai.pb.msf.msg.svc import PbGetMsgReq, PbDeleteMsgReq
from .event import (
    GetMessageEvent,
    GetMessageSuccess,
    GetMessageFail,
    PushNotifyEvent,
    PushNotify,
    PushNotifyError,
    PushForceOfflineEvent,
    PushForceOffline,
    PushForceOfflineError,
)

if TYPE_CHECKING:
    from cai.client import Client


class SyncFlag(IntEnum):
    START = 0
    CONTINUE = 1
    STOP = 2


def encode_get_message(
    seq: int,
    session_id: bytes,
    uin: int,
    d2key: bytes,
    request_type: int,
    sync_flag: Union[int, SyncFlag] = SyncFlag.START,
    sync_cookie: Optional[bytes] = None,
    online_sync_flag: int = 0,
    pubaccount_cookie: Optional[bytes] = None,
    server_buf: Optional[bytes] = None,
) -> Packet:
    """Build get message packet.

    Called in ``com.tencent.mobileqq.app.MessageHandler.a``.

    command name: ``MessageSvc.PbGetMsg``

    Note:
        Source: com.tencent.mobileqq.app.MessageHandler.a

    Args:
        seq (int): Packet sequence.
        session_id (bytes): Session ID.
        uin (int): User QQ number.
        d2key (bytes): Siginfo d2 key.
        request_type (int): Request type.
        sync_flag (Union[int, SyncFlag], optional): Sync flag.
            Defaults to :obj:`SyncFlag.START`.
        sync_cookie (Optional[bytes], optional): Sync cookie. Defaults to None.
        online_sync_flag (int, optional): Online sync flag. Defaults to 0.
        pubaccount_cookie (Optional[bytes], optional): Pubaccount cookie.
            Defaults to None.
        server_buf (Optional[bytes], optional): Server buf from ``PushNotify``.
            Defaults to None.

    Returns:
        Packet: PbGetMsg packet.
    """
    COMMAND_NAME = "MessageSvc.PbGetMsg"

    payload = PbGetMsgReq(
        sync_flag=sync_flag,
        sync_cookie=sync_cookie,
        ramble_flag=0,
        latest_ramble_number=20,
        other_ramble_number=3,
        online_sync_flag=online_sync_flag,
        context_flag=1,
        req_type=request_type,
        pubaccount_cookie=pubaccount_cookie,
        server_buf=server_buf,
    ).SerializeToString()
    packet = UniPacket.build(
        uin, seq, COMMAND_NAME, session_id, 1, payload, d2key
    )
    return packet


async def handle_get_message(
    client: "Client", packet: IncomingPacket
) -> "GetMessageEvent":
    """Handle Pb Get Message response.

    Note:
        Source:

        com.tencent.imcore.message.C2CMessageProcessor.b

        com.tencent.imcore.message.C2CMessageProcessor.a

        com.tencent.imcore.message.C2CMessageProcessorCallback.a

        com.tencent.imcore.message.DecodeMsg.a
    """
    resp = GetMessageEvent.decode_response(
        packet.uin,
        packet.seq,
        packet.ret_code,
        packet.command_name,
        packet.data,
    )
    if isinstance(resp, GetMessageSuccess):
        # cache last cookie
        if resp.response.rsp_type == 0:
            client._sync_cookie = resp.response.sync_cookie
            client._pubaccount_cookie = resp.response.sync_cookie
        elif resp.response.rsp_type == 1:
            client._sync_cookie = resp.response.sync_cookie
        elif resp.response.rsp_type == 2:
            client._pubaccount_cookie = resp.response.pubaccount_cookie

        if resp.response.sync_flag < SyncFlag.STOP:
            seq = client.next_seq()
            continue_packet = encode_get_message(
                seq,
                client._session_id,
                client.uin,
                client._siginfo.d2key,
                request_type=resp.response.rsp_type,
                sync_flag=resp.response.sync_flag,
                sync_cookie=resp.response.rsp_type != 2
                and client._sync_cookie
                or None,
                pubaccount_cookie=resp.response.rsp_type == 2
                and client._pubaccount_cookie
                or None,
            )
            await client.send(seq, "MessageSvc.PbGetMsg", continue_packet)

        delete_msgs: List[PbDeleteMsgReq.MsgItem] = []
        for pair_msgs in resp.response.uin_pair_msgs:
            last_read_time = pair_msgs.last_read_time & 0xFFFFFFFF
            for message in pair_msgs.msg:
                delete_msgs.append(
                    PbDeleteMsgReq.MsgItem(
                        from_uin=message.head.from_uin,
                        to_uin=message.head.to_uin,
                        type=message.head.type,
                        seq=message.head.seq,
                        uid=message.head.uid,
                    )
                )

                if message.head.to_uin != client.uin:
                    continue
                if message.head.time < last_read_time:
                    continue

                key = (
                    f"{message.head.from_uin}"
                    f"{message.head.type}"
                    f"{message.head.time}"
                )
                if key in client._msg_cache:
                    continue
                client._msg_cache[key] = None

                msg_type = message.head.type
                Decoder = MESSAGE_DECODERS.get(msg_type, None)
                if not Decoder:
                    logger.debug(
                        "MessageSvc.PbGetMsg: "
                        f"Received unknown message type {msg_type}."
                    )
                decoded_message = Decoder(message)
                print(decoded_message)
        if delete_msgs:
            seq = client.next_seq()
            del_packet = encode_delete_message(
                seq,
                client._session_id,
                client.uin,
                client._siginfo.d2key,
                delete_msgs,
            )
            await client.send(seq, "MessageSvc.PbDeleteMsg", del_packet)
    return resp


def encode_delete_message(
    seq: int,
    session_id: bytes,
    uin: int,
    d2key: bytes,
    items: List[PbDeleteMsgReq.MsgItem],
) -> Packet:
    """Build delete message packet.

    Called in ``com.tencent.mobileqq.app.MessageHandler.a``.

    command name: ``MessageSvc.PbDeleteMsg``

    Note:
        Source: com.tencent.mobileqq.app.MessageHandler.a

    Args:
        seq (int): Packet sequence.
        session_id (bytes): Session ID.
        uin (int): User QQ number.
        d2key (bytes): Siginfo d2 key.
        items (List[PbDeleteMsgReq.MsgItem]): List of message items.

    Returns:
        Packet: PbDeleteMsg packet.
    """
    COMMAND_NAME = "MessageSvc.PbDeleteMsg"

    payload = PbDeleteMsgReq(msg_items=items).SerializeToString()
    packet = UniPacket.build(
        uin, seq, COMMAND_NAME, session_id, 1, payload, d2key
    )
    return packet


async def handle_push_notify(
    client: "Client", packet: IncomingPacket
) -> PushNotifyEvent:
    """Handle Push Notify Event.

    Note:
        Source:
        com.tencent.mobileqq.app.handler.receivesuccess.MessageSvcPushNotify.a
    """
    notify = PushNotifyEvent.decode_response(
        packet.uin,
        packet.seq,
        packet.ret_code,
        packet.command_name,
        packet.data,
    )
    if isinstance(notify, PushNotify):
        # sub account
        # if notify.notify.general_flag & 8 == 8:
        #     sub_uin = notify.notify.binded_uin

        # ping
        # if notify.notify.ping_flag == 1:
        # send OnlinePush.RespPush response
        # com.tencent.mobileqq.app.BaseMessageHandler.a

        # pb get msg
        # com.tencent.mobileqq.app.MessageHandler.a
        seq = client.next_seq()
        if client._sync_cookie:
            get_msg_packet = encode_get_message(
                seq,
                client._session_id,
                client.uin,
                client._siginfo.d2key,
                request_type=1,
                sync_flag=SyncFlag.START,
                sync_cookie=client._sync_cookie,
            )
        else:
            get_msg_packet = encode_get_message(
                seq,
                client._session_id,
                client.uin,
                client._siginfo.d2key,
                request_type=0,
                sync_flag=SyncFlag.START,
                sync_cookie=None,
                online_sync_flag=1,
                server_buf=notify.notify.server_buf,
            )
        await client.send(seq, "MessageSvc.PbGetMsg", get_msg_packet)

    return notify


# MessageSvc.PushForceOffline
async def handle_force_offline(
    client: "Client", packet: IncomingPacket
) -> PushForceOfflineEvent:
    client._status = OnlineStatus.Offline
    await client.close()
    request = PushForceOfflineEvent.decode_response(
        packet.uin,
        packet.seq,
        packet.ret_code,
        packet.command_name,
        packet.data,
    )
    logger.error(
        f"Client {client.uin} force offline: " + request.request.tips
        if isinstance(request, PushForceOffline)
        else "Unknown reason."
    )
    return request


__all__ = [
    "SyncFlag",
    "encode_get_message",
    "handle_get_message",
    "GetMessageEvent",
    "GetMessageSuccess",
    "GetMessageFail",
    "handle_push_notify",
    "PushNotifyEvent",
    "PushNotify",
    "PushNotifyError",
    "handle_force_offline",
    "PushForceOfflineEvent",
    "PushForceOffline",
    "PushForceOfflineError",
]
