import zlib
from typing import Union, Sequence

from cai.pb.msf.msg.svc import PbSendMsgReq
from cai.pb.msf.msg.comm.comm_pb2 import ContentHead
from cai.pb.msf.msg.svc.svc_pb2 import Grp, RoutingHead
from cai.pb.im.msg.service.comm_elem import (
    MsgElemInfo_servtype2,
    MsgElemInfo_servtype3,
)
from cai.pb.im.msg.msg_body import (
    Elem,
    MsgBody,
    RichMsg,
    RichText,
    VideoFile,
    PlainText,
    CommonElem,
    CustomFace,
    ShakeWindow,
    LightAppElem,
    OpenQQData
)

from . import models


def _build_image_elem(
    e: Union[models.ImageElement, models.FlashImageElement]
) -> CustomFace:
    return CustomFace(
        file_type=66,
        useful=1,
        biz_type=0,
        width=e.width,
        height=e.height,
        file_id=e.id,
        file_path=e.filename,
        image_type=e.filetype,
        source=200,
        origin=1,
        size=e.size,
        md5=e.md5,
        show_len=0,
        download_len=0
        # flag=b"\x00\x00\x00\x00"
    )


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
            ret.append(Elem(custom_face=_build_image_elem(e)))
        elif isinstance(e, models.AtElement):
            ret.append(
                Elem(
                    text=PlainText(
                        str=e.display.encode(),
                        attr_6_buf=b"\x00\x01\x00\x00\x00\x03\x00"
                        + e.target.to_bytes(4, "big", signed=False)
                        + b"\x00\x00",
                    )
                )
            )
        elif isinstance(e, models.AtAllElement):
            ret.append(
                Elem(
                    text=PlainText(
                        str="@全体成员".encode(),
                        attr_6_buf=b"\x00\x01\x00\x00\x00\x03\x01\x00\x00\x00\x00\x00\x00",
                    )
                )
            )
        elif isinstance(e, models.RichMsgElement):
            if len(e.content) > 256:  # compress require
                content = b"\x01" + zlib.compress(e.content, level=6)
            else:
                content = b"\x00" + e.content
            if e.service_id == -2:  # LightApp
                ret_elem = Elem(light_app=LightAppElem(data=content))
            else:  # Json & Xml
                ret_elem = Elem(
                    rich_msg=RichMsg(
                        template_1=content,
                        service_id=0 if e.service_id < 0 else e.service_id,
                    )
                )
            ret.append(ret_elem)
        elif isinstance(e, models.ShakeElement):
            ret.append(Elem(shake_window=ShakeWindow(type=e.stype, uin=e.uin)))
            ret.append(  # fallback info
                Elem(text=PlainText(str="[窗口抖动]请使用新版手机QQ查看".encode()))
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
            ptt = e.to_ptt()
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
        elif isinstance(e, models.CustomDataElement):
            ret.append(
                Elem(
                    open_qq_data=OpenQQData(car_qq_data=e.data)
                )
            )
        else:
            raise NotImplementedError(e)

    return MsgBody(rich_text=RichText(elems=ret, ptt=ptt))


def encode_send_group_msg_req(
    seq: int, rand: int, group: int, body: MsgBody, head: ContentHead
) -> PbSendMsgReq:
    return PbSendMsgReq(
        routing_head=RoutingHead(grp=Grp(group_code=group)),
        content_head=head,
        body=body,
        seq=seq,
        rand=rand,
        via=1,
    )


def make_group_msg_pkg(seq: int, gid: int, rand: int, body: MsgBody) -> PbSendMsgReq:
    return encode_send_group_msg_req(
        seq, rand, gid, body, ContentHead(pkg_num=1, pkg_index=0, div_seq=0)
    )
