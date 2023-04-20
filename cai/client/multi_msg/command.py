from dataclasses import dataclass

from cai.client.command import Command
from cai.pb.highway.multi_msg import MultiMsgApplyUpRsp
from cai.pb.msf.msg.svc import PbMultiMsgTransmit


@dataclass
class ApplyDownCommand(Command):
    transmit: PbMultiMsgTransmit

    @classmethod
    def decode(
        cls,
        uin: int,
        seq: int,
        ret_code: int,
        command_name: str,
        data: bytes
    ) -> "ApplyDownCommand":
        return cls(
            uin,
            seq,
            ret_code,
            command_name,
            transmit=PbMultiMsgTransmit.FromString(data)
        )


@dataclass
class MultiApplyResp(Command):
    data: MultiMsgApplyUpRsp
