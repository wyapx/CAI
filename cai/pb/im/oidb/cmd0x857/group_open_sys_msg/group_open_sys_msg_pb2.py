# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cai/pb/im/oidb/cmd0x857/group_open_sys_msg/group_open_sys_msg.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nCcai/pb/im/oidb/cmd0x857/group_open_sys_msg/group_open_sys_msg.proto\x12#im.oidb.cmd0x857.group_open_sys_msg\"\xab\x01\n\x08LightApp\x12\x0b\n\x03\x61pp\x18\x01 \x01(\t\x12\x0c\n\x04view\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x65sc\x18\x03 \x01(\t\x12\x0e\n\x06prompt\x18\x04 \x01(\t\x12\x0b\n\x03ver\x18\x05 \x01(\t\x12\x0c\n\x04meta\x18\x06 \x01(\t\x12\x0e\n\x06\x63onfig\x18\x07 \x01(\t\x12;\n\x06source\x18\x08 \x01(\x0b\x32+.im.oidb.cmd0x857.group_open_sys_msg.Source\"\x8e\x01\n\x07RichMsg\x12\r\n\x05title\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x65sc\x18\x02 \x01(\t\x12\r\n\x05\x62rief\x18\x03 \x01(\t\x12\r\n\x05\x63over\x18\x04 \x01(\t\x12\x0b\n\x03url\x18\x05 \x01(\t\x12;\n\x06source\x18\x06 \x01(\x0b\x32+.im.oidb.cmd0x857.group_open_sys_msg.Source\"@\n\x06Sender\x12\x0b\n\x03uin\x18\x01 \x01(\x04\x12\x0c\n\x04nick\x18\x02 \x01(\t\x12\x0e\n\x06\x61vatar\x18\x03 \x01(\t\x12\x0b\n\x03url\x18\x04 \x01(\t\"1\n\x06Source\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04icon\x18\x02 \x01(\t\x12\x0b\n\x03url\x18\x03 \x01(\t\"\x8b\x02\n\nSysMsgBody\x12\x10\n\x08group_id\x18\x01 \x01(\x04\x12\r\n\x05\x61ppid\x18\x02 \x01(\x04\x12;\n\x06sender\x18\x03 \x01(\x0b\x32+.im.oidb.cmd0x857.group_open_sys_msg.Sender\x12\x0c\n\x04type\x18\x04 \x01(\r\x12\x0f\n\x07\x63ontent\x18\x05 \x01(\t\x12>\n\x08rich_msg\x18\x06 \x01(\x0b\x32,.im.oidb.cmd0x857.group_open_sys_msg.RichMsg\x12@\n\tlight_app\x18\x07 \x01(\x0b\x32-.im.oidb.cmd0x857.group_open_sys_msg.LightApp')



_LIGHTAPP = DESCRIPTOR.message_types_by_name['LightApp']
_RICHMSG = DESCRIPTOR.message_types_by_name['RichMsg']
_SENDER = DESCRIPTOR.message_types_by_name['Sender']
_SOURCE = DESCRIPTOR.message_types_by_name['Source']
_SYSMSGBODY = DESCRIPTOR.message_types_by_name['SysMsgBody']
LightApp = _reflection.GeneratedProtocolMessageType('LightApp', (_message.Message,), {
  'DESCRIPTOR' : _LIGHTAPP,
  '__module__' : 'cai.pb.im.oidb.cmd0x857.group_open_sys_msg.group_open_sys_msg_pb2'
  # @@protoc_insertion_point(class_scope:im.oidb.cmd0x857.group_open_sys_msg.LightApp)
  })
_sym_db.RegisterMessage(LightApp)

RichMsg = _reflection.GeneratedProtocolMessageType('RichMsg', (_message.Message,), {
  'DESCRIPTOR' : _RICHMSG,
  '__module__' : 'cai.pb.im.oidb.cmd0x857.group_open_sys_msg.group_open_sys_msg_pb2'
  # @@protoc_insertion_point(class_scope:im.oidb.cmd0x857.group_open_sys_msg.RichMsg)
  })
_sym_db.RegisterMessage(RichMsg)

Sender = _reflection.GeneratedProtocolMessageType('Sender', (_message.Message,), {
  'DESCRIPTOR' : _SENDER,
  '__module__' : 'cai.pb.im.oidb.cmd0x857.group_open_sys_msg.group_open_sys_msg_pb2'
  # @@protoc_insertion_point(class_scope:im.oidb.cmd0x857.group_open_sys_msg.Sender)
  })
_sym_db.RegisterMessage(Sender)

Source = _reflection.GeneratedProtocolMessageType('Source', (_message.Message,), {
  'DESCRIPTOR' : _SOURCE,
  '__module__' : 'cai.pb.im.oidb.cmd0x857.group_open_sys_msg.group_open_sys_msg_pb2'
  # @@protoc_insertion_point(class_scope:im.oidb.cmd0x857.group_open_sys_msg.Source)
  })
_sym_db.RegisterMessage(Source)

SysMsgBody = _reflection.GeneratedProtocolMessageType('SysMsgBody', (_message.Message,), {
  'DESCRIPTOR' : _SYSMSGBODY,
  '__module__' : 'cai.pb.im.oidb.cmd0x857.group_open_sys_msg.group_open_sys_msg_pb2'
  # @@protoc_insertion_point(class_scope:im.oidb.cmd0x857.group_open_sys_msg.SysMsgBody)
  })
_sym_db.RegisterMessage(SysMsgBody)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _LIGHTAPP._serialized_start=109
  _LIGHTAPP._serialized_end=280
  _RICHMSG._serialized_start=283
  _RICHMSG._serialized_end=425
  _SENDER._serialized_start=427
  _SENDER._serialized_end=491
  _SOURCE._serialized_start=493
  _SOURCE._serialized_end=542
  _SYSMSGBODY._serialized_start=545
  _SYSMSGBODY._serialized_end=812
# @@protoc_insertion_point(module_scope)
