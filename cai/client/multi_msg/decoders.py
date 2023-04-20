import struct
from typing import TYPE_CHECKING
from ipaddress import IPv4Address
from gzip import decompress

from cai.pb.highway.long_msg import LongRspBody
from cai.pb.highway.multi_msg import MultiRspBody
from cai.utils.httpcat import HttpCat
from cai.utils.tea import qqtea_decrypt

from .command import ApplyDownCommand, MultiApplyResp

if TYPE_CHECKING:
    from cai.client.session import Session
    from cai.client.packet import IncomingPacket

async def handle_multi_msg_apply_down(
    client: "Session", packet: "IncomingPacket"
) -> ApplyDownCommand:
    body = MultiRspBody.FromString(packet.data)
    assert body.multimsgApplydownRsp
    rsp = body.multimsgApplydownRsp[0]
    assert rsp.thumbDownPara
    if rsp.msgExternInfo and rsp.msgExternInfo.channelType == 2:
        prefix = "https://ssl.htdata.qq.com"
    else:
        prefix = "https://{domain}:{port}".format(
            domain=IPv4Address(rsp.uint32DownIp[0]).compressed,
            port=rsp.uint32DownPort[0]
        )
    http_resp = await HttpCat.request("GET", f"{prefix}{rsp.thumbDownPara.decode()}")
    mv = bytes(http_resp.body)
    if http_resp.code != 200:
        raise AssertionError(http_resp.code, http_resp.text())
    elif mv[0] != 40:
        raise ValueError("bad data")
    cursor = 9
    head_len, body_len = struct.unpack("!ii", mv[1:9])
    if head_len > 0:
        cursor += head_len
    long_rsp = LongRspBody.FromString(
        qqtea_decrypt(
            mv[cursor:cursor + body_len],
            rsp.msgKey
        )
    )
    if not long_rsp.msgDownRsp[0].msgContent:
        raise ValueError("empty content")
    return ApplyDownCommand.decode(
        packet.uin,
        packet.seq,
        packet.ret_code,
        packet.command_name,
        decompress(long_rsp.msgDownRsp[0].msgContent)
    )


async def handle_multi_resp_body(
    client: "Session", pkg: "IncomingPacket"
) -> MultiApplyResp:
    mrb = MultiRspBody.FromString(pkg.data).multimsgApplyupRsp
    if not mrb:
        raise ConnectionError("no MultiMsgApplyUpRsp Found")
    return MultiApplyResp(
        uin=pkg.uin,
        seq=pkg.seq,
        ret_code=pkg.ret_code,
        command_name=pkg.command_name,
        data=mrb[0],
    )
