from typing import TYPE_CHECKING, Tuple

from cai.pb.highway.long_msg.long_msg_pb2 import LongReqBody, LongMsgUpReq
from cai.pb.highway.multi_msg.multi_msg_pb2 import (
    MultiReqBody,
    MultiMsgApplyUpReq,
    MultiMsgApplyUpRsp,
)

if TYPE_CHECKING:
    from cai.client.session import Session
    from .command import MultiApplyResp


def _encode_multi_req_body(
    group_id: int, data_len: int, data_md5: bytes, bu_type: int
) -> MultiReqBody:
    return MultiReqBody(
        subcmd=1,
        termType=5,
        platformType=9,
        netType=3,
        buildVer="8.2.0.1297",  # modify
        multimsgApplyupReq=[
            MultiMsgApplyUpReq(
                dstUin=group_id, msgSize=data_len, msgMd5=data_md5, msgType=3
            )
        ],
        buType=bu_type,
    )


async def build_multi_apply_up_pkg(
    client: "Session",
    group_id: int,
    data: bytes,
    data_md5: bytes,
    bu_type: int
) -> Tuple[LongReqBody, MultiMsgApplyUpRsp]:
    body: "MultiApplyResp" = await client.send_unipkg_and_wait(
        "MultiMsg.ApplyUp",
        _encode_multi_req_body(
            group_id, len(data), data_md5, bu_type
        ).SerializeToString(),
    )
    return LongReqBody(
        subcmd=1,
        termType=5,
        platformType=9,
        msgUpReq=[
            LongMsgUpReq(
                msgType=3,
                dstUin=client.uin,
                msgContent=data,
                storeType=2,
                msgUkey=body.data.msgUkey,
            )
        ],
    ), body.data
