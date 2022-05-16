"""OnlinePush Related SDK.

This module is used to build and handle online push related packet.

:Copyright: Copyright (C) 2021-2021  cscs181
:License: AGPL-3.0 or later. See `LICENSE`_ for detail.

.. _LICENSE:
    https://github.com/cscs181/CAI/blob/master/LICENSE
"""
import struct
from typing import TYPE_CHECKING, List, Optional

from jce import types

from cai.log import logger
from cai.utils.binary import Packet
from cai.utils.jce import RequestPacketVersion3
from cai.client.message_service import MESSAGE_DECODERS
from cai.client.packet import UniPacket, IncomingPacket
from cai.client.events.group import (
    GroupMemberLeaveEvent,
    TransferGroupEvent,
    GroupMemberPermissionChangeEvent
)


from .decoders import ONLINEPUSH_DECODERS, decode_trans_msg
from .jce import DelMsgInfo, DeviceInfo, SvcRespPushMsg
from .command import (
    PushMsg,
    SvcReqPush,
    PushMsgError,
    PushMsgCommand,
    SvcReqPushCommand,
)

if TYPE_CHECKING:
    from cai.client import Session


# OnlinePush.RespPush
def encode_push_response(
    session: "Session",
    seq: int,
    svrip: int,
    delete_messages: List[DelMsgInfo] = None,
    push_token: Optional[bytes] = None,
    service_type: int = 0,
    device_info: Optional[DeviceInfo] = None,
) -> Packet:
    """Build online push response packet.

    Called in ``com.tencent.mobileqq.app.BaseMessageHandler.a``.

    command name: ``OnlinePush.RespPush``

    Note:
        Source: com.tencent.mobileqq.service.message.MessageFactorySender.b

    Args:
        session (Session): Session instance.
        seq (int): Packet sequence.
        svrip (int): Svrip from push packet.
        delete_messages (List[DelMsgInfo]): List of delete messages.
        push_token (Optional[bytes]): Push token from push packet.
        service_type (int): Service type.
        device_info (Optional[DeviceInfo]): Device info.

    Returns:
        Packet: PbDeleteMsg packet.
    """
    COMMAND_NAME = "OnlinePush.RespPush"

    resp = SvcRespPushMsg(
        uin=session.uin,
        del_infos=delete_messages if delete_messages else [],
        svrip=svrip,
        push_token=push_token,
        service_type=service_type,
        device_info=device_info,
    )
    payload = SvcRespPushMsg.to_bytes(0, resp)
    req_packet = RequestPacketVersion3(
        servant_name="OnlinePush",
        func_name="SvcRespPushMsg",
        data=types.MAP({types.STRING("resp"): types.BYTES(payload)}),
    ).encode()
    packet = UniPacket.build(
        session.uin, seq, COMMAND_NAME, session._session_id, 1, req_packet, session._siginfo.d2key
    )
    return packet


async def handle_c2c_sync(
    client: "Session", packet: IncomingPacket
) -> PushMsgCommand:
    """Handle C2C Message Sync.

    Note:
        Source: c2c 2003

        com.tencent.imcore.message.C2CMessageProcessor.b (handleMsgPush_PB_SlaveMaster)

        com.tencent.mobileqq.app.MessageHandler.b
    """
    push = PushMsgCommand.decode_response(
        packet.uin,
        packet.seq,
        packet.ret_code,
        packet.command_name,
        packet.data,
    )
    if isinstance(push, PushMsg) and push.push.HasField("msg"):
        # c2c 2003
        message = push.push.msg
        msg_type = message.head.type

        resp_packet = encode_push_response(
            client,
            push.seq,
            push.push.svrip,
            push_token=push.push.push_token or None,
        )
        await client.send(push.seq, "OnlinePush.RespPush", resp_packet)

        Decoder = MESSAGE_DECODERS.get(msg_type, None)
        if not Decoder:
            logger.debug(
                f"{push.command_name}: "
                f"Received unknown message type {msg_type}."
            )
            return push
        decoded_message = Decoder(message)
        if decoded_message:
            client.dispatch_event(decoded_message)

    return push


async def handle_push_msg(
    client: "Session",
    packet: IncomingPacket,
) -> PushMsgCommand:
    """Handle Push Message Command.

    Note:
        Source: troop 1001, c2c 1001, discussion 1001

        com.tencent.mobileqq.app.MessageHandler.b
    """

    push = PushMsgCommand.decode_response(
        packet.uin,
        packet.seq,
        packet.ret_code,
        packet.command_name,
        packet.data,
    )
    if isinstance(push, PushMsg) and push.push.HasField("msg"):
        message = push.push.msg
        msg_type = message.head.type

        if msg_type == 43 or msg_type == 82:
            # troop 1001
            # ping
            if push.push.ping_flag == 1:
                resp_packet = encode_push_response(
                    client,
                    push.seq,
                    push.push.svrip,
                    push_token=push.push.push_token or None,
                    service_type=1,
                    device_info=DeviceInfo(
                        net_type=1,
                        dev_type=client.device.model,
                        os_ver=client.device.version.release,
                        vendor_name=client.device.vendor_name,
                        vendor_os_name=client.device.vendor_os_name,
                    ),
                )
                await client.send(push.seq, "OnlinePush.RespPush", resp_packet)
        elif msg_type == 141:
            # c2c 1001
            delete_info = DelMsgInfo(
                from_uin=message.head.from_uin,
                msg_seq=message.head.seq,
                msg_time=message.head.time,
            )
            resp_packet = encode_push_response(
                client,
                push.seq,
                push.push.svrip,
                [delete_info],
                push_token=push.push.push_token or None,
            )
            await client.send(push.seq, "OnlinePush.RespPush", resp_packet)
        elif msg_type != 42:
            # discussion 1001
            pass

        Decoder = MESSAGE_DECODERS.get(msg_type, None)
        if not Decoder:
            logger.debug(
                f"{push.command_name}: "
                f"Received unknown message type {msg_type}."
            )
            return push
        decoded_message = Decoder(message)
        if decoded_message:
            client.dispatch_event(decoded_message)

    return push


# OnlinePush.ReqPush
async def handle_req_push(
    client: "Session", packet: IncomingPacket
) -> SvcReqPushCommand:
    """Handle Request Push Command.

    Note:
        Source: com.tencent.imcore.message.OnLinePushMessageProcessor.ProcessOneMsg.a
    """
    push = SvcReqPushCommand.decode_response(
        packet.uin,
        packet.seq,
        packet.ret_code,
        packet.command_name,
        packet.data,
    )

    if isinstance(push, SvcReqPush):
        pkg = encode_push_response(
            client,
            push.seq,
            push.message.svrip,
            [
                DelMsgInfo(
                    from_uin=info.from_uin,
                    msg_seq=info.msg_seq,
                    msg_time=info.msg_time,
                    msg_cookies=info.msg_cookies,
                )
                for info in push.message.msg_info
            ],
        )
        await client.send(push.seq, "OnlinePush.RespPush", pkg)

        for info in push.message.msg_info:
            key = f"{info.msg_seq}{info.msg_time}{info.msg_uid}"
            should_skip = key in client._online_push_cache
            client._online_push_cache[key] = None
            if should_skip:
                continue

            Decoder = ONLINEPUSH_DECODERS.get(info.msg_type, None)
            if not Decoder:
                logger.debug(
                    f"{push.command_name}: "
                    f"Received unknown onlinepush type {info.msg_type}."
                )
                continue
            for event in Decoder(info):
                client.dispatch_event(event)
    return push


# OnlinePush.PbPushTransMsg
async def handle_push_trans_msg(
    client: "Session", packet: IncomingPacket
) -> IncomingPacket:
    trans_msg = decode_trans_msg(packet.data)
    # Make Response
    resp = encode_push_response(
        client,
        packet.seq,
        trans_msg.svrIp
    )
    await client.send(packet.seq, "OnlinePush.RespPush", resp)  # seems not working?
    if str(packet.seq) in client._online_push_cache:
        return packet
    else:
        client._online_push_cache[str(packet.seq)] = None

    # Parse
    if trans_msg.type == 34:  # LeaveEvent
        group, target, subtype, operator = struct.unpack("!IxIBI", trans_msg.data[:14])
        if subtype in (2, 130):
            client.dispatch_event(GroupMemberLeaveEvent(
                group,
                target
            ))
        else:
            if target == client.uin:
                operator = target
            client.dispatch_event(GroupMemberLeaveEvent(
                group,
                target,
                operator,
                subtype in (1, 129)
            ))
    elif trans_msg.type == 44:
        group, subtype, v1 = struct.unpack("!IBxI", trans_msg.data[:10])
        if subtype in (0, 1):
            client.dispatch_event(GroupMemberPermissionChangeEvent(
                group,
                v1,
                trans_msg.data[10] > 0
            ))
        elif subtype == 255:
            client.dispatch_event(TransferGroupEvent(
                group,
                v1,
                struct.unpack("!I", trans_msg.data[10:14])[0]
            ))
    else:
        logger.warning("OnlinePush.PbPushTransMsg: Unknown type -> " + str(trans_msg.type))

    return packet


__all__ = [
    "handle_c2c_sync",
    "handle_push_msg",
    "handle_req_push",
    "handle_push_trans_msg",
    "PushMsgCommand",
    "PushMsg",
    "PushMsgError",
]
