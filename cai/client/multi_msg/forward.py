import gzip
import hashlib
from typing import List, TYPE_CHECKING, Tuple

from cai.client.message_service.encoders import build_msg
from cai.pb.msf.msg.comm import Msg, MsgHead, MutilTransHead, GroupInfo
from cai.pb.msf.msg.svc import PbMultiMsgTransmit, PbMultiMsgItem, PbMultiMsgNew

if TYPE_CHECKING:
    from cai.client.message_service.models import ForwardNode


def prepare(fm: List["ForwardNode"], seq: int, group: int, random: int) -> Tuple[bytes, bytes]:
    msgs = pack(fm, seq, group, random)
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


def pack(fm: List["ForwardNode"], seq: int, group: int, random: int) -> List[Msg]:
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
            body=build_msg(node.message)
        ) for node in fm
    ]
