import struct
import zlib
from typing import Union, Sequence, Optional

from cai.pb.msf.msg.svc import PbSendMsgReq
from cai.pb.msf.msg.comm.comm_pb2 import ContentHead
from cai.pb.msf.msg.svc.svc_pb2 import Grp, RoutingHead, C2C
from cai.pb.im.msg.service.comm_elem import (
    MsgElemInfo_servtype2,
    MsgElemInfo_servtype3,
)
from cai.pb.im.msg.resv import CustomFaceExtPb
from cai.pb.msf.msg.ctrl import MsgCtrl
from cai.pb.im.msg.msg_body import (
    Elem,
    Face,
    MsgBody,
    RichMsg,
    RichText,
    SourceMsg,
    VideoFile,
    PlainText,
    CommonElem,
    CustomFace,
    ShakeWindow,
    LightAppElem,
    OpenQQData,
)

from . import models


def _build_image_elem(
    e: Union[models.ImageElement, models.FlashImageElement]
) -> CustomFace:
    return CustomFace(
        file_type=66,
        useful=1,
        biz_type=5,
        width=e.width,
        height=e.height,
        file_id=e.id,
        file_path=e.filename,
        image_type=e.filetype,
        source=200,
        origin=1 if not e.is_emoji else 0,
        size=e.size,
        md5=e.md5,
        show_len=0,
        download_len=0,
        pb_reserve=CustomFaceExtPb.ResvAttr(
            imageBizType=1 if e.is_emoji else 0,
            customfaceType=0,
            emojiPackageid=0 if e.filename.endswith(".gif") else None,
            textSummary=("[动画表情]" if e.is_emoji else "[图片]").encode(),
            emojiFrom=0,
            source=6 if e.is_emoji else 2
        ).SerializeToString(),
        flag=b"\x00\x00\x00\x00"
    )


def _build_rich_msg(data: bytes, service_id: int) -> Elem:
    if len(data) > 256:  # compress require
        content = b"\x01" + zlib.compress(data, level=6)
    else:
        content = b"\x00" + data
    if service_id == 0:  # LightApp
        return Elem(light_app=LightAppElem(data=content))
    else:  # Json & Xml
        return Elem(
            rich_msg=RichMsg(
                template_1=content,
                service_id=0 if service_id < 0 else service_id,
            )
        )


def _fill_forward_msg_tpl(res_id: str, filename: str, msg_len: int) -> bytes:
    return f'<?xml version=\'1.0\' encoding=\'UTF-8\' standalone=\'yes\' ?>' \
           f'<msg serviceID="35" templateID="1" action="viewMultiMsg" brief="[聊天记录]" m_resid="{res_id}" m_fileName="{filename}" tSum="3" sourceMsgId="0" url="" flag="3" adverSign="0" multiMsgFlag="0">' \
           f'<item layout="1" advertiser_id="0" aid="0">' \
           f'<title size="34" maxLines="2" lineSpace="12">群聊的聊天记录</title><title size="26" color="#777700" maxLines="2" lineSpace="12">点击查看聊天记录</title>' \
           f'<hr hidden="false" style="0" /><summary size="26" color="#777777">查看{msg_len}条转发消息</summary>' \
           f'</item><source name="聊天记录？" icon="" action="" appid="-1" /></msg>'.encode()


def build_msg(elements: Sequence[models.Element]) -> MsgBody:
    ret = []
    ptt = None
    for e in elements:  # todo: support more element
        if isinstance(e, models.TextElement):
            ret.append(Elem(text=PlainText(str=e.content.encode())))
        elif isinstance(e, models.FlashImageElement):
            ret.append(
                Elem(
                    common_elem=CommonElem(
                        service_type=3,
                        pb_elem=MsgElemInfo_servtype3(
                            flash_troop_pic=_build_image_elem(e)
                        ).SerializeToString(),
                    )
                )
            )
            ret.append(  # fallback info
                Elem(text=PlainText(str="[闪照]请使用新版手机QQ查看".encode()))
            )
        elif isinstance(e, models.ImageElement):
            if e.filename.endswith(".gif"):
                e.is_emoji = True
            ret.append(Elem(custom_face=_build_image_elem(e)))
        elif isinstance(e, models.AtElement):
            ret.append(
                Elem(
                    text=PlainText(
                        str=e.display.encode(),
                        attr_6_buf=struct.pack("!xb3xbbI2x", 1, len(e.display), 0, e.target)
                    )
                )
            )
        elif isinstance(e, models.AtAllElement):
            ret.append(
                Elem(
                    text=PlainText(
                        str="@全体成员".encode(),
                        attr_6_buf=b"\x00\x01\x00\x00\x00\x05\x01\x00\x00\x00\x00\x00\x00",
                    )
                )
            )
        elif isinstance(e, models.RichMsgElement):
            ret.append(
                _build_rich_msg(e.content, e.service_id)
            )
        elif isinstance(e, models.ShakeElement):
            ret.append(Elem(shake_window=ShakeWindow(type=e.stype, uin=e.uin)))
            ret.append(  # fallback info
                Elem(text=PlainText(str="[窗口抖动]请使用新版手机QQ查看".encode()))
            )
        elif isinstance(e, models.FaceElement):
            ret.append(
                Elem(
                    face=Face(
                        index=e.id
                    )
                )
            )
        elif isinstance(e, models.PokeElement):
            ret.append(
                Elem(
                    common_elem=CommonElem(
                        service_type=2,
                        business_type=e.id,
                        pb_elem=MsgElemInfo_servtype2(
                            vaspoke_id=0xFFFFFFFF,
                            vaspoke_name=e.name.encode(),
                            poke_type=0,
                            poke_strength=e.strength,
                            double_hit=e.double_hit,
                            poke_flag=0,
                        ).SerializeToString(),
                    )
                )
            )
        elif isinstance(e, models.VoiceElement):
            ptt = e._to_ptt()
            break
        elif isinstance(e, models.VideoElement):
            ret.append(
                Elem(
                    video_file=VideoFile(
                        file_uuid=e.file_uuid,
                        file_md5=e.file_md5,
                        file_name=e.file_name.encode(),
                        file_format=3,
                        file_time=e.file_time,
                        file_size=e.file_size,
                        thumb_width=1280,
                        thumb_height=768,
                        thumb_file_md5=e.thumb_md5,
                        thumb_file_size=e.thumb_size,
                        source=b"camera"  # const?
                    )
                )
            )
            ret.append(  # fallback info
                Elem(text=PlainText(str="[视频短片]请使用新版手机QQ查看".encode()))
            )
        elif isinstance(e, models.ReplyElement):
            display = f"@{e.sender}"
            ret.append(
                Elem(
                    src_msg=SourceMsg(
                        orig_seqs=[e.seq],
                        sender_uin=e.sender,
                        time=e.time,
                        flag=1,
                        elems=build_msg(e.message).rich_text.elems
                    )
                )
            )
            ret.append(
                Elem(
                    text=PlainText(
                        str=display.encode(),
                        attr_6_buf=struct.pack("!xb3xbbI2x", 1, len(display), 0, e.sender)
                    )
                )
            )
        elif isinstance(e, models.ForwardMessage):
            ret.append(
                _build_rich_msg(_fill_forward_msg_tpl(e.res_id, e.file_name, len(e.nodes)), 35)
            )
        elif isinstance(e, models.CustomDataElement):
            ret.append(
                Elem(
                    open_qq_data=OpenQQData(car_qq_data=e.data)
                )
            )
        else:
            raise NotImplementedError(e)

    return MsgBody(rich_text=RichText(elems=ret, ptt=ptt))


def encode_send_msg_req(
    seq: int,
    rand: int,
    body: MsgBody,
    head: ContentHead,
    *,
    group: Optional[int] = None,
    uin: Optional[int] = None
) -> PbSendMsgReq:
    assert group != uin
    return PbSendMsgReq(
        routing_head=RoutingHead(
            c2c=C2C(to_uin=uin) if uin else None,
            grp=Grp(group_code=group) if group else None
        ),
        content_head=head,
        body=body,
        seq=seq,
        rand=rand,
        via=1,
        ctrl=MsgCtrl(flag=4) if getattr(body.rich_text.elems[0].rich_msg, "service_id", 0) == 35 else None
    )


def make_msg_pkg(
    seq: int,
    rand: int,
    body: MsgBody,
    group_id: Optional[int] = None,
    uin: Optional[int] = None,
    *,
    pkg_num: int = 1,
    pkg_index: int = 0,
    div_seq: int = 0
) -> PbSendMsgReq:
    assert uin != group_id
    return encode_send_msg_req(
        seq,
        rand,
        body,
        ContentHead(
            pkg_num=pkg_num,
            pkg_index=pkg_index,
            div_seq=div_seq
        ),
        group=group_id,
        uin=uin
    )
