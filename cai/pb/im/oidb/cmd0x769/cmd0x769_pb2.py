# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cai/pb/im/oidb/cmd0x769/cmd0x769.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&cai/pb/im/oidb/cmd0x769/cmd0x769.proto\x12\x10im.oidb.cmd0x769\"6\n\x03\x43PU\x12\r\n\x05model\x18\x01 \x01(\t\x12\r\n\x05\x63ores\x18\x02 \x01(\r\x12\x11\n\tfrequency\x18\x03 \x01(\r\";\n\x06\x43\x61mera\x12\x0f\n\x07primary\x18\x01 \x01(\x04\x12\x11\n\tsecondary\x18\x02 \x01(\x04\x12\r\n\x05\x66lash\x18\x03 \x01(\x08\"\x85\x01\n\x06\x43onfig\x12\x0c\n\x04type\x18\x01 \x01(\r\x12\x0f\n\x07version\x18\x02 \x01(\r\x12\x14\n\x0c\x63ontent_list\x18\x03 \x03(\t\x12\x11\n\tdebug_msg\x18\x04 \x01(\t\x12\x33\n\x10msg_content_list\x18\x05 \x03(\x0b\x32\x19.im.oidb.cmd0x769.Content\"*\n\tConfigSeq\x12\x0c\n\x04type\x18\x01 \x01(\r\x12\x0f\n\x07version\x18\x02 \x01(\r\"=\n\x07\x43ontent\x12\x0f\n\x07task_id\x18\x01 \x01(\r\x12\x10\n\x08\x63ompress\x18\x02 \x01(\r\x12\x0f\n\x07\x63ontent\x18\n \x01(\x0c\"\x9a\x02\n\nDeviceInfo\x12\r\n\x05\x62rand\x18\x01 \x01(\t\x12\r\n\x05model\x18\x02 \x01(\t\x12 \n\x02os\x18\x03 \x01(\x0b\x32\x14.im.oidb.cmd0x769.OS\x12\"\n\x03\x63pu\x18\x04 \x01(\x0b\x32\x15.im.oidb.cmd0x769.CPU\x12(\n\x06memory\x18\x05 \x01(\x0b\x32\x18.im.oidb.cmd0x769.Memory\x12*\n\x07storage\x18\x06 \x01(\x0b\x32\x19.im.oidb.cmd0x769.Storage\x12(\n\x06screen\x18\x07 \x01(\x0b\x32\x18.im.oidb.cmd0x769.Screen\x12(\n\x06\x63\x61mera\x18\x08 \x01(\x0b\x32\x18.im.oidb.cmd0x769.Camera\"(\n\x06Memory\x12\r\n\x05total\x18\x01 \x01(\x04\x12\x0f\n\x07process\x18\x02 \x01(\x04\"M\n\x02OS\x12\x0c\n\x04type\x18\x01 \x01(\r\x12\x0f\n\x07version\x18\x02 \x01(\t\x12\x0b\n\x03sdk\x18\x03 \x01(\t\x12\x0e\n\x06kernel\x18\x04 \x01(\t\x12\x0b\n\x03rom\x18\x05 \x01(\t\">\n\x17QueryUinPackageUsageReq\x12\x0c\n\x04type\x18\x01 \x01(\r\x12\x15\n\ruin_file_size\x18\x02 \x01(\x04\"\xad\x01\n\x17QueryUinPackageUsageRsp\x12\x0e\n\x06status\x18\x01 \x01(\r\x12\x14\n\x0cleft_uin_num\x18\x02 \x01(\x04\x12\x13\n\x0bmax_uin_num\x18\x03 \x01(\x04\x12\x12\n\nproportion\x18\x04 \x01(\r\x12\x43\n\x15uin_package_used_list\x18\n \x03(\x0b\x32$.im.oidb.cmd0x769.UinPackageUsedInfo\"\x83\x02\n\x07ReqBody\x12\x30\n\x0b\x63onfig_list\x18\x01 \x03(\x0b\x32\x1b.im.oidb.cmd0x769.ConfigSeq\x12\x31\n\x0b\x64\x65vice_info\x18\x02 \x01(\x0b\x32\x1c.im.oidb.cmd0x769.DeviceInfo\x12\x0c\n\x04info\x18\x03 \x01(\t\x12\x10\n\x08province\x18\x04 \x01(\t\x12\x0c\n\x04\x63ity\x18\x05 \x01(\t\x12\x15\n\rreq_debug_msg\x18\x06 \x01(\x05\x12N\n\x1bquery_uin_package_usage_req\x18\x65 \x01(\x0b\x32).im.oidb.cmd0x769.QueryUinPackageUsageReq\"\x98\x01\n\x07RspBody\x12\x0e\n\x06result\x18\x01 \x01(\r\x12-\n\x0b\x63onfig_list\x18\x02 \x03(\x0b\x32\x18.im.oidb.cmd0x769.Config\x12N\n\x1bquery_uin_package_usage_rsp\x18\x65 \x01(\x0b\x32).im.oidb.cmd0x769.QueryUinPackageUsageRsp\"X\n\x06Screen\x12\r\n\x05model\x18\x01 \x01(\t\x12\r\n\x05width\x18\x02 \x01(\r\x12\x0e\n\x06height\x18\x03 \x01(\r\x12\x0b\n\x03\x64pi\x18\x04 \x01(\r\x12\x13\n\x0bmulti_touch\x18\x05 \x01(\x08\",\n\x07Storage\x12\x0f\n\x07\x62uiltin\x18\x01 \x01(\x04\x12\x10\n\x08\x65xternal\x18\x02 \x01(\x04\"S\n\x12UinPackageUsedInfo\x12\x0f\n\x07rule_id\x18\x01 \x01(\r\x12\x0e\n\x06\x61uthor\x18\x02 \x01(\t\x12\x0b\n\x03url\x18\x03 \x01(\t\x12\x0f\n\x07uin_num\x18\x04 \x01(\x04')



_CPU = DESCRIPTOR.message_types_by_name['CPU']
_CAMERA = DESCRIPTOR.message_types_by_name['Camera']
_CONFIG = DESCRIPTOR.message_types_by_name['Config']
_CONFIGSEQ = DESCRIPTOR.message_types_by_name['ConfigSeq']
_CONTENT = DESCRIPTOR.message_types_by_name['Content']
_DEVICEINFO = DESCRIPTOR.message_types_by_name['DeviceInfo']
_MEMORY = DESCRIPTOR.message_types_by_name['Memory']
_OS = DESCRIPTOR.message_types_by_name['OS']
_QUERYUINPACKAGEUSAGEREQ = DESCRIPTOR.message_types_by_name['QueryUinPackageUsageReq']
_QUERYUINPACKAGEUSAGERSP = DESCRIPTOR.message_types_by_name['QueryUinPackageUsageRsp']
_REQBODY = DESCRIPTOR.message_types_by_name['ReqBody']
_RSPBODY = DESCRIPTOR.message_types_by_name['RspBody']
_SCREEN = DESCRIPTOR.message_types_by_name['Screen']
_STORAGE = DESCRIPTOR.message_types_by_name['Storage']
_UINPACKAGEUSEDINFO = DESCRIPTOR.message_types_by_name['UinPackageUsedInfo']
CPU = _reflection.GeneratedProtocolMessageType('CPU', (_message.Message,), {
  'DESCRIPTOR' : _CPU,
  '__module__' : 'cai.pb.im.oidb.cmd0x769.cmd0x769_pb2'
  # @@protoc_insertion_point(class_scope:im.oidb.cmd0x769.CPU)
  })
_sym_db.RegisterMessage(CPU)

Camera = _reflection.GeneratedProtocolMessageType('Camera', (_message.Message,), {
  'DESCRIPTOR' : _CAMERA,
  '__module__' : 'cai.pb.im.oidb.cmd0x769.cmd0x769_pb2'
  # @@protoc_insertion_point(class_scope:im.oidb.cmd0x769.Camera)
  })
_sym_db.RegisterMessage(Camera)

Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), {
  'DESCRIPTOR' : _CONFIG,
  '__module__' : 'cai.pb.im.oidb.cmd0x769.cmd0x769_pb2'
  # @@protoc_insertion_point(class_scope:im.oidb.cmd0x769.Config)
  })
_sym_db.RegisterMessage(Config)

ConfigSeq = _reflection.GeneratedProtocolMessageType('ConfigSeq', (_message.Message,), {
  'DESCRIPTOR' : _CONFIGSEQ,
  '__module__' : 'cai.pb.im.oidb.cmd0x769.cmd0x769_pb2'
  # @@protoc_insertion_point(class_scope:im.oidb.cmd0x769.ConfigSeq)
  })
_sym_db.RegisterMessage(ConfigSeq)

Content = _reflection.GeneratedProtocolMessageType('Content', (_message.Message,), {
  'DESCRIPTOR' : _CONTENT,
  '__module__' : 'cai.pb.im.oidb.cmd0x769.cmd0x769_pb2'
  # @@protoc_insertion_point(class_scope:im.oidb.cmd0x769.Content)
  })
_sym_db.RegisterMessage(Content)

DeviceInfo = _reflection.GeneratedProtocolMessageType('DeviceInfo', (_message.Message,), {
  'DESCRIPTOR' : _DEVICEINFO,
  '__module__' : 'cai.pb.im.oidb.cmd0x769.cmd0x769_pb2'
  # @@protoc_insertion_point(class_scope:im.oidb.cmd0x769.DeviceInfo)
  })
_sym_db.RegisterMessage(DeviceInfo)

Memory = _reflection.GeneratedProtocolMessageType('Memory', (_message.Message,), {
  'DESCRIPTOR' : _MEMORY,
  '__module__' : 'cai.pb.im.oidb.cmd0x769.cmd0x769_pb2'
  # @@protoc_insertion_point(class_scope:im.oidb.cmd0x769.Memory)
  })
_sym_db.RegisterMessage(Memory)

OS = _reflection.GeneratedProtocolMessageType('OS', (_message.Message,), {
  'DESCRIPTOR' : _OS,
  '__module__' : 'cai.pb.im.oidb.cmd0x769.cmd0x769_pb2'
  # @@protoc_insertion_point(class_scope:im.oidb.cmd0x769.OS)
  })
_sym_db.RegisterMessage(OS)

QueryUinPackageUsageReq = _reflection.GeneratedProtocolMessageType('QueryUinPackageUsageReq', (_message.Message,), {
  'DESCRIPTOR' : _QUERYUINPACKAGEUSAGEREQ,
  '__module__' : 'cai.pb.im.oidb.cmd0x769.cmd0x769_pb2'
  # @@protoc_insertion_point(class_scope:im.oidb.cmd0x769.QueryUinPackageUsageReq)
  })
_sym_db.RegisterMessage(QueryUinPackageUsageReq)

QueryUinPackageUsageRsp = _reflection.GeneratedProtocolMessageType('QueryUinPackageUsageRsp', (_message.Message,), {
  'DESCRIPTOR' : _QUERYUINPACKAGEUSAGERSP,
  '__module__' : 'cai.pb.im.oidb.cmd0x769.cmd0x769_pb2'
  # @@protoc_insertion_point(class_scope:im.oidb.cmd0x769.QueryUinPackageUsageRsp)
  })
_sym_db.RegisterMessage(QueryUinPackageUsageRsp)

ReqBody = _reflection.GeneratedProtocolMessageType('ReqBody', (_message.Message,), {
  'DESCRIPTOR' : _REQBODY,
  '__module__' : 'cai.pb.im.oidb.cmd0x769.cmd0x769_pb2'
  # @@protoc_insertion_point(class_scope:im.oidb.cmd0x769.ReqBody)
  })
_sym_db.RegisterMessage(ReqBody)

RspBody = _reflection.GeneratedProtocolMessageType('RspBody', (_message.Message,), {
  'DESCRIPTOR' : _RSPBODY,
  '__module__' : 'cai.pb.im.oidb.cmd0x769.cmd0x769_pb2'
  # @@protoc_insertion_point(class_scope:im.oidb.cmd0x769.RspBody)
  })
_sym_db.RegisterMessage(RspBody)

Screen = _reflection.GeneratedProtocolMessageType('Screen', (_message.Message,), {
  'DESCRIPTOR' : _SCREEN,
  '__module__' : 'cai.pb.im.oidb.cmd0x769.cmd0x769_pb2'
  # @@protoc_insertion_point(class_scope:im.oidb.cmd0x769.Screen)
  })
_sym_db.RegisterMessage(Screen)

Storage = _reflection.GeneratedProtocolMessageType('Storage', (_message.Message,), {
  'DESCRIPTOR' : _STORAGE,
  '__module__' : 'cai.pb.im.oidb.cmd0x769.cmd0x769_pb2'
  # @@protoc_insertion_point(class_scope:im.oidb.cmd0x769.Storage)
  })
_sym_db.RegisterMessage(Storage)

UinPackageUsedInfo = _reflection.GeneratedProtocolMessageType('UinPackageUsedInfo', (_message.Message,), {
  'DESCRIPTOR' : _UINPACKAGEUSEDINFO,
  '__module__' : 'cai.pb.im.oidb.cmd0x769.cmd0x769_pb2'
  # @@protoc_insertion_point(class_scope:im.oidb.cmd0x769.UinPackageUsedInfo)
  })
_sym_db.RegisterMessage(UinPackageUsedInfo)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CPU._serialized_start=60
  _CPU._serialized_end=114
  _CAMERA._serialized_start=116
  _CAMERA._serialized_end=175
  _CONFIG._serialized_start=178
  _CONFIG._serialized_end=311
  _CONFIGSEQ._serialized_start=313
  _CONFIGSEQ._serialized_end=355
  _CONTENT._serialized_start=357
  _CONTENT._serialized_end=418
  _DEVICEINFO._serialized_start=421
  _DEVICEINFO._serialized_end=703
  _MEMORY._serialized_start=705
  _MEMORY._serialized_end=745
  _OS._serialized_start=747
  _OS._serialized_end=824
  _QUERYUINPACKAGEUSAGEREQ._serialized_start=826
  _QUERYUINPACKAGEUSAGEREQ._serialized_end=888
  _QUERYUINPACKAGEUSAGERSP._serialized_start=891
  _QUERYUINPACKAGEUSAGERSP._serialized_end=1064
  _REQBODY._serialized_start=1067
  _REQBODY._serialized_end=1326
  _RSPBODY._serialized_start=1329
  _RSPBODY._serialized_end=1481
  _SCREEN._serialized_start=1483
  _SCREEN._serialized_end=1571
  _STORAGE._serialized_start=1573
  _STORAGE._serialized_end=1617
  _UINPACKAGEUSEDINFO._serialized_start=1619
  _UINPACKAGEUSEDINFO._serialized_end=1702
# @@protoc_insertion_point(module_scope)
