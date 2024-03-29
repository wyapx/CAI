# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cai/pb/highway/protocol/highway_head.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*cai/pb/highway/protocol/highway_head.proto\"\x93\x10\n\x0chighway_head\x1a_\n\x13\x43\x32\x43\x43ommonExtendinfo\x12\x0e\n\x06infoId\x18\x01 \x01(\r\x12\x38\n\x10\x66ilterExtendinfo\x18\x02 \x01(\x0b\x32\x1e.highway_head.FilterExtendinfo\x1a\xc8\x01\n\x0f\x44\x61taHighwayHead\x12\x0f\n\x07version\x18\x01 \x01(\r\x12\x0b\n\x03uin\x18\x02 \x01(\x0c\x12\x0f\n\x07\x63ommand\x18\x03 \x01(\x0c\x12\x0b\n\x03seq\x18\x04 \x01(\r\x12\x12\n\nretryTimes\x18\x05 \x01(\r\x12\r\n\x05\x61ppid\x18\x06 \x01(\r\x12\x10\n\x08\x64\x61taflag\x18\x07 \x01(\r\x12\x11\n\tcommandId\x18\x08 \x01(\r\x12\x10\n\x08\x62uildVer\x18\t \x01(\x0c\x12\x10\n\x08localeId\x18\n \x01(\r\x12\r\n\x05\x65nvId\x18\x0b \x01(\r\x1a&\n\x08\x44\x61taHole\x12\r\n\x05\x62\x65gin\x18\x01 \x01(\x04\x12\x0b\n\x03\x65nd\x18\x02 \x01(\x04\x1a\x64\n\x10\x46ilterExtendinfo\x12\x12\n\nfilterFlag\x18\x01 \x01(\r\x12<\n\x12imageFilterRequest\x18\x02 \x01(\x0b\x32 .highway_head.ImageFilterRequest\x1a\x31\n\x0b\x46ilterStyle\x12\x0f\n\x07styleId\x18\x01 \x01(\r\x12\x11\n\tstyleName\x18\x02 \x01(\x0c\x1a\xa2\x01\n\x12ImageFilterRequest\x12\x11\n\tsessionId\x18\x01 \x01(\x0c\x12\x10\n\x08\x63lientIp\x18\x02 \x01(\r\x12\x0b\n\x03uin\x18\x03 \x01(\x04\x12(\n\x05style\x18\x04 \x01(\x0b\x32\x19.highway_head.FilterStyle\x12\r\n\x05width\x18\x05 \x01(\r\x12\x0e\n\x06height\x18\x06 \x01(\r\x12\x11\n\timageData\x18\x07 \x01(\x0c\x1aK\n\x13ImageFilterResponse\x12\x0f\n\x07retCode\x18\x01 \x01(\x05\x12\x11\n\timageData\x18\x02 \x01(\x0c\x12\x10\n\x08\x63ostTime\x18\x03 \x01(\r\x1a\x36\n\x0cLoginSigHead\x12\x14\n\x0cloginsigType\x18\x01 \x01(\r\x12\x10\n\x08loginsig\x18\x02 \x01(\x0c\x1a\x33\n\x10NewServiceTicket\x12\x11\n\tsignature\x18\x01 \x01(\x0c\x12\x0c\n\x04ukey\x18\x02 \x01(\x0c\x1a\xfa\x01\n\nPicInfoExt\x12\x10\n\x08picWidth\x18\x01 \x01(\r\x12\x11\n\tpicHeight\x18\x02 \x01(\r\x12\x0f\n\x07picFlag\x18\x03 \x01(\r\x12\x10\n\x08\x62usiType\x18\x04 \x01(\r\x12\x0f\n\x07srcTerm\x18\x05 \x01(\r\x12\x10\n\x08platType\x18\x06 \x01(\r\x12\x0f\n\x07netType\x18\x07 \x01(\r\x12\x0f\n\x07imgType\x18\x08 \x01(\r\x12\x12\n\nappPicType\x18\t \x01(\r\x12\x1b\n\x13\x65\x63hoCreatedByServer\x18\n \x01(\x0c\x12\x15\n\rqqmeetGuildId\x18\x0b \x01(\x04\x12\x17\n\x0fqqmeetChannelId\x18\x0c \x01(\x04\x1aT\n\rPicRspExtInfo\x12\x0c\n\x04skey\x18\x01 \x01(\x0c\x12\x10\n\x08\x63lientIp\x18\x02 \x01(\r\x12\x10\n\x08upOffset\x18\x03 \x01(\x04\x12\x11\n\tblockSize\x18\x04 \x01(\x04\x1aZ\n\x0cQueryHoleRsp\x12\x0e\n\x06result\x18\x01 \x01(\r\x12(\n\x08\x64\x61taHole\x18\x02 \x03(\x0b\x32\x16.highway_head.DataHole\x12\x10\n\x08\x63ompFlag\x18\x03 \x01(\x08\x1a\xc9\x01\n\x12ReqDataHighwayHead\x12/\n\x08\x62\x61sehead\x18\x01 \x01(\x0b\x32\x1d.highway_head.DataHighwayHead\x12&\n\x07seghead\x18\x02 \x01(\x0b\x32\x15.highway_head.SegHead\x12\x15\n\rreqExtendinfo\x18\x03 \x01(\x0c\x12\x11\n\ttimestamp\x18\x04 \x01(\x04\x12\x30\n\x0cloginSigHead\x18\x05 \x01(\x0b\x32\x1a.highway_head.LoginSigHead\x1a;\n\x07RspBody\x12\x30\n\x0cqueryHoleRsp\x18\x01 \x01(\x0b\x32\x1a.highway_head.QueryHoleRsp\x1a\x81\x02\n\x12RspDataHighwayHead\x12/\n\x08\x62\x61sehead\x18\x01 \x01(\x0b\x32\x1d.highway_head.DataHighwayHead\x12&\n\x07seghead\x18\x02 \x01(\x0b\x32\x15.highway_head.SegHead\x12\x11\n\terrorCode\x18\x03 \x01(\r\x12\x12\n\nallowRetry\x18\x04 \x01(\r\x12\x11\n\tcachecost\x18\x05 \x01(\r\x12\x0e\n\x06htcost\x18\x06 \x01(\r\x12\x15\n\rrspExtendinfo\x18\x07 \x01(\x0c\x12\x11\n\ttimestamp\x18\x08 \x01(\x04\x12\r\n\x05range\x18\t \x01(\x04\x12\x0f\n\x07isReset\x18\n \x01(\r\x1a\xfa\x01\n\x07SegHead\x12\x11\n\tserviceid\x18\x01 \x01(\r\x12\x10\n\x08\x66ilesize\x18\x02 \x01(\x04\x12\x12\n\ndataoffset\x18\x03 \x01(\x04\x12\x12\n\ndatalength\x18\x04 \x01(\r\x12\x0e\n\x06rtcode\x18\x05 \x01(\r\x12\x15\n\rserviceticket\x18\x06 \x01(\x0c\x12\x0c\n\x04\x66lag\x18\x07 \x01(\r\x12\x0b\n\x03md5\x18\x08 \x01(\x0c\x12\x0f\n\x07\x66ileMd5\x18\t \x01(\x0c\x12\x11\n\tcacheAddr\x18\n \x01(\r\x12\x12\n\nqueryTimes\x18\x0b \x01(\r\x12\x15\n\rupdateCacheip\x18\x0c \x01(\r\x12\x11\n\tcachePort\x18\r \x01(\r')



_HIGHWAY_HEAD = DESCRIPTOR.message_types_by_name['highway_head']
_HIGHWAY_HEAD_C2CCOMMONEXTENDINFO = _HIGHWAY_HEAD.nested_types_by_name['C2CCommonExtendinfo']
_HIGHWAY_HEAD_DATAHIGHWAYHEAD = _HIGHWAY_HEAD.nested_types_by_name['DataHighwayHead']
_HIGHWAY_HEAD_DATAHOLE = _HIGHWAY_HEAD.nested_types_by_name['DataHole']
_HIGHWAY_HEAD_FILTEREXTENDINFO = _HIGHWAY_HEAD.nested_types_by_name['FilterExtendinfo']
_HIGHWAY_HEAD_FILTERSTYLE = _HIGHWAY_HEAD.nested_types_by_name['FilterStyle']
_HIGHWAY_HEAD_IMAGEFILTERREQUEST = _HIGHWAY_HEAD.nested_types_by_name['ImageFilterRequest']
_HIGHWAY_HEAD_IMAGEFILTERRESPONSE = _HIGHWAY_HEAD.nested_types_by_name['ImageFilterResponse']
_HIGHWAY_HEAD_LOGINSIGHEAD = _HIGHWAY_HEAD.nested_types_by_name['LoginSigHead']
_HIGHWAY_HEAD_NEWSERVICETICKET = _HIGHWAY_HEAD.nested_types_by_name['NewServiceTicket']
_HIGHWAY_HEAD_PICINFOEXT = _HIGHWAY_HEAD.nested_types_by_name['PicInfoExt']
_HIGHWAY_HEAD_PICRSPEXTINFO = _HIGHWAY_HEAD.nested_types_by_name['PicRspExtInfo']
_HIGHWAY_HEAD_QUERYHOLERSP = _HIGHWAY_HEAD.nested_types_by_name['QueryHoleRsp']
_HIGHWAY_HEAD_REQDATAHIGHWAYHEAD = _HIGHWAY_HEAD.nested_types_by_name['ReqDataHighwayHead']
_HIGHWAY_HEAD_RSPBODY = _HIGHWAY_HEAD.nested_types_by_name['RspBody']
_HIGHWAY_HEAD_RSPDATAHIGHWAYHEAD = _HIGHWAY_HEAD.nested_types_by_name['RspDataHighwayHead']
_HIGHWAY_HEAD_SEGHEAD = _HIGHWAY_HEAD.nested_types_by_name['SegHead']
highway_head = _reflection.GeneratedProtocolMessageType('highway_head', (_message.Message,), {

  'C2CCommonExtendinfo' : _reflection.GeneratedProtocolMessageType('C2CCommonExtendinfo', (_message.Message,), {
    'DESCRIPTOR' : _HIGHWAY_HEAD_C2CCOMMONEXTENDINFO,
    '__module__' : 'cai.pb.highway.protocol.highway_head_pb2'
    # @@protoc_insertion_point(class_scope:highway_head.C2CCommonExtendinfo)
    })
  ,

  'DataHighwayHead' : _reflection.GeneratedProtocolMessageType('DataHighwayHead', (_message.Message,), {
    'DESCRIPTOR' : _HIGHWAY_HEAD_DATAHIGHWAYHEAD,
    '__module__' : 'cai.pb.highway.protocol.highway_head_pb2'
    # @@protoc_insertion_point(class_scope:highway_head.DataHighwayHead)
    })
  ,

  'DataHole' : _reflection.GeneratedProtocolMessageType('DataHole', (_message.Message,), {
    'DESCRIPTOR' : _HIGHWAY_HEAD_DATAHOLE,
    '__module__' : 'cai.pb.highway.protocol.highway_head_pb2'
    # @@protoc_insertion_point(class_scope:highway_head.DataHole)
    })
  ,

  'FilterExtendinfo' : _reflection.GeneratedProtocolMessageType('FilterExtendinfo', (_message.Message,), {
    'DESCRIPTOR' : _HIGHWAY_HEAD_FILTEREXTENDINFO,
    '__module__' : 'cai.pb.highway.protocol.highway_head_pb2'
    # @@protoc_insertion_point(class_scope:highway_head.FilterExtendinfo)
    })
  ,

  'FilterStyle' : _reflection.GeneratedProtocolMessageType('FilterStyle', (_message.Message,), {
    'DESCRIPTOR' : _HIGHWAY_HEAD_FILTERSTYLE,
    '__module__' : 'cai.pb.highway.protocol.highway_head_pb2'
    # @@protoc_insertion_point(class_scope:highway_head.FilterStyle)
    })
  ,

  'ImageFilterRequest' : _reflection.GeneratedProtocolMessageType('ImageFilterRequest', (_message.Message,), {
    'DESCRIPTOR' : _HIGHWAY_HEAD_IMAGEFILTERREQUEST,
    '__module__' : 'cai.pb.highway.protocol.highway_head_pb2'
    # @@protoc_insertion_point(class_scope:highway_head.ImageFilterRequest)
    })
  ,

  'ImageFilterResponse' : _reflection.GeneratedProtocolMessageType('ImageFilterResponse', (_message.Message,), {
    'DESCRIPTOR' : _HIGHWAY_HEAD_IMAGEFILTERRESPONSE,
    '__module__' : 'cai.pb.highway.protocol.highway_head_pb2'
    # @@protoc_insertion_point(class_scope:highway_head.ImageFilterResponse)
    })
  ,

  'LoginSigHead' : _reflection.GeneratedProtocolMessageType('LoginSigHead', (_message.Message,), {
    'DESCRIPTOR' : _HIGHWAY_HEAD_LOGINSIGHEAD,
    '__module__' : 'cai.pb.highway.protocol.highway_head_pb2'
    # @@protoc_insertion_point(class_scope:highway_head.LoginSigHead)
    })
  ,

  'NewServiceTicket' : _reflection.GeneratedProtocolMessageType('NewServiceTicket', (_message.Message,), {
    'DESCRIPTOR' : _HIGHWAY_HEAD_NEWSERVICETICKET,
    '__module__' : 'cai.pb.highway.protocol.highway_head_pb2'
    # @@protoc_insertion_point(class_scope:highway_head.NewServiceTicket)
    })
  ,

  'PicInfoExt' : _reflection.GeneratedProtocolMessageType('PicInfoExt', (_message.Message,), {
    'DESCRIPTOR' : _HIGHWAY_HEAD_PICINFOEXT,
    '__module__' : 'cai.pb.highway.protocol.highway_head_pb2'
    # @@protoc_insertion_point(class_scope:highway_head.PicInfoExt)
    })
  ,

  'PicRspExtInfo' : _reflection.GeneratedProtocolMessageType('PicRspExtInfo', (_message.Message,), {
    'DESCRIPTOR' : _HIGHWAY_HEAD_PICRSPEXTINFO,
    '__module__' : 'cai.pb.highway.protocol.highway_head_pb2'
    # @@protoc_insertion_point(class_scope:highway_head.PicRspExtInfo)
    })
  ,

  'QueryHoleRsp' : _reflection.GeneratedProtocolMessageType('QueryHoleRsp', (_message.Message,), {
    'DESCRIPTOR' : _HIGHWAY_HEAD_QUERYHOLERSP,
    '__module__' : 'cai.pb.highway.protocol.highway_head_pb2'
    # @@protoc_insertion_point(class_scope:highway_head.QueryHoleRsp)
    })
  ,

  'ReqDataHighwayHead' : _reflection.GeneratedProtocolMessageType('ReqDataHighwayHead', (_message.Message,), {
    'DESCRIPTOR' : _HIGHWAY_HEAD_REQDATAHIGHWAYHEAD,
    '__module__' : 'cai.pb.highway.protocol.highway_head_pb2'
    # @@protoc_insertion_point(class_scope:highway_head.ReqDataHighwayHead)
    })
  ,

  'RspBody' : _reflection.GeneratedProtocolMessageType('RspBody', (_message.Message,), {
    'DESCRIPTOR' : _HIGHWAY_HEAD_RSPBODY,
    '__module__' : 'cai.pb.highway.protocol.highway_head_pb2'
    # @@protoc_insertion_point(class_scope:highway_head.RspBody)
    })
  ,

  'RspDataHighwayHead' : _reflection.GeneratedProtocolMessageType('RspDataHighwayHead', (_message.Message,), {
    'DESCRIPTOR' : _HIGHWAY_HEAD_RSPDATAHIGHWAYHEAD,
    '__module__' : 'cai.pb.highway.protocol.highway_head_pb2'
    # @@protoc_insertion_point(class_scope:highway_head.RspDataHighwayHead)
    })
  ,

  'SegHead' : _reflection.GeneratedProtocolMessageType('SegHead', (_message.Message,), {
    'DESCRIPTOR' : _HIGHWAY_HEAD_SEGHEAD,
    '__module__' : 'cai.pb.highway.protocol.highway_head_pb2'
    # @@protoc_insertion_point(class_scope:highway_head.SegHead)
    })
  ,
  'DESCRIPTOR' : _HIGHWAY_HEAD,
  '__module__' : 'cai.pb.highway.protocol.highway_head_pb2'
  # @@protoc_insertion_point(class_scope:highway_head)
  })
_sym_db.RegisterMessage(highway_head)
_sym_db.RegisterMessage(highway_head.C2CCommonExtendinfo)
_sym_db.RegisterMessage(highway_head.DataHighwayHead)
_sym_db.RegisterMessage(highway_head.DataHole)
_sym_db.RegisterMessage(highway_head.FilterExtendinfo)
_sym_db.RegisterMessage(highway_head.FilterStyle)
_sym_db.RegisterMessage(highway_head.ImageFilterRequest)
_sym_db.RegisterMessage(highway_head.ImageFilterResponse)
_sym_db.RegisterMessage(highway_head.LoginSigHead)
_sym_db.RegisterMessage(highway_head.NewServiceTicket)
_sym_db.RegisterMessage(highway_head.PicInfoExt)
_sym_db.RegisterMessage(highway_head.PicRspExtInfo)
_sym_db.RegisterMessage(highway_head.QueryHoleRsp)
_sym_db.RegisterMessage(highway_head.ReqDataHighwayHead)
_sym_db.RegisterMessage(highway_head.RspBody)
_sym_db.RegisterMessage(highway_head.RspDataHighwayHead)
_sym_db.RegisterMessage(highway_head.SegHead)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _HIGHWAY_HEAD._serialized_start=47
  _HIGHWAY_HEAD._serialized_end=2114
  _HIGHWAY_HEAD_C2CCOMMONEXTENDINFO._serialized_start=63
  _HIGHWAY_HEAD_C2CCOMMONEXTENDINFO._serialized_end=158
  _HIGHWAY_HEAD_DATAHIGHWAYHEAD._serialized_start=161
  _HIGHWAY_HEAD_DATAHIGHWAYHEAD._serialized_end=361
  _HIGHWAY_HEAD_DATAHOLE._serialized_start=363
  _HIGHWAY_HEAD_DATAHOLE._serialized_end=401
  _HIGHWAY_HEAD_FILTEREXTENDINFO._serialized_start=403
  _HIGHWAY_HEAD_FILTEREXTENDINFO._serialized_end=503
  _HIGHWAY_HEAD_FILTERSTYLE._serialized_start=505
  _HIGHWAY_HEAD_FILTERSTYLE._serialized_end=554
  _HIGHWAY_HEAD_IMAGEFILTERREQUEST._serialized_start=557
  _HIGHWAY_HEAD_IMAGEFILTERREQUEST._serialized_end=719
  _HIGHWAY_HEAD_IMAGEFILTERRESPONSE._serialized_start=721
  _HIGHWAY_HEAD_IMAGEFILTERRESPONSE._serialized_end=796
  _HIGHWAY_HEAD_LOGINSIGHEAD._serialized_start=798
  _HIGHWAY_HEAD_LOGINSIGHEAD._serialized_end=852
  _HIGHWAY_HEAD_NEWSERVICETICKET._serialized_start=854
  _HIGHWAY_HEAD_NEWSERVICETICKET._serialized_end=905
  _HIGHWAY_HEAD_PICINFOEXT._serialized_start=908
  _HIGHWAY_HEAD_PICINFOEXT._serialized_end=1158
  _HIGHWAY_HEAD_PICRSPEXTINFO._serialized_start=1160
  _HIGHWAY_HEAD_PICRSPEXTINFO._serialized_end=1244
  _HIGHWAY_HEAD_QUERYHOLERSP._serialized_start=1246
  _HIGHWAY_HEAD_QUERYHOLERSP._serialized_end=1336
  _HIGHWAY_HEAD_REQDATAHIGHWAYHEAD._serialized_start=1339
  _HIGHWAY_HEAD_REQDATAHIGHWAYHEAD._serialized_end=1540
  _HIGHWAY_HEAD_RSPBODY._serialized_start=1542
  _HIGHWAY_HEAD_RSPBODY._serialized_end=1601
  _HIGHWAY_HEAD_RSPDATAHIGHWAYHEAD._serialized_start=1604
  _HIGHWAY_HEAD_RSPDATAHIGHWAYHEAD._serialized_end=1861
  _HIGHWAY_HEAD_SEGHEAD._serialized_start=1864
  _HIGHWAY_HEAD_SEGHEAD._serialized_end=2114
# @@protoc_insertion_point(module_scope)
