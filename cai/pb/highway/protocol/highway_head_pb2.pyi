"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
from builtins import (
    bool,
    bytes,
    int,
)

from google.protobuf.descriptor import (
    Descriptor,
    FileDescriptor,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer,
)

from google.protobuf.message import (
    Message,
)

from typing import (
    Iterable,
    Optional,
)

from typing_extensions import (
    Literal,
)


DESCRIPTOR: FileDescriptor

class highway_head(Message):
    """origin name: CSDataHighwayHead"""
    DESCRIPTOR: Descriptor
    class C2CCommonExtendinfo(Message):
        DESCRIPTOR: Descriptor
        INFOID_FIELD_NUMBER: int
        FILTEREXTENDINFO_FIELD_NUMBER: int
        infoId: int
        @property
        def filterExtendinfo(self) -> highway_head.FilterExtendinfo: ...
        def __init__(self,
            *,
            infoId: Optional[int] = ...,
            filterExtendinfo: Optional[highway_head.FilterExtendinfo] = ...,
            ) -> None: ...
        def HasField(self, field_name: Literal["filterExtendinfo",b"filterExtendinfo","infoId",b"infoId"]) -> bool: ...
        def ClearField(self, field_name: Literal["filterExtendinfo",b"filterExtendinfo","infoId",b"infoId"]) -> None: ...

    class DataHighwayHead(Message):
        DESCRIPTOR: Descriptor
        VERSION_FIELD_NUMBER: int
        UIN_FIELD_NUMBER: int
        COMMAND_FIELD_NUMBER: int
        SEQ_FIELD_NUMBER: int
        RETRYTIMES_FIELD_NUMBER: int
        APPID_FIELD_NUMBER: int
        DATAFLAG_FIELD_NUMBER: int
        COMMANDID_FIELD_NUMBER: int
        BUILDVER_FIELD_NUMBER: int
        LOCALEID_FIELD_NUMBER: int
        ENVID_FIELD_NUMBER: int
        version: int
        uin: bytes
        command: bytes
        seq: int
        retryTimes: int
        appid: int
        dataflag: int
        commandId: int
        buildVer: bytes
        localeId: int
        envId: int
        def __init__(self,
            *,
            version: Optional[int] = ...,
            uin: Optional[bytes] = ...,
            command: Optional[bytes] = ...,
            seq: Optional[int] = ...,
            retryTimes: Optional[int] = ...,
            appid: Optional[int] = ...,
            dataflag: Optional[int] = ...,
            commandId: Optional[int] = ...,
            buildVer: Optional[bytes] = ...,
            localeId: Optional[int] = ...,
            envId: Optional[int] = ...,
            ) -> None: ...
        def HasField(self, field_name: Literal["appid",b"appid","buildVer",b"buildVer","command",b"command","commandId",b"commandId","dataflag",b"dataflag","envId",b"envId","localeId",b"localeId","retryTimes",b"retryTimes","seq",b"seq","uin",b"uin","version",b"version"]) -> bool: ...
        def ClearField(self, field_name: Literal["appid",b"appid","buildVer",b"buildVer","command",b"command","commandId",b"commandId","dataflag",b"dataflag","envId",b"envId","localeId",b"localeId","retryTimes",b"retryTimes","seq",b"seq","uin",b"uin","version",b"version"]) -> None: ...

    class DataHole(Message):
        DESCRIPTOR: Descriptor
        BEGIN_FIELD_NUMBER: int
        END_FIELD_NUMBER: int
        begin: int
        end: int
        def __init__(self,
            *,
            begin: Optional[int] = ...,
            end: Optional[int] = ...,
            ) -> None: ...
        def HasField(self, field_name: Literal["begin",b"begin","end",b"end"]) -> bool: ...
        def ClearField(self, field_name: Literal["begin",b"begin","end",b"end"]) -> None: ...

    class FilterExtendinfo(Message):
        DESCRIPTOR: Descriptor
        FILTERFLAG_FIELD_NUMBER: int
        IMAGEFILTERREQUEST_FIELD_NUMBER: int
        filterFlag: int
        @property
        def imageFilterRequest(self) -> highway_head.ImageFilterRequest: ...
        def __init__(self,
            *,
            filterFlag: Optional[int] = ...,
            imageFilterRequest: Optional[highway_head.ImageFilterRequest] = ...,
            ) -> None: ...
        def HasField(self, field_name: Literal["filterFlag",b"filterFlag","imageFilterRequest",b"imageFilterRequest"]) -> bool: ...
        def ClearField(self, field_name: Literal["filterFlag",b"filterFlag","imageFilterRequest",b"imageFilterRequest"]) -> None: ...

    class FilterStyle(Message):
        DESCRIPTOR: Descriptor
        STYLEID_FIELD_NUMBER: int
        STYLENAME_FIELD_NUMBER: int
        styleId: int
        styleName: bytes
        def __init__(self,
            *,
            styleId: Optional[int] = ...,
            styleName: Optional[bytes] = ...,
            ) -> None: ...
        def HasField(self, field_name: Literal["styleId",b"styleId","styleName",b"styleName"]) -> bool: ...
        def ClearField(self, field_name: Literal["styleId",b"styleId","styleName",b"styleName"]) -> None: ...

    class ImageFilterRequest(Message):
        DESCRIPTOR: Descriptor
        SESSIONID_FIELD_NUMBER: int
        CLIENTIP_FIELD_NUMBER: int
        UIN_FIELD_NUMBER: int
        STYLE_FIELD_NUMBER: int
        WIDTH_FIELD_NUMBER: int
        HEIGHT_FIELD_NUMBER: int
        IMAGEDATA_FIELD_NUMBER: int
        sessionId: bytes
        clientIp: int
        uin: int
        @property
        def style(self) -> highway_head.FilterStyle: ...
        width: int
        height: int
        imageData: bytes
        def __init__(self,
            *,
            sessionId: Optional[bytes] = ...,
            clientIp: Optional[int] = ...,
            uin: Optional[int] = ...,
            style: Optional[highway_head.FilterStyle] = ...,
            width: Optional[int] = ...,
            height: Optional[int] = ...,
            imageData: Optional[bytes] = ...,
            ) -> None: ...
        def HasField(self, field_name: Literal["clientIp",b"clientIp","height",b"height","imageData",b"imageData","sessionId",b"sessionId","style",b"style","uin",b"uin","width",b"width"]) -> bool: ...
        def ClearField(self, field_name: Literal["clientIp",b"clientIp","height",b"height","imageData",b"imageData","sessionId",b"sessionId","style",b"style","uin",b"uin","width",b"width"]) -> None: ...

    class ImageFilterResponse(Message):
        DESCRIPTOR: Descriptor
        RETCODE_FIELD_NUMBER: int
        IMAGEDATA_FIELD_NUMBER: int
        COSTTIME_FIELD_NUMBER: int
        retCode: int
        imageData: bytes
        costTime: int
        def __init__(self,
            *,
            retCode: Optional[int] = ...,
            imageData: Optional[bytes] = ...,
            costTime: Optional[int] = ...,
            ) -> None: ...
        def HasField(self, field_name: Literal["costTime",b"costTime","imageData",b"imageData","retCode",b"retCode"]) -> bool: ...
        def ClearField(self, field_name: Literal["costTime",b"costTime","imageData",b"imageData","retCode",b"retCode"]) -> None: ...

    class LoginSigHead(Message):
        DESCRIPTOR: Descriptor
        LOGINSIGTYPE_FIELD_NUMBER: int
        LOGINSIG_FIELD_NUMBER: int
        loginsigType: int
        loginsig: bytes
        def __init__(self,
            *,
            loginsigType: Optional[int] = ...,
            loginsig: Optional[bytes] = ...,
            ) -> None: ...
        def HasField(self, field_name: Literal["loginsig",b"loginsig","loginsigType",b"loginsigType"]) -> bool: ...
        def ClearField(self, field_name: Literal["loginsig",b"loginsig","loginsigType",b"loginsigType"]) -> None: ...

    class NewServiceTicket(Message):
        DESCRIPTOR: Descriptor
        SIGNATURE_FIELD_NUMBER: int
        UKEY_FIELD_NUMBER: int
        signature: bytes
        ukey: bytes
        def __init__(self,
            *,
            signature: Optional[bytes] = ...,
            ukey: Optional[bytes] = ...,
            ) -> None: ...
        def HasField(self, field_name: Literal["signature",b"signature","ukey",b"ukey"]) -> bool: ...
        def ClearField(self, field_name: Literal["signature",b"signature","ukey",b"ukey"]) -> None: ...

    class PicInfoExt(Message):
        DESCRIPTOR: Descriptor
        PICWIDTH_FIELD_NUMBER: int
        PICHEIGHT_FIELD_NUMBER: int
        PICFLAG_FIELD_NUMBER: int
        BUSITYPE_FIELD_NUMBER: int
        SRCTERM_FIELD_NUMBER: int
        PLATTYPE_FIELD_NUMBER: int
        NETTYPE_FIELD_NUMBER: int
        IMGTYPE_FIELD_NUMBER: int
        APPPICTYPE_FIELD_NUMBER: int
        ECHOCREATEDBYSERVER_FIELD_NUMBER: int
        QQMEETGUILDID_FIELD_NUMBER: int
        QQMEETCHANNELID_FIELD_NUMBER: int
        picWidth: int
        picHeight: int
        picFlag: int
        busiType: int
        srcTerm: int
        platType: int
        netType: int
        imgType: int
        appPicType: int
        echoCreatedByServer: bytes
        qqmeetGuildId: int
        qqmeetChannelId: int
        def __init__(self,
            *,
            picWidth: Optional[int] = ...,
            picHeight: Optional[int] = ...,
            picFlag: Optional[int] = ...,
            busiType: Optional[int] = ...,
            srcTerm: Optional[int] = ...,
            platType: Optional[int] = ...,
            netType: Optional[int] = ...,
            imgType: Optional[int] = ...,
            appPicType: Optional[int] = ...,
            echoCreatedByServer: Optional[bytes] = ...,
            qqmeetGuildId: Optional[int] = ...,
            qqmeetChannelId: Optional[int] = ...,
            ) -> None: ...
        def HasField(self, field_name: Literal["appPicType",b"appPicType","busiType",b"busiType","echoCreatedByServer",b"echoCreatedByServer","imgType",b"imgType","netType",b"netType","picFlag",b"picFlag","picHeight",b"picHeight","picWidth",b"picWidth","platType",b"platType","qqmeetChannelId",b"qqmeetChannelId","qqmeetGuildId",b"qqmeetGuildId","srcTerm",b"srcTerm"]) -> bool: ...
        def ClearField(self, field_name: Literal["appPicType",b"appPicType","busiType",b"busiType","echoCreatedByServer",b"echoCreatedByServer","imgType",b"imgType","netType",b"netType","picFlag",b"picFlag","picHeight",b"picHeight","picWidth",b"picWidth","platType",b"platType","qqmeetChannelId",b"qqmeetChannelId","qqmeetGuildId",b"qqmeetGuildId","srcTerm",b"srcTerm"]) -> None: ...

    class PicRspExtInfo(Message):
        DESCRIPTOR: Descriptor
        SKEY_FIELD_NUMBER: int
        CLIENTIP_FIELD_NUMBER: int
        UPOFFSET_FIELD_NUMBER: int
        BLOCKSIZE_FIELD_NUMBER: int
        skey: bytes
        clientIp: int
        upOffset: int
        blockSize: int
        def __init__(self,
            *,
            skey: Optional[bytes] = ...,
            clientIp: Optional[int] = ...,
            upOffset: Optional[int] = ...,
            blockSize: Optional[int] = ...,
            ) -> None: ...
        def HasField(self, field_name: Literal["blockSize",b"blockSize","clientIp",b"clientIp","skey",b"skey","upOffset",b"upOffset"]) -> bool: ...
        def ClearField(self, field_name: Literal["blockSize",b"blockSize","clientIp",b"clientIp","skey",b"skey","upOffset",b"upOffset"]) -> None: ...

    class QueryHoleRsp(Message):
        DESCRIPTOR: Descriptor
        RESULT_FIELD_NUMBER: int
        DATAHOLE_FIELD_NUMBER: int
        COMPFLAG_FIELD_NUMBER: int
        result: int
        @property
        def dataHole(self) -> RepeatedCompositeFieldContainer[highway_head.DataHole]: ...
        compFlag: bool
        def __init__(self,
            *,
            result: Optional[int] = ...,
            dataHole: Optional[Iterable[highway_head.DataHole]] = ...,
            compFlag: Optional[bool] = ...,
            ) -> None: ...
        def HasField(self, field_name: Literal["compFlag",b"compFlag","result",b"result"]) -> bool: ...
        def ClearField(self, field_name: Literal["compFlag",b"compFlag","dataHole",b"dataHole","result",b"result"]) -> None: ...

    class ReqDataHighwayHead(Message):
        DESCRIPTOR: Descriptor
        BASEHEAD_FIELD_NUMBER: int
        SEGHEAD_FIELD_NUMBER: int
        REQEXTENDINFO_FIELD_NUMBER: int
        TIMESTAMP_FIELD_NUMBER: int
        LOGINSIGHEAD_FIELD_NUMBER: int
        @property
        def basehead(self) -> highway_head.DataHighwayHead: ...
        @property
        def seghead(self) -> highway_head.SegHead: ...
        reqExtendinfo: bytes
        timestamp: int
        @property
        def loginSigHead(self) -> highway_head.LoginSigHead: ...
        def __init__(self,
            *,
            basehead: Optional[highway_head.DataHighwayHead] = ...,
            seghead: Optional[highway_head.SegHead] = ...,
            reqExtendinfo: Optional[bytes] = ...,
            timestamp: Optional[int] = ...,
            loginSigHead: Optional[highway_head.LoginSigHead] = ...,
            ) -> None: ...
        def HasField(self, field_name: Literal["basehead",b"basehead","loginSigHead",b"loginSigHead","reqExtendinfo",b"reqExtendinfo","seghead",b"seghead","timestamp",b"timestamp"]) -> bool: ...
        def ClearField(self, field_name: Literal["basehead",b"basehead","loginSigHead",b"loginSigHead","reqExtendinfo",b"reqExtendinfo","seghead",b"seghead","timestamp",b"timestamp"]) -> None: ...

    class RspBody(Message):
        DESCRIPTOR: Descriptor
        QUERYHOLERSP_FIELD_NUMBER: int
        @property
        def queryHoleRsp(self) -> highway_head.QueryHoleRsp: ...
        def __init__(self,
            *,
            queryHoleRsp: Optional[highway_head.QueryHoleRsp] = ...,
            ) -> None: ...
        def HasField(self, field_name: Literal["queryHoleRsp",b"queryHoleRsp"]) -> bool: ...
        def ClearField(self, field_name: Literal["queryHoleRsp",b"queryHoleRsp"]) -> None: ...

    class RspDataHighwayHead(Message):
        DESCRIPTOR: Descriptor
        BASEHEAD_FIELD_NUMBER: int
        SEGHEAD_FIELD_NUMBER: int
        ERRORCODE_FIELD_NUMBER: int
        ALLOWRETRY_FIELD_NUMBER: int
        CACHECOST_FIELD_NUMBER: int
        HTCOST_FIELD_NUMBER: int
        RSPEXTENDINFO_FIELD_NUMBER: int
        TIMESTAMP_FIELD_NUMBER: int
        RANGE_FIELD_NUMBER: int
        ISRESET_FIELD_NUMBER: int
        @property
        def basehead(self) -> highway_head.DataHighwayHead: ...
        @property
        def seghead(self) -> highway_head.SegHead: ...
        errorCode: int
        allowRetry: int
        cachecost: int
        htcost: int
        rspExtendinfo: bytes
        timestamp: int
        range: int
        isReset: int
        def __init__(self,
            *,
            basehead: Optional[highway_head.DataHighwayHead] = ...,
            seghead: Optional[highway_head.SegHead] = ...,
            errorCode: Optional[int] = ...,
            allowRetry: Optional[int] = ...,
            cachecost: Optional[int] = ...,
            htcost: Optional[int] = ...,
            rspExtendinfo: Optional[bytes] = ...,
            timestamp: Optional[int] = ...,
            range: Optional[int] = ...,
            isReset: Optional[int] = ...,
            ) -> None: ...
        def HasField(self, field_name: Literal["allowRetry",b"allowRetry","basehead",b"basehead","cachecost",b"cachecost","errorCode",b"errorCode","htcost",b"htcost","isReset",b"isReset","range",b"range","rspExtendinfo",b"rspExtendinfo","seghead",b"seghead","timestamp",b"timestamp"]) -> bool: ...
        def ClearField(self, field_name: Literal["allowRetry",b"allowRetry","basehead",b"basehead","cachecost",b"cachecost","errorCode",b"errorCode","htcost",b"htcost","isReset",b"isReset","range",b"range","rspExtendinfo",b"rspExtendinfo","seghead",b"seghead","timestamp",b"timestamp"]) -> None: ...

    class SegHead(Message):
        DESCRIPTOR: Descriptor
        SERVICEID_FIELD_NUMBER: int
        FILESIZE_FIELD_NUMBER: int
        DATAOFFSET_FIELD_NUMBER: int
        DATALENGTH_FIELD_NUMBER: int
        RTCODE_FIELD_NUMBER: int
        SERVICETICKET_FIELD_NUMBER: int
        FLAG_FIELD_NUMBER: int
        MD5_FIELD_NUMBER: int
        FILEMD5_FIELD_NUMBER: int
        CACHEADDR_FIELD_NUMBER: int
        QUERYTIMES_FIELD_NUMBER: int
        UPDATECACHEIP_FIELD_NUMBER: int
        CACHEPORT_FIELD_NUMBER: int
        serviceid: int
        filesize: int
        dataoffset: int
        datalength: int
        rtcode: int
        serviceticket: bytes
        flag: int
        md5: bytes
        fileMd5: bytes
        cacheAddr: int
        queryTimes: int
        updateCacheip: int
        cachePort: int
        def __init__(self,
            *,
            serviceid: Optional[int] = ...,
            filesize: Optional[int] = ...,
            dataoffset: Optional[int] = ...,
            datalength: Optional[int] = ...,
            rtcode: Optional[int] = ...,
            serviceticket: Optional[bytes] = ...,
            flag: Optional[int] = ...,
            md5: Optional[bytes] = ...,
            fileMd5: Optional[bytes] = ...,
            cacheAddr: Optional[int] = ...,
            queryTimes: Optional[int] = ...,
            updateCacheip: Optional[int] = ...,
            cachePort: Optional[int] = ...,
            ) -> None: ...
        def HasField(self, field_name: Literal["cacheAddr",b"cacheAddr","cachePort",b"cachePort","datalength",b"datalength","dataoffset",b"dataoffset","fileMd5",b"fileMd5","filesize",b"filesize","flag",b"flag","md5",b"md5","queryTimes",b"queryTimes","rtcode",b"rtcode","serviceid",b"serviceid","serviceticket",b"serviceticket","updateCacheip",b"updateCacheip"]) -> bool: ...
        def ClearField(self, field_name: Literal["cacheAddr",b"cacheAddr","cachePort",b"cachePort","datalength",b"datalength","dataoffset",b"dataoffset","fileMd5",b"fileMd5","filesize",b"filesize","flag",b"flag","md5",b"md5","queryTimes",b"queryTimes","rtcode",b"rtcode","serviceid",b"serviceid","serviceticket",b"serviceticket","updateCacheip",b"updateCacheip"]) -> None: ...

    def __init__(self,
        ) -> None: ...
