from typing import Sequence, Tuple

from cai.pb.msf.msg.svc import (
    PbGroupMsgWithDrawReq,
    PbC2CMsgWithDrawReq,
    PbMsgWithDrawReq,
    MessageInfo,
    RoutingHead,
    C2C, PbGetGroupMsgReq
)


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


# RecallPrivateMessage, PbMessageSvc.PbMsgWithDraw
def build_recall_private_msg_pkg(
    from_uin: int,
    to_uin: int,
    msg_list: Sequence[Tuple[int, int, int]],
    is_long_msg=False
) -> PbMsgWithDrawReq:
    return PbMsgWithDrawReq(
        c2c_with_draw=[PbC2CMsgWithDrawReq(
            info=[PbC2CMsgWithDrawReq.MsgInfo(
                from_uin=from_uin,
                to_uin=to_uin,
                msg_seq=seq,
                msg_time=t,
                msg_uid=0x0100000000000000 | (rand & 0xFFFFFFFF),
                msg_random=rand,
                routing_head=RoutingHead(
                    c2c=C2C(
                        to_uin=to_uin
                    )
                )
            ) for (seq, rand, t) in msg_list],
            long_message_flag=bool(is_long_msg),
            sub_cmd=1
        )]
    )


# get group msg from server, MessageSvc.PbGetGroupMsg
def build_get_group_msg_req(
    group_code: int,
    begin_seq: int,
    end_seq: int
) -> PbGetGroupMsgReq:
    return PbGetGroupMsgReq(
        group_code=group_code,
        begin_seq=begin_seq,
        end_seq=end_seq,
        public_group=False
    )
