# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: short_video.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11short_video.proto\"&\n\x08\x44\x61taHole\x12\r\n\x05\x62\x65gin\x18\x01 \x01(\x04\x12\x0b\n\x03\x65nd\x18\x02 \x01(\x04\"4\n\x0c\x45xtensionReq\x12\x13\n\x0bsubBusiType\x18\x01 \x01(\r\x12\x0f\n\x07userCnt\x18\x02 \x01(\r\"f\n\x11PttShortVideoAddr\x12\x10\n\x08hostType\x18\x01 \x01(\r\x12\x0c\n\x04host\x18\n \x03(\t\x12\x0f\n\x07urlArgs\x18\x0b \x01(\t\x12\x10\n\x08hostIpv6\x18\x15 \x03(\t\x12\x0e\n\x06\x64omain\x18\x16 \x03(\t\"\xbb\x01\n\x16PttShortVideoDeleteReq\x12\x0f\n\x07\x66romuin\x18\x01 \x01(\x04\x12\r\n\x05touin\x18\x02 \x01(\x04\x12\x10\n\x08\x63hatType\x18\x03 \x01(\r\x12\x12\n\nclientType\x18\x04 \x01(\r\x12\x0e\n\x06\x66ileid\x18\x05 \x01(\t\x12\x11\n\tgroupCode\x18\x06 \x01(\x04\x12\x11\n\tagentType\x18\x07 \x01(\r\x12\x0f\n\x07\x66ileMd5\x18\x08 \x01(\x0c\x12\x14\n\x0c\x62usinessType\x18\t \x01(\r\":\n\x17PttShortVideoDeleteResp\x12\x0f\n\x07retCode\x18\x01 \x01(\x05\x12\x0e\n\x06retMsg\x18\x02 \x01(\t\"\xfa\x02\n\x18PttShortVideoDownloadReq\x12\x0f\n\x07\x66romuin\x18\x01 \x01(\x04\x12\r\n\x05touin\x18\x02 \x01(\x04\x12\x10\n\x08\x63hatType\x18\x03 \x01(\r\x12\x12\n\nclientType\x18\x04 \x01(\r\x12\x0e\n\x06\x66ileid\x18\x05 \x01(\t\x12\x11\n\tgroupCode\x18\x06 \x01(\x04\x12\x11\n\tagentType\x18\x07 \x01(\r\x12\x0f\n\x07\x66ileMd5\x18\x08 \x01(\x0c\x12\x14\n\x0c\x62usinessType\x18\t \x01(\r\x12\x10\n\x08\x66ileType\x18\n \x01(\r\x12\x10\n\x08\x64ownType\x18\x0b \x01(\r\x12\x11\n\tsceneType\x18\x0c \x01(\r\x12\x15\n\rneedInnerAddr\x18\r \x01(\r\x12\x17\n\x0freqTransferType\x18\x0e \x01(\r\x12\x13\n\x0breqHostType\x18\x0f \x01(\r\x12\x1c\n\x14\x66lagSupportLargeSize\x18\x14 \x01(\r\x12!\n\x19\x66lagClientQuicProtoEnable\x18\x1e \x01(\r\"\x9b\x03\n\x19PttShortVideoDownloadResp\x12\x0f\n\x07retCode\x18\x01 \x01(\x05\x12\x0e\n\x06retMsg\x18\x02 \x01(\t\x12-\n\x0fsameAreaOutAddr\x18\x03 \x03(\x0b\x32\x14.PttShortVideoIpList\x12-\n\x0f\x64iffAreaOutAddr\x18\x04 \x03(\x0b\x32\x14.PttShortVideoIpList\x12\x13\n\x0b\x64ownloadkey\x18\x05 \x01(\x0c\x12\x0f\n\x07\x66ileMd5\x18\x06 \x01(\x0c\x12/\n\x11sameAreaInnerAddr\x18\x07 \x03(\x0b\x32\x14.PttShortVideoIpList\x12/\n\x11\x64iffAreaInnerAddr\x18\x08 \x03(\x0b\x32\x14.PttShortVideoIpList\x12(\n\x0c\x64ownloadAddr\x18\t \x01(\x0b\x32\x12.PttShortVideoAddr\x12\x12\n\nencryptKey\x18\n \x01(\x0c\x12!\n\x19\x66lagServerQuicProtoEnable\x18\x1e \x01(\r\x12\x16\n\x0eserverQuicPara\x18\x1f \x01(\x0c\"\xb1\x02\n\x15PttShortVideoFileInfo\x12\x10\n\x08\x66ileName\x18\x01 \x01(\t\x12\x0f\n\x07\x66ileMd5\x18\x02 \x01(\x0c\x12\x14\n\x0cthumbFileMd5\x18\x03 \x01(\x0c\x12\x10\n\x08\x66ileSize\x18\x04 \x01(\x04\x12\x15\n\rfileResLength\x18\x05 \x01(\r\x12\x14\n\x0c\x66ileResWidth\x18\x06 \x01(\r\x12\x12\n\nfileFormat\x18\x07 \x01(\r\x12\x10\n\x08\x66ileTime\x18\x08 \x01(\r\x12\x15\n\rthumbFileSize\x18\t \x01(\x04\x12\x17\n\x0f\x64\x65\x63ryptVideoMd5\x18\n \x01(\x0c\x12\x17\n\x0f\x64\x65\x63ryptFileSize\x18\x0b \x01(\x04\x12\x17\n\x0f\x64\x65\x63ryptThumbMd5\x18\x0c \x01(\x0c\x12\x18\n\x10\x64\x65\x63ryptThumbSize\x18\r \x01(\x04\"/\n\x13PttShortVideoIpList\x12\n\n\x02ip\x18\x01 \x01(\r\x12\x0c\n\x04port\x18\x02 \x01(\r\"\xac\x02\n\x17PttShortVideoRetweetReq\x12\x0f\n\x07\x66romUin\x18\x01 \x01(\x04\x12\r\n\x05toUin\x18\x02 \x01(\x04\x12\x14\n\x0c\x66romChatType\x18\x03 \x01(\r\x12\x12\n\ntoChatType\x18\x04 \x01(\r\x12\x14\n\x0c\x66romBusiType\x18\x05 \x01(\r\x12\x12\n\ntoBusiType\x18\x06 \x01(\r\x12\x12\n\nclientType\x18\x07 \x01(\r\x12\x35\n\x15PttShortVideoFileInfo\x18\x08 \x01(\x0b\x32\x16.PttShortVideoFileInfo\x12\x11\n\tagentType\x18\t \x01(\r\x12\x0e\n\x06\x66ileid\x18\n \x01(\t\x12\x11\n\tgroupCode\x18\x0b \x01(\x04\x12\x1c\n\x14\x66lagSupportLargeSize\x18\x14 \x01(\r\"\x82\x03\n\x18PttShortVideoRetweetResp\x12\x0f\n\x07retCode\x18\x01 \x01(\x05\x12\x0e\n\x06retMsg\x18\x02 \x01(\t\x12-\n\x0fsameAreaOutAddr\x18\x03 \x03(\x0b\x32\x14.PttShortVideoIpList\x12-\n\x0f\x64iffAreaOutAddr\x18\x04 \x03(\x0b\x32\x14.PttShortVideoIpList\x12\x0e\n\x06\x66ileid\x18\x05 \x01(\t\x12\x0c\n\x04ukey\x18\x06 \x01(\x0c\x12\x11\n\tfileExist\x18\x07 \x01(\r\x12/\n\x11sameAreaInnerAddr\x18\x08 \x03(\x0b\x32\x14.PttShortVideoIpList\x12/\n\x11\x64iffAreaInnerAddr\x18\t \x03(\x0b\x32\x14.PttShortVideoIpList\x12\x1b\n\x08\x64\x61taHole\x18\n \x03(\x0b\x32\t.DataHole\x12\x11\n\tisHotFile\x18\x0b \x01(\r\x12$\n\x1clongVideoCarryWatchPointType\x18\x0c \x01(\r\"\x9c\x02\n\x16PttShortVideoUploadReq\x12\x0f\n\x07\x66romuin\x18\x01 \x01(\x04\x12\r\n\x05touin\x18\x02 \x01(\x04\x12\x10\n\x08\x63hatType\x18\x03 \x01(\r\x12\x12\n\nclientType\x18\x04 \x01(\r\x12\x35\n\x15PttShortVideoFileInfo\x18\x05 \x01(\x0b\x32\x16.PttShortVideoFileInfo\x12\x11\n\tgroupCode\x18\x06 \x01(\x04\x12\x11\n\tagentType\x18\x07 \x01(\r\x12\x14\n\x0c\x62usinessType\x18\x08 \x01(\r\x12\x12\n\nencryptKey\x18\t \x01(\x0c\x12\x17\n\x0fsubBusinessType\x18\n \x01(\r\x12\x1c\n\x14\x66lagSupportLargeSize\x18\x14 \x01(\r\"\x95\x03\n\x17PttShortVideoUploadResp\x12\x0f\n\x07retCode\x18\x01 \x01(\x05\x12\x0e\n\x06retMsg\x18\x02 \x01(\t\x12-\n\x0fsameAreaOutAddr\x18\x03 \x03(\x0b\x32\x14.PttShortVideoIpList\x12-\n\x0f\x64iffAreaOutAddr\x18\x04 \x03(\x0b\x32\x14.PttShortVideoIpList\x12\x0e\n\x06\x66ileid\x18\x05 \x01(\t\x12\x0c\n\x04ukey\x18\x06 \x01(\x0c\x12\x11\n\tfileExist\x18\x07 \x01(\r\x12/\n\x11sameAreaInnerAddr\x18\x08 \x03(\x0b\x32\x14.PttShortVideoIpList\x12/\n\x11\x64iffAreaInnerAddr\x18\t \x03(\x0b\x32\x14.PttShortVideoIpList\x12\x1b\n\x08\x64\x61taHole\x18\n \x03(\x0b\x32\t.DataHole\x12\x12\n\nencryptKey\x18\x0b \x01(\x0c\x12\x11\n\tisHotFile\x18\x0c \x01(\r\x12$\n\x1clongVideoCarryWatchPointType\x18\r \x01(\r\"J\n\rQuicParameter\x12\x12\n\nenableQuic\x18\x01 \x01(\r\x12\x15\n\rencryptionVer\x18\x02 \x01(\r\x12\x0e\n\x06\x66\x65\x63Ver\x18\x03 \x01(\r\"\xae\x02\n\x07ReqBody\x12\x0b\n\x03\x63md\x18\x01 \x01(\r\x12\x0b\n\x03seq\x18\x02 \x01(\r\x12\x38\n\x17PttShortVideoUpload_Req\x18\x03 \x01(\x0b\x32\x17.PttShortVideoUploadReq\x12<\n\x19PttShortVideoDownload_Req\x18\x04 \x01(\x0b\x32\x19.PttShortVideoDownloadReq\x12\x36\n\x14shortVideoRetweetReq\x18\x05 \x03(\x0b\x32\x18.PttShortVideoRetweetReq\x12\x34\n\x13shortVideoDeleteReq\x18\x06 \x03(\x0b\x32\x17.PttShortVideoDeleteReq\x12#\n\x0c\x65xtensionReq\x18\x64 \x03(\x0b\x32\r.ExtensionReq\"\xbc\x02\n\x07RspBody\x12\x0b\n\x03\x63md\x18\x01 \x01(\r\x12\x0b\n\x03seq\x18\x02 \x01(\r\x12:\n\x18PttShortVideoUpload_Resp\x18\x03 \x01(\x0b\x32\x18.PttShortVideoUploadResp\x12>\n\x1aPttShortVideoDownload_Resp\x18\x04 \x01(\x0b\x32\x1a.PttShortVideoDownloadResp\x12\x38\n\x15shortVideoRetweetResp\x18\x05 \x03(\x0b\x32\x19.PttShortVideoRetweetResp\x12\x36\n\x14shortVideoDeleteResp\x18\x06 \x03(\x0b\x32\x18.PttShortVideoDeleteResp\x12\x15\n\rchangeChannel\x18\x64 \x01(\r\x12\x12\n\nallowRetry\x18\x65 \x01(\r')



_DATAHOLE = DESCRIPTOR.message_types_by_name['DataHole']
_EXTENSIONREQ = DESCRIPTOR.message_types_by_name['ExtensionReq']
_PTTSHORTVIDEOADDR = DESCRIPTOR.message_types_by_name['PttShortVideoAddr']
_PTTSHORTVIDEODELETEREQ = DESCRIPTOR.message_types_by_name['PttShortVideoDeleteReq']
_PTTSHORTVIDEODELETERESP = DESCRIPTOR.message_types_by_name['PttShortVideoDeleteResp']
_PTTSHORTVIDEODOWNLOADREQ = DESCRIPTOR.message_types_by_name['PttShortVideoDownloadReq']
_PTTSHORTVIDEODOWNLOADRESP = DESCRIPTOR.message_types_by_name['PttShortVideoDownloadResp']
_PTTSHORTVIDEOFILEINFO = DESCRIPTOR.message_types_by_name['PttShortVideoFileInfo']
_PTTSHORTVIDEOIPLIST = DESCRIPTOR.message_types_by_name['PttShortVideoIpList']
_PTTSHORTVIDEORETWEETREQ = DESCRIPTOR.message_types_by_name['PttShortVideoRetweetReq']
_PTTSHORTVIDEORETWEETRESP = DESCRIPTOR.message_types_by_name['PttShortVideoRetweetResp']
_PTTSHORTVIDEOUPLOADREQ = DESCRIPTOR.message_types_by_name['PttShortVideoUploadReq']
_PTTSHORTVIDEOUPLOADRESP = DESCRIPTOR.message_types_by_name['PttShortVideoUploadResp']
_QUICPARAMETER = DESCRIPTOR.message_types_by_name['QuicParameter']
_REQBODY = DESCRIPTOR.message_types_by_name['ReqBody']
_RSPBODY = DESCRIPTOR.message_types_by_name['RspBody']
DataHole = _reflection.GeneratedProtocolMessageType('DataHole', (_message.Message,), {
  'DESCRIPTOR' : _DATAHOLE,
  '__module__' : 'short_video_pb2'
  # @@protoc_insertion_point(class_scope:DataHole)
  })
_sym_db.RegisterMessage(DataHole)

ExtensionReq = _reflection.GeneratedProtocolMessageType('ExtensionReq', (_message.Message,), {
  'DESCRIPTOR' : _EXTENSIONREQ,
  '__module__' : 'short_video_pb2'
  # @@protoc_insertion_point(class_scope:ExtensionReq)
  })
_sym_db.RegisterMessage(ExtensionReq)

PttShortVideoAddr = _reflection.GeneratedProtocolMessageType('PttShortVideoAddr', (_message.Message,), {
  'DESCRIPTOR' : _PTTSHORTVIDEOADDR,
  '__module__' : 'short_video_pb2'
  # @@protoc_insertion_point(class_scope:PttShortVideoAddr)
  })
_sym_db.RegisterMessage(PttShortVideoAddr)

PttShortVideoDeleteReq = _reflection.GeneratedProtocolMessageType('PttShortVideoDeleteReq', (_message.Message,), {
  'DESCRIPTOR' : _PTTSHORTVIDEODELETEREQ,
  '__module__' : 'short_video_pb2'
  # @@protoc_insertion_point(class_scope:PttShortVideoDeleteReq)
  })
_sym_db.RegisterMessage(PttShortVideoDeleteReq)

PttShortVideoDeleteResp = _reflection.GeneratedProtocolMessageType('PttShortVideoDeleteResp', (_message.Message,), {
  'DESCRIPTOR' : _PTTSHORTVIDEODELETERESP,
  '__module__' : 'short_video_pb2'
  # @@protoc_insertion_point(class_scope:PttShortVideoDeleteResp)
  })
_sym_db.RegisterMessage(PttShortVideoDeleteResp)

PttShortVideoDownloadReq = _reflection.GeneratedProtocolMessageType('PttShortVideoDownloadReq', (_message.Message,), {
  'DESCRIPTOR' : _PTTSHORTVIDEODOWNLOADREQ,
  '__module__' : 'short_video_pb2'
  # @@protoc_insertion_point(class_scope:PttShortVideoDownloadReq)
  })
_sym_db.RegisterMessage(PttShortVideoDownloadReq)

PttShortVideoDownloadResp = _reflection.GeneratedProtocolMessageType('PttShortVideoDownloadResp', (_message.Message,), {
  'DESCRIPTOR' : _PTTSHORTVIDEODOWNLOADRESP,
  '__module__' : 'short_video_pb2'
  # @@protoc_insertion_point(class_scope:PttShortVideoDownloadResp)
  })
_sym_db.RegisterMessage(PttShortVideoDownloadResp)

PttShortVideoFileInfo = _reflection.GeneratedProtocolMessageType('PttShortVideoFileInfo', (_message.Message,), {
  'DESCRIPTOR' : _PTTSHORTVIDEOFILEINFO,
  '__module__' : 'short_video_pb2'
  # @@protoc_insertion_point(class_scope:PttShortVideoFileInfo)
  })
_sym_db.RegisterMessage(PttShortVideoFileInfo)

PttShortVideoIpList = _reflection.GeneratedProtocolMessageType('PttShortVideoIpList', (_message.Message,), {
  'DESCRIPTOR' : _PTTSHORTVIDEOIPLIST,
  '__module__' : 'short_video_pb2'
  # @@protoc_insertion_point(class_scope:PttShortVideoIpList)
  })
_sym_db.RegisterMessage(PttShortVideoIpList)

PttShortVideoRetweetReq = _reflection.GeneratedProtocolMessageType('PttShortVideoRetweetReq', (_message.Message,), {
  'DESCRIPTOR' : _PTTSHORTVIDEORETWEETREQ,
  '__module__' : 'short_video_pb2'
  # @@protoc_insertion_point(class_scope:PttShortVideoRetweetReq)
  })
_sym_db.RegisterMessage(PttShortVideoRetweetReq)

PttShortVideoRetweetResp = _reflection.GeneratedProtocolMessageType('PttShortVideoRetweetResp', (_message.Message,), {
  'DESCRIPTOR' : _PTTSHORTVIDEORETWEETRESP,
  '__module__' : 'short_video_pb2'
  # @@protoc_insertion_point(class_scope:PttShortVideoRetweetResp)
  })
_sym_db.RegisterMessage(PttShortVideoRetweetResp)

PttShortVideoUploadReq = _reflection.GeneratedProtocolMessageType('PttShortVideoUploadReq', (_message.Message,), {
  'DESCRIPTOR' : _PTTSHORTVIDEOUPLOADREQ,
  '__module__' : 'short_video_pb2'
  # @@protoc_insertion_point(class_scope:PttShortVideoUploadReq)
  })
_sym_db.RegisterMessage(PttShortVideoUploadReq)

PttShortVideoUploadResp = _reflection.GeneratedProtocolMessageType('PttShortVideoUploadResp', (_message.Message,), {
  'DESCRIPTOR' : _PTTSHORTVIDEOUPLOADRESP,
  '__module__' : 'short_video_pb2'
  # @@protoc_insertion_point(class_scope:PttShortVideoUploadResp)
  })
_sym_db.RegisterMessage(PttShortVideoUploadResp)

QuicParameter = _reflection.GeneratedProtocolMessageType('QuicParameter', (_message.Message,), {
  'DESCRIPTOR' : _QUICPARAMETER,
  '__module__' : 'short_video_pb2'
  # @@protoc_insertion_point(class_scope:QuicParameter)
  })
_sym_db.RegisterMessage(QuicParameter)

ReqBody = _reflection.GeneratedProtocolMessageType('ReqBody', (_message.Message,), {
  'DESCRIPTOR' : _REQBODY,
  '__module__' : 'short_video_pb2'
  # @@protoc_insertion_point(class_scope:ReqBody)
  })
_sym_db.RegisterMessage(ReqBody)

RspBody = _reflection.GeneratedProtocolMessageType('RspBody', (_message.Message,), {
  'DESCRIPTOR' : _RSPBODY,
  '__module__' : 'short_video_pb2'
  # @@protoc_insertion_point(class_scope:RspBody)
  })
_sym_db.RegisterMessage(RspBody)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _DATAHOLE._serialized_start=21
  _DATAHOLE._serialized_end=59
  _EXTENSIONREQ._serialized_start=61
  _EXTENSIONREQ._serialized_end=113
  _PTTSHORTVIDEOADDR._serialized_start=115
  _PTTSHORTVIDEOADDR._serialized_end=217
  _PTTSHORTVIDEODELETEREQ._serialized_start=220
  _PTTSHORTVIDEODELETEREQ._serialized_end=407
  _PTTSHORTVIDEODELETERESP._serialized_start=409
  _PTTSHORTVIDEODELETERESP._serialized_end=467
  _PTTSHORTVIDEODOWNLOADREQ._serialized_start=470
  _PTTSHORTVIDEODOWNLOADREQ._serialized_end=848
  _PTTSHORTVIDEODOWNLOADRESP._serialized_start=851
  _PTTSHORTVIDEODOWNLOADRESP._serialized_end=1262
  _PTTSHORTVIDEOFILEINFO._serialized_start=1265
  _PTTSHORTVIDEOFILEINFO._serialized_end=1570
  _PTTSHORTVIDEOIPLIST._serialized_start=1572
  _PTTSHORTVIDEOIPLIST._serialized_end=1619
  _PTTSHORTVIDEORETWEETREQ._serialized_start=1622
  _PTTSHORTVIDEORETWEETREQ._serialized_end=1922
  _PTTSHORTVIDEORETWEETRESP._serialized_start=1925
  _PTTSHORTVIDEORETWEETRESP._serialized_end=2311
  _PTTSHORTVIDEOUPLOADREQ._serialized_start=2314
  _PTTSHORTVIDEOUPLOADREQ._serialized_end=2598
  _PTTSHORTVIDEOUPLOADRESP._serialized_start=2601
  _PTTSHORTVIDEOUPLOADRESP._serialized_end=3006
  _QUICPARAMETER._serialized_start=3008
  _QUICPARAMETER._serialized_end=3082
  _REQBODY._serialized_start=3085
  _REQBODY._serialized_end=3387
  _RSPBODY._serialized_start=3390
  _RSPBODY._serialized_end=3706
# @@protoc_insertion_point(module_scope)
