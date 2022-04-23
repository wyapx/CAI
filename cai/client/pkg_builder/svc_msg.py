from typing import Sequence, Tuple

from cai.pb.msf.msg.svc import PbGroupMsgWithDrawReq, PbMsgWithDrawReq, MessageInfo


# RecallGroupMessage, PbMessageSvc.PbMsgWithDraw
def build_recall_group_msg_pkg(group: int, msg_list: Sequence[Tuple[int, int, int]]) -> PbMsgWithDrawReq:
    return PbMsgWithDrawReq(
        group_with_draw=[PbGroupMsgWithDrawReq(
            sub_cmd=1,
            group_code=group,
            userdef=b"\x08\x00",
            list=[
                MessageInfo(
                    msg_seq=msg[0],
                    msg_random=msg[1],
                    msg_type=0
                ) for msg in msg_list
            ]
        )]
    )
