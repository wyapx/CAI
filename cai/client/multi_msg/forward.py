import gzip
import hashlib
from typing import List, Tuple, TYPE_CHECKING


from cai.client.message_service.models import ForwardNode, ForwardMessage
from cai.client.message_service.decoders import TroopMessageDecoder
from cai.client.message_service.encoders import build_msg
from cai.pb.highway.multi_msg import MultiReqBody, MultiMsgApplyDownReq
from cai.pb.msf.msg.comm import Msg, MsgHead, MutilTransHead, GroupInfo
from cai.pb.msf.msg.svc import PbMultiMsgTransmit, PbMultiMsgItem, PbMultiMsgNew

if TYPE_CHECKING:
    from cai.client import GroupMessage


def prepare_upload(fm: List[ForwardNode], seq: int, group: int, random: int) -> Tuple[bytes, bytes]:
    msgs = _pack(fm, seq, group, random)
    raw = PbMultiMsgTransmit(
        msg=msgs,
        pbItemList=[
            PbMultiMsgItem(
                fileName="MultiMsg",
                buffer=PbMultiMsgNew(msg=msgs).SerializeToString()
            )
        ]
    ).SerializeToString()
    data = gzip.compress(raw)
    return data, hashlib.md5(data).digest()


def prepare_download_req(res_id: bytes) -> bytes:
    """UniPacket, MultiMsg.ApplyDown"""
    return MultiReqBody(
        subcmd=2,
        termType=5,
        platformType=9,
        netType=3,
        buildVer="8.2.0.1297",
        buType=2,
        reqChannelType=2,
        multimsgApplydownReq=[MultiMsgApplyDownReq(
            msgResid=res_id,
            msgType=3
        )]
    ).SerializeToString()


def parse_raw(transmit: PbMultiMsgTransmit, res_id: str) -> ForwardMessage:
    return ForwardMessage(
        transmit.msg[0].head.group_info.group_code,
        res_id,
        "",
        _unpack(transmit)
    )


def _unpack(transmit: PbMultiMsgTransmit) -> List[ForwardNode]:
    msgs: List[ForwardNode] = []
    for msg in transmit.msg:
        tmsg: "GroupMessage" = TroopMessageDecoder.decode(msg)  # noqa
        msgs.append(
            ForwardNode(
                from_uin=tmsg.from_uin,
                nickname=tmsg.from_group_card,
                send_time=tmsg.time,
                message=tmsg.message
            )
        )
    return msgs


def _pack(fm: List[ForwardNode], seq: int, group: int, random: int) -> List[Msg]:
    """internal function"""
    return [
        Msg(
            head=MsgHead(
                from_uin=node.from_uin,
                type=82,
                seq=seq,
                time=node.send_time,
                uid=0x0100000000000000 | (random & 0xFFFFFFFF),
                mutiltrans_head=MutilTransHead(msg_id=1),
                group_info=GroupInfo(
                    group_code=group,
                    group_card=node.nickname.encode()
                )
            ),
            body=build_msg(node.message, compatible=False)
        ) for node in fm
    ]
