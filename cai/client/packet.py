"""Client packets.

This module is used to packet data into outgoing format.

:Copyright: Copyright (C) 2021-2021  yanyongyu
:License: AGPL-3.0 or later. See `LICENSE`_ for detail.

.. _LICENSE:
    https://github.com/yanyongyu/CAI/blob/master/LICENSE
"""
import struct
from typing import Union, Optional

from rtea import qqtea_encrypt, qqtea_decrypt

from cai.utils.binary import Packet


class CSsoBodyPacket(Packet):
    """CSSOBody Packet.

    Note:
        Source:
            com.tencent.qphone.base.util.CodecWarpper

            /data/data/com.tencent.mobileqq/lib/libcodecwrapperV2.so

            `CSSOReqHead::serialize_verFull`
    """

    @classmethod
    def build(
        cls,
        seq: int,
        sub_app_id: int,
        command_name: str,
        imei: str,
        session_id: bytes,
        ksid: bytes,
        body: Union[bytes, Packet],
        extra_data: Union[bytes, Packet] = b"",
        unknown_bytes: bytes = bytes(
            [
                0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                0x01, 0x00
            ]
        )
    ) -> "CSsoBodyPacket":
        """Build CSSOBody head and append body.

        Note:
            Source: `CSSOReqHead::serialize_verFull`
        """
        extra = extra_data and (len(extra_data) != 4)
        packet = cls().write_with_length(
            struct.pack(">III", seq, sub_app_id, sub_app_id),
            unknown_bytes,
            struct.pack(">I", 4) if not extra else b"",
            struct.pack(
                ">I",
                len(extra_data) + 4,
            ) if extra else b"",
            extra_data if extra else b"",
            struct.pack(">I",
                        len(command_name) + 4),
            command_name.encode(),
            struct.pack(">I",
                        len(session_id) + 4),
            session_id,
            struct.pack(">I",
                        len(imei) + 4),
            imei.encode(),
            struct.pack(">IH", 4,
                        len(ksid) + 2),
            ksid,
            struct.pack(">I", 4),
            offset=4
        )
        return packet.write_with_length(body, offset=4)


class CSsoDataPacket(Packet):
    """CSSOData Packet.

    `KSSOVersion`: `Full: 0xA` `Simple: 0xB`.

    Note:
        Source:
            com.tencent.qphone.base.util.CodecWarpper

            /data/data/com.tencent.mobileqq/lib/libcodecwrapperV2.so

            `CSSOData::serialize`
    """

    @classmethod
    def build(
        cls,
        uin: int,
        body_type: int,
        body: Union[bytes, Packet],
        ksso_version: int = 0xA,
        key: Optional[bytes] = None,
        extra_data: bytes = b""
    ) -> "CSsoDataPacket":
        """Build CSSOPacket head and append body.

        Packet body was encrypted in `CSSOData::serialize`.

        Note:
            Source: `CSSOHead::serialize_verFull`
        """
        return cls().write_with_length(
            Packet.build(
                struct.pack(">IB", ksso_version, body_type),
                struct.pack(">I",
                            len(extra_data) + 4), extra_data, bytes([0]),
                struct.pack(">I",
                            len(str(uin)) + 4),
                str(uin).encode(),
                qqtea_encrypt(body, key) if key else body
            ),
            offset=4
        )


class UniPacket(Packet):

    @classmethod
    def build(
        cls,
        uin: int,
        seq: int,
        command_name: str,
        session_id: bytes,
        encrypt_type: int,
        body: Union[bytes, Packet],
        key: bytes,
        extra_data: bytes = b""
    ) -> "UniPacket":
        data = Packet().write_with_length(
            struct.pack(">I",
                        len(command_name) + 4),
            command_name.encode(),
            struct.pack(">I",
                        len(session_id) + 4),
            session_id,
            struct.pack(">I",
                        len(extra_data) + 4),
            extra_data,
            offset=4
        )
        data.write_with_length(body, offset=4)
        return cls().write_with_length(
            struct.pack(">IBIB", 0xB, encrypt_type, seq, 0),
            struct.pack(">I",
                        len(str(uin)) + 4),
            str(uin).encode(), qqtea_encrypt(data, key)
        )


class IncomingPacket:

    @classmethod
    def parse(cls, data: bytes, d2key: bytes) -> "IncomingPacket":
        flag1, flag2, flag3 = struct.unpack_from(">IBB", data)
