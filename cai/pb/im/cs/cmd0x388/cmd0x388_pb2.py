# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cai/pb/im/cs/cmd0x388/cmd0x388.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$cai/pb/im/cs/cmd0x388/cmd0x388.proto\x12\x0eim.cs.cmd0x388\"\xb9\x01\n\tDelImgReq\x12\x0f\n\x07src_uin\x18\x01 \x01(\x04\x12\x0f\n\x07\x64st_uin\x18\x02 \x01(\x04\x12\x10\n\x08req_term\x18\x03 \x01(\r\x12\x19\n\x11req_platform_type\x18\x04 \x01(\r\x12\x0f\n\x07\x62u_type\x18\x05 \x01(\r\x12\x11\n\tbuild_ver\x18\x06 \x01(\x0c\x12\x12\n\nfile_resid\x18\x07 \x01(\x0c\x12\x11\n\tpic_width\x18\x08 \x01(\r\x12\x12\n\npic_height\x18\t \x01(\r\"A\n\tDelImgRsp\x12\x0e\n\x06result\x18\x01 \x01(\r\x12\x10\n\x08\x66\x61il_msg\x18\x02 \x01(\x0c\x12\x12\n\nfile_resid\x18\x03 \x01(\x0c\"\"\n\x11\x45xpRoamExtendInfo\x12\r\n\x05resid\x18\x01 \x01(\x0c\"C\n\x0e\x45xpRoamPicInfo\x12\x11\n\tshop_flag\x18\x01 \x01(\r\x12\x0e\n\x06pkg_id\x18\x02 \x01(\r\x12\x0e\n\x06pic_id\x18\x03 \x01(\x0c\"(\n\x15\x45xtensionCommPicTryUp\x12\x0f\n\x07\x65xtinfo\x18\x01 \x03(\x0c\"Q\n\x15\x45xtensionExpRoamTryUp\x12\x38\n\x10\x65xproam_pic_info\x18\x01 \x03(\x0b\x32\x1e.im.cs.cmd0x388.ExpRoamPicInfo\"\xe5\x03\n\x0cGetImgUrlReq\x12\x12\n\ngroup_code\x18\x01 \x01(\x04\x12\x0f\n\x07\x64st_uin\x18\x02 \x01(\x04\x12\x0e\n\x06\x66ileid\x18\x03 \x01(\x04\x12\x10\n\x08\x66ile_md5\x18\x04 \x01(\x0c\x12\x10\n\x08url_flag\x18\x05 \x01(\r\x12\x10\n\x08url_type\x18\x06 \x01(\r\x12\x10\n\x08req_term\x18\x07 \x01(\r\x12\x19\n\x11req_platform_type\x18\x08 \x01(\r\x12\x10\n\x08inner_ip\x18\t \x01(\r\x12\x0f\n\x07\x62u_type\x18\n \x01(\r\x12\x11\n\tbuild_ver\x18\x0b \x01(\x0c\x12\x0f\n\x07\x66ile_id\x18\x0c \x01(\x04\x12\x11\n\tfile_size\x18\r \x01(\x04\x12\x14\n\x0coriginal_pic\x18\x0e \x01(\r\x12\x11\n\tretry_req\x18\x0f \x01(\r\x12\x13\n\x0b\x66ile_height\x18\x10 \x01(\r\x12\x12\n\nfile_width\x18\x11 \x01(\r\x12\x10\n\x08pic_type\x18\x12 \x01(\r\x12\x18\n\x10pic_up_timestamp\x18\x13 \x01(\r\x12\x19\n\x11req_transfer_type\x18\x14 \x01(\r\x12\x17\n\x0fqqmeet_guild_id\x18\x15 \x01(\x04\x12\x19\n\x11qqmeet_channel_id\x18\x16 \x01(\x04\x12\x16\n\x0e\x64ownload_index\x18\x17 \x01(\x0c\"\x82\x04\n\x0cGetImgUrlRsp\x12\x0e\n\x06\x66ileid\x18\x01 \x01(\x04\x12\x10\n\x08\x66ile_md5\x18\x02 \x01(\x0c\x12\x0e\n\x06result\x18\x03 \x01(\r\x12\x10\n\x08\x66\x61il_msg\x18\x04 \x01(\x0c\x12)\n\x08img_info\x18\x05 \x01(\x0b\x32\x17.im.cs.cmd0x388.ImgInfo\x12\x16\n\x0ethumb_down_url\x18\x06 \x03(\x0c\x12\x19\n\x11original_down_url\x18\x07 \x03(\x0c\x12\x14\n\x0c\x62ig_down_url\x18\x08 \x03(\x0c\x12\x0f\n\x07\x64own_ip\x18\t \x03(\r\x12\x11\n\tdown_port\x18\n \x03(\r\x12\x13\n\x0b\x64own_domain\x18\x0b \x01(\x0c\x12\x17\n\x0fthumb_down_para\x18\x0c \x01(\x0c\x12\x1a\n\x12original_down_para\x18\r \x01(\x0c\x12\x15\n\rbig_down_para\x18\x0e \x01(\x0c\x12\x0f\n\x07\x66ile_id\x18\x0f \x01(\x04\x12\x16\n\x0e\x61uto_down_type\x18\x10 \x01(\r\x12\x17\n\x0forder_down_type\x18\x11 \x03(\r\x12\x1b\n\x13\x62ig_thumb_down_para\x18\x13 \x01(\x0c\x12\x16\n\x0ehttps_url_flag\x18\x14 \x01(\r\x12*\n\x08\x64own_ip6\x18\x1a \x03(\x0b\x32\x18.im.cs.cmd0x388.IPv6Info\x12\x12\n\nclient_ip6\x18\x1b \x01(\x0c\"\xa5\x02\n\x0cGetPttUrlReq\x12\x12\n\ngroup_code\x18\x01 \x01(\x04\x12\x0f\n\x07\x64st_uin\x18\x02 \x01(\x04\x12\x0e\n\x06\x66ileid\x18\x03 \x01(\x04\x12\x10\n\x08\x66ile_md5\x18\x04 \x01(\x0c\x12\x10\n\x08req_term\x18\x05 \x01(\r\x12\x19\n\x11req_platform_type\x18\x06 \x01(\r\x12\x10\n\x08inner_ip\x18\x07 \x01(\r\x12\x0f\n\x07\x62u_type\x18\x08 \x01(\r\x12\x11\n\tbuild_ver\x18\t \x01(\x0c\x12\x0f\n\x07\x66ile_id\x18\n \x01(\x04\x12\x10\n\x08\x66ile_key\x18\x0b \x01(\x0c\x12\r\n\x05\x63odec\x18\x0c \x01(\r\x12\r\n\x05\x62u_id\x18\r \x01(\r\x12\x19\n\x11req_transfer_type\x18\x0e \x01(\r\x12\x0f\n\x07is_auto\x18\x0f \x01(\r\"\xbd\x02\n\x0cGetPttUrlRsp\x12\x0e\n\x06\x66ileid\x18\x01 \x01(\x04\x12\x10\n\x08\x66ile_md5\x18\x02 \x01(\x0c\x12\x0e\n\x06result\x18\x03 \x01(\r\x12\x10\n\x08\x66\x61il_msg\x18\x04 \x01(\x0c\x12\x10\n\x08\x64own_url\x18\x05 \x03(\x0c\x12\x0f\n\x07\x64own_ip\x18\x06 \x03(\r\x12\x11\n\tdown_port\x18\x07 \x03(\r\x12\x13\n\x0b\x64own_domain\x18\x08 \x01(\x0c\x12\x11\n\tdown_para\x18\t \x01(\x0c\x12\x0f\n\x07\x66ile_id\x18\n \x01(\x04\x12\x15\n\rtransfer_type\x18\x0b \x01(\r\x12\x13\n\x0b\x61llow_retry\x18\x0c \x01(\r\x12*\n\x08\x64own_ip6\x18\x1a \x03(\x0b\x32\x18.im.cs.cmd0x388.IPv6Info\x12\x12\n\nclient_ip6\x18\x1b \x01(\x0c\x12\x0e\n\x06\x64omain\x18\x1c \x01(\t\"%\n\x08IPv6Info\x12\x0b\n\x03ip6\x18\x01 \x01(\x0c\x12\x0c\n\x04port\x18\x02 \x01(\r\"j\n\x07ImgInfo\x12\x10\n\x08\x66ile_md5\x18\x01 \x01(\x0c\x12\x11\n\tfile_type\x18\x02 \x01(\r\x12\x11\n\tfile_size\x18\x03 \x01(\x04\x12\x12\n\nfile_width\x18\x04 \x01(\r\x12\x13\n\x0b\x66ile_height\x18\x05 \x01(\r\"8\n\x07PicSize\x12\x10\n\x08original\x18\x01 \x01(\r\x12\r\n\x05thumb\x18\x02 \x01(\r\x12\x0c\n\x04high\x18\x03 \x01(\r\"\xd7\x02\n\x07ReqBody\x12\x10\n\x08net_type\x18\x01 \x01(\r\x12\x0e\n\x06subcmd\x18\x02 \x01(\r\x12\x32\n\rtryup_img_req\x18\x03 \x03(\x0b\x32\x1b.im.cs.cmd0x388.TryUpImgReq\x12\x34\n\x0egetimg_url_req\x18\x04 \x03(\x0b\x32\x1c.im.cs.cmd0x388.GetImgUrlReq\x12\x32\n\rtryup_ptt_req\x18\x05 \x03(\x0b\x32\x1b.im.cs.cmd0x388.TryUpPttReq\x12\x34\n\x0egetptt_url_req\x18\x06 \x03(\x0b\x32\x1c.im.cs.cmd0x388.GetPttUrlReq\x12\x12\n\ncommand_id\x18\x07 \x01(\r\x12.\n\x0b\x64\x65l_img_req\x18\x08 \x03(\x0b\x32\x19.im.cs.cmd0x388.DelImgReq\x12\x12\n\textension\x18\xe9\x07 \x01(\x0c\"\xb0\x02\n\x07RspBody\x12\x11\n\tclient_ip\x18\x01 \x01(\r\x12\x0e\n\x06subcmd\x18\x02 \x01(\r\x12\x32\n\rtryup_img_rsp\x18\x03 \x03(\x0b\x32\x1b.im.cs.cmd0x388.TryUpImgRsp\x12\x34\n\x0egetimg_url_rsp\x18\x04 \x03(\x0b\x32\x1c.im.cs.cmd0x388.GetImgUrlRsp\x12\x32\n\rtryup_ptt_rsp\x18\x05 \x03(\x0b\x32\x1b.im.cs.cmd0x388.TryUpPttRsp\x12\x34\n\x0egetptt_url_rsp\x18\x06 \x03(\x0b\x32\x1c.im.cs.cmd0x388.GetPttUrlRsp\x12.\n\x0b\x64\x65l_img_rsp\x18\x07 \x03(\x0b\x32\x19.im.cs.cmd0x388.DelImgRsp\"\xc2\x03\n\x0bTryUpImgReq\x12\x12\n\ngroup_code\x18\x01 \x01(\x04\x12\x0f\n\x07src_uin\x18\x02 \x01(\x04\x12\x0f\n\x07\x66ile_id\x18\x03 \x01(\x04\x12\x10\n\x08\x66ile_md5\x18\x04 \x01(\x0c\x12\x11\n\tfile_size\x18\x05 \x01(\x04\x12\x11\n\tfile_name\x18\x06 \x01(\x0c\x12\x10\n\x08src_term\x18\x07 \x01(\r\x12\x15\n\rplatform_type\x18\x08 \x01(\r\x12\x0f\n\x07\x62u_type\x18\t \x01(\r\x12\x11\n\tpic_width\x18\n \x01(\r\x12\x12\n\npic_height\x18\x0b \x01(\r\x12\x10\n\x08pic_type\x18\x0c \x01(\r\x12\x11\n\tbuild_ver\x18\r \x01(\x0c\x12\x10\n\x08inner_ip\x18\x0e \x01(\r\x12\x14\n\x0c\x61pp_pic_type\x18\x0f \x01(\r\x12\x14\n\x0coriginal_pic\x18\x10 \x01(\r\x12\x12\n\nfile_index\x18\x11 \x01(\x0c\x12\x0f\n\x07\x64st_uin\x18\x12 \x01(\x04\x12\x12\n\nsrv_upload\x18\x13 \x01(\r\x12\x14\n\x0ctransfer_url\x18\x14 \x01(\x0c\x12\x17\n\x0fqqmeet_guild_id\x18\x15 \x01(\x04\x12\x19\n\x11qqmeet_channel_id\x18\x16 \x01(\x04\"\x87\x03\n\x0bTryUpImgRsp\x12\x0f\n\x07\x66ile_id\x18\x01 \x01(\x04\x12\x0e\n\x06result\x18\x02 \x01(\r\x12\x10\n\x08\x66\x61il_msg\x18\x03 \x01(\x0c\x12\x11\n\tfile_exit\x18\x04 \x01(\x08\x12)\n\x08img_info\x18\x05 \x01(\x0b\x32\x17.im.cs.cmd0x388.ImgInfo\x12\r\n\x05up_ip\x18\x06 \x03(\r\x12\x0f\n\x07up_port\x18\x07 \x03(\r\x12\x0f\n\x07up_ukey\x18\x08 \x01(\x0c\x12\x0e\n\x06\x66ileid\x18\t \x01(\x04\x12\x11\n\tup_offset\x18\n \x01(\x04\x12\x12\n\nblock_size\x18\x0b \x01(\x04\x12\x14\n\x0cnew_big_chan\x18\x0c \x01(\x08\x12(\n\x06up_ip6\x18\x1a \x03(\x0b\x32\x18.im.cs.cmd0x388.IPv6Info\x12\x12\n\nclient_ip6\x18\x1b \x01(\x0c\x12\x16\n\x0e\x64ownload_index\x18\x1c \x01(\x0c\x12\x33\n\ninfo4_busi\x18\xe9\x07 \x01(\x0b\x32\x1e.im.cs.cmd0x388.TryUpInfo4Busi\"\x82\x01\n\x0eTryUpInfo4Busi\x12\x13\n\x0b\x64own_domain\x18\x01 \x01(\x0c\x12\x16\n\x0ethumb_down_url\x18\x02 \x01(\x0c\x12\x19\n\x11original_down_url\x18\x03 \x01(\x0c\x12\x14\n\x0c\x62ig_down_url\x18\x04 \x01(\x0c\x12\x12\n\nfile_resid\x18\x05 \x01(\x0c\"\xb7\x02\n\x0bTryUpPttReq\x12\x12\n\ngroup_code\x18\x01 \x01(\x04\x12\x0f\n\x07src_uin\x18\x02 \x01(\x04\x12\x0f\n\x07\x66ile_id\x18\x03 \x01(\x04\x12\x10\n\x08\x66ile_md5\x18\x04 \x01(\x0c\x12\x11\n\tfile_size\x18\x05 \x01(\x04\x12\x11\n\tfile_name\x18\x06 \x01(\x0c\x12\x10\n\x08src_term\x18\x07 \x01(\r\x12\x15\n\rplatform_type\x18\x08 \x01(\r\x12\x0f\n\x07\x62u_type\x18\t \x01(\r\x12\x11\n\tbuild_ver\x18\n \x01(\x0c\x12\x10\n\x08inner_ip\x18\x0b \x01(\r\x12\x14\n\x0cvoice_length\x18\x0c \x01(\r\x12\x13\n\x0bnew_up_chan\x18\r \x01(\x08\x12\r\n\x05\x63odec\x18\x0e \x01(\r\x12\x12\n\nvoice_type\x18\x0f \x01(\r\x12\r\n\x05\x62u_id\x18\x10 \x01(\r\"\xa1\x02\n\x0bTryUpPttRsp\x12\x0f\n\x07\x66ile_id\x18\x01 \x01(\x04\x12\x0e\n\x06result\x18\x02 \x01(\r\x12\x10\n\x08\x66\x61il_msg\x18\x03 \x01(\x0c\x12\x11\n\tfile_exit\x18\x04 \x01(\x08\x12\r\n\x05up_ip\x18\x05 \x03(\r\x12\x0f\n\x07up_port\x18\x06 \x03(\r\x12\x0f\n\x07up_ukey\x18\x07 \x01(\x0c\x12\x0e\n\x06\x66ileid\x18\x08 \x01(\x04\x12\x11\n\tup_offset\x18\t \x01(\x04\x12\x12\n\nblock_size\x18\n \x01(\x04\x12\x10\n\x08\x66ile_key\x18\x0b \x01(\x0c\x12\x14\n\x0c\x63hannel_type\x18\x0c \x01(\r\x12(\n\x06up_ip6\x18\x1a \x03(\x0b\x32\x18.im.cs.cmd0x388.IPv6Info\x12\x12\n\nclient_ip6\x18\x1b \x01(\x0c')



_DELIMGREQ = DESCRIPTOR.message_types_by_name['DelImgReq']
_DELIMGRSP = DESCRIPTOR.message_types_by_name['DelImgRsp']
_EXPROAMEXTENDINFO = DESCRIPTOR.message_types_by_name['ExpRoamExtendInfo']
_EXPROAMPICINFO = DESCRIPTOR.message_types_by_name['ExpRoamPicInfo']
_EXTENSIONCOMMPICTRYUP = DESCRIPTOR.message_types_by_name['ExtensionCommPicTryUp']
_EXTENSIONEXPROAMTRYUP = DESCRIPTOR.message_types_by_name['ExtensionExpRoamTryUp']
_GETIMGURLREQ = DESCRIPTOR.message_types_by_name['GetImgUrlReq']
_GETIMGURLRSP = DESCRIPTOR.message_types_by_name['GetImgUrlRsp']
_GETPTTURLREQ = DESCRIPTOR.message_types_by_name['GetPttUrlReq']
_GETPTTURLRSP = DESCRIPTOR.message_types_by_name['GetPttUrlRsp']
_IPV6INFO = DESCRIPTOR.message_types_by_name['IPv6Info']
_IMGINFO = DESCRIPTOR.message_types_by_name['ImgInfo']
_PICSIZE = DESCRIPTOR.message_types_by_name['PicSize']
_REQBODY = DESCRIPTOR.message_types_by_name['ReqBody']
_RSPBODY = DESCRIPTOR.message_types_by_name['RspBody']
_TRYUPIMGREQ = DESCRIPTOR.message_types_by_name['TryUpImgReq']
_TRYUPIMGRSP = DESCRIPTOR.message_types_by_name['TryUpImgRsp']
_TRYUPINFO4BUSI = DESCRIPTOR.message_types_by_name['TryUpInfo4Busi']
_TRYUPPTTREQ = DESCRIPTOR.message_types_by_name['TryUpPttReq']
_TRYUPPTTRSP = DESCRIPTOR.message_types_by_name['TryUpPttRsp']
DelImgReq = _reflection.GeneratedProtocolMessageType('DelImgReq', (_message.Message,), {
  'DESCRIPTOR' : _DELIMGREQ,
  '__module__' : 'cai.pb.im.cs.cmd0x388.cmd0x388_pb2'
  # @@protoc_insertion_point(class_scope:im.cs.cmd0x388.DelImgReq)
  })
_sym_db.RegisterMessage(DelImgReq)

DelImgRsp = _reflection.GeneratedProtocolMessageType('DelImgRsp', (_message.Message,), {
  'DESCRIPTOR' : _DELIMGRSP,
  '__module__' : 'cai.pb.im.cs.cmd0x388.cmd0x388_pb2'
  # @@protoc_insertion_point(class_scope:im.cs.cmd0x388.DelImgRsp)
  })
_sym_db.RegisterMessage(DelImgRsp)

ExpRoamExtendInfo = _reflection.GeneratedProtocolMessageType('ExpRoamExtendInfo', (_message.Message,), {
  'DESCRIPTOR' : _EXPROAMEXTENDINFO,
  '__module__' : 'cai.pb.im.cs.cmd0x388.cmd0x388_pb2'
  # @@protoc_insertion_point(class_scope:im.cs.cmd0x388.ExpRoamExtendInfo)
  })
_sym_db.RegisterMessage(ExpRoamExtendInfo)

ExpRoamPicInfo = _reflection.GeneratedProtocolMessageType('ExpRoamPicInfo', (_message.Message,), {
  'DESCRIPTOR' : _EXPROAMPICINFO,
  '__module__' : 'cai.pb.im.cs.cmd0x388.cmd0x388_pb2'
  # @@protoc_insertion_point(class_scope:im.cs.cmd0x388.ExpRoamPicInfo)
  })
_sym_db.RegisterMessage(ExpRoamPicInfo)

ExtensionCommPicTryUp = _reflection.GeneratedProtocolMessageType('ExtensionCommPicTryUp', (_message.Message,), {
  'DESCRIPTOR' : _EXTENSIONCOMMPICTRYUP,
  '__module__' : 'cai.pb.im.cs.cmd0x388.cmd0x388_pb2'
  # @@protoc_insertion_point(class_scope:im.cs.cmd0x388.ExtensionCommPicTryUp)
  })
_sym_db.RegisterMessage(ExtensionCommPicTryUp)

ExtensionExpRoamTryUp = _reflection.GeneratedProtocolMessageType('ExtensionExpRoamTryUp', (_message.Message,), {
  'DESCRIPTOR' : _EXTENSIONEXPROAMTRYUP,
  '__module__' : 'cai.pb.im.cs.cmd0x388.cmd0x388_pb2'
  # @@protoc_insertion_point(class_scope:im.cs.cmd0x388.ExtensionExpRoamTryUp)
  })
_sym_db.RegisterMessage(ExtensionExpRoamTryUp)

GetImgUrlReq = _reflection.GeneratedProtocolMessageType('GetImgUrlReq', (_message.Message,), {
  'DESCRIPTOR' : _GETIMGURLREQ,
  '__module__' : 'cai.pb.im.cs.cmd0x388.cmd0x388_pb2'
  # @@protoc_insertion_point(class_scope:im.cs.cmd0x388.GetImgUrlReq)
  })
_sym_db.RegisterMessage(GetImgUrlReq)

GetImgUrlRsp = _reflection.GeneratedProtocolMessageType('GetImgUrlRsp', (_message.Message,), {
  'DESCRIPTOR' : _GETIMGURLRSP,
  '__module__' : 'cai.pb.im.cs.cmd0x388.cmd0x388_pb2'
  # @@protoc_insertion_point(class_scope:im.cs.cmd0x388.GetImgUrlRsp)
  })
_sym_db.RegisterMessage(GetImgUrlRsp)

GetPttUrlReq = _reflection.GeneratedProtocolMessageType('GetPttUrlReq', (_message.Message,), {
  'DESCRIPTOR' : _GETPTTURLREQ,
  '__module__' : 'cai.pb.im.cs.cmd0x388.cmd0x388_pb2'
  # @@protoc_insertion_point(class_scope:im.cs.cmd0x388.GetPttUrlReq)
  })
_sym_db.RegisterMessage(GetPttUrlReq)

GetPttUrlRsp = _reflection.GeneratedProtocolMessageType('GetPttUrlRsp', (_message.Message,), {
  'DESCRIPTOR' : _GETPTTURLRSP,
  '__module__' : 'cai.pb.im.cs.cmd0x388.cmd0x388_pb2'
  # @@protoc_insertion_point(class_scope:im.cs.cmd0x388.GetPttUrlRsp)
  })
_sym_db.RegisterMessage(GetPttUrlRsp)

IPv6Info = _reflection.GeneratedProtocolMessageType('IPv6Info', (_message.Message,), {
  'DESCRIPTOR' : _IPV6INFO,
  '__module__' : 'cai.pb.im.cs.cmd0x388.cmd0x388_pb2'
  # @@protoc_insertion_point(class_scope:im.cs.cmd0x388.IPv6Info)
  })
_sym_db.RegisterMessage(IPv6Info)

ImgInfo = _reflection.GeneratedProtocolMessageType('ImgInfo', (_message.Message,), {
  'DESCRIPTOR' : _IMGINFO,
  '__module__' : 'cai.pb.im.cs.cmd0x388.cmd0x388_pb2'
  # @@protoc_insertion_point(class_scope:im.cs.cmd0x388.ImgInfo)
  })
_sym_db.RegisterMessage(ImgInfo)

PicSize = _reflection.GeneratedProtocolMessageType('PicSize', (_message.Message,), {
  'DESCRIPTOR' : _PICSIZE,
  '__module__' : 'cai.pb.im.cs.cmd0x388.cmd0x388_pb2'
  # @@protoc_insertion_point(class_scope:im.cs.cmd0x388.PicSize)
  })
_sym_db.RegisterMessage(PicSize)

ReqBody = _reflection.GeneratedProtocolMessageType('ReqBody', (_message.Message,), {
  'DESCRIPTOR' : _REQBODY,
  '__module__' : 'cai.pb.im.cs.cmd0x388.cmd0x388_pb2'
  # @@protoc_insertion_point(class_scope:im.cs.cmd0x388.ReqBody)
  })
_sym_db.RegisterMessage(ReqBody)

RspBody = _reflection.GeneratedProtocolMessageType('RspBody', (_message.Message,), {
  'DESCRIPTOR' : _RSPBODY,
  '__module__' : 'cai.pb.im.cs.cmd0x388.cmd0x388_pb2'
  # @@protoc_insertion_point(class_scope:im.cs.cmd0x388.RspBody)
  })
_sym_db.RegisterMessage(RspBody)

TryUpImgReq = _reflection.GeneratedProtocolMessageType('TryUpImgReq', (_message.Message,), {
  'DESCRIPTOR' : _TRYUPIMGREQ,
  '__module__' : 'cai.pb.im.cs.cmd0x388.cmd0x388_pb2'
  # @@protoc_insertion_point(class_scope:im.cs.cmd0x388.TryUpImgReq)
  })
_sym_db.RegisterMessage(TryUpImgReq)

TryUpImgRsp = _reflection.GeneratedProtocolMessageType('TryUpImgRsp', (_message.Message,), {
  'DESCRIPTOR' : _TRYUPIMGRSP,
  '__module__' : 'cai.pb.im.cs.cmd0x388.cmd0x388_pb2'
  # @@protoc_insertion_point(class_scope:im.cs.cmd0x388.TryUpImgRsp)
  })
_sym_db.RegisterMessage(TryUpImgRsp)

TryUpInfo4Busi = _reflection.GeneratedProtocolMessageType('TryUpInfo4Busi', (_message.Message,), {
  'DESCRIPTOR' : _TRYUPINFO4BUSI,
  '__module__' : 'cai.pb.im.cs.cmd0x388.cmd0x388_pb2'
  # @@protoc_insertion_point(class_scope:im.cs.cmd0x388.TryUpInfo4Busi)
  })
_sym_db.RegisterMessage(TryUpInfo4Busi)

TryUpPttReq = _reflection.GeneratedProtocolMessageType('TryUpPttReq', (_message.Message,), {
  'DESCRIPTOR' : _TRYUPPTTREQ,
  '__module__' : 'cai.pb.im.cs.cmd0x388.cmd0x388_pb2'
  # @@protoc_insertion_point(class_scope:im.cs.cmd0x388.TryUpPttReq)
  })
_sym_db.RegisterMessage(TryUpPttReq)

TryUpPttRsp = _reflection.GeneratedProtocolMessageType('TryUpPttRsp', (_message.Message,), {
  'DESCRIPTOR' : _TRYUPPTTRSP,
  '__module__' : 'cai.pb.im.cs.cmd0x388.cmd0x388_pb2'
  # @@protoc_insertion_point(class_scope:im.cs.cmd0x388.TryUpPttRsp)
  })
_sym_db.RegisterMessage(TryUpPttRsp)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _DELIMGREQ._serialized_start=57
  _DELIMGREQ._serialized_end=242
  _DELIMGRSP._serialized_start=244
  _DELIMGRSP._serialized_end=309
  _EXPROAMEXTENDINFO._serialized_start=311
  _EXPROAMEXTENDINFO._serialized_end=345
  _EXPROAMPICINFO._serialized_start=347
  _EXPROAMPICINFO._serialized_end=414
  _EXTENSIONCOMMPICTRYUP._serialized_start=416
  _EXTENSIONCOMMPICTRYUP._serialized_end=456
  _EXTENSIONEXPROAMTRYUP._serialized_start=458
  _EXTENSIONEXPROAMTRYUP._serialized_end=539
  _GETIMGURLREQ._serialized_start=542
  _GETIMGURLREQ._serialized_end=1027
  _GETIMGURLRSP._serialized_start=1030
  _GETIMGURLRSP._serialized_end=1544
  _GETPTTURLREQ._serialized_start=1547
  _GETPTTURLREQ._serialized_end=1840
  _GETPTTURLRSP._serialized_start=1843
  _GETPTTURLRSP._serialized_end=2160
  _IPV6INFO._serialized_start=2162
  _IPV6INFO._serialized_end=2199
  _IMGINFO._serialized_start=2201
  _IMGINFO._serialized_end=2307
  _PICSIZE._serialized_start=2309
  _PICSIZE._serialized_end=2365
  _REQBODY._serialized_start=2368
  _REQBODY._serialized_end=2711
  _RSPBODY._serialized_start=2714
  _RSPBODY._serialized_end=3018
  _TRYUPIMGREQ._serialized_start=3021
  _TRYUPIMGREQ._serialized_end=3471
  _TRYUPIMGRSP._serialized_start=3474
  _TRYUPIMGRSP._serialized_end=3865
  _TRYUPINFO4BUSI._serialized_start=3868
  _TRYUPINFO4BUSI._serialized_end=3998
  _TRYUPPTTREQ._serialized_start=4001
  _TRYUPPTTREQ._serialized_end=4312
  _TRYUPPTTRSP._serialized_start=4315
  _TRYUPPTTRSP._serialized_end=4604
# @@protoc_insertion_point(module_scope)
