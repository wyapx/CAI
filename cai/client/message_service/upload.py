import os

from cai.pb.im.oidb.cmd0x388.cmd0x388_pb2 import D388ReqBody, TryUpImgReq, D388RspBody


def encode_d388_req(group_code: int, uin: int, md5: bytes, size: int, build_ver: bytes) -> D388ReqBody:
    fn = md5.hex() + ".gif"
    return D388ReqBody(
        netType=3,
        subcmd=1,
        tryupImgReq=[TryUpImgReq(
            groupCode=group_code,
            srcUin=uin,
            fileName=fn.encode(),
            fileMd5=md5,
            fileSize=size,
            fileId=0,
            srcTerm=5,
            platformType=9,
            buType=1,
            picType=1000,
            buildVer=build_ver,
            appPicType=1006,
            originalPic=0,
        )]
    )


def decode_d388_rsp(data: bytes) -> D388RspBody:
    return D388RspBody.FromString(data)
