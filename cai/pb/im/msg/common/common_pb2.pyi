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

from google.protobuf.message import (
    Message,
)

from typing import (
    Optional,
    Text,
)

from typing_extensions import (
    Literal,
)


DESCRIPTOR: FileDescriptor

class GroupInfo(Message):
    """tencent/im/msg/im_common.java

    """
    DESCRIPTOR: Descriptor
    GROUP_ID_FIELD_NUMBER: int
    GROUP_TYPE_FIELD_NUMBER: int
    group_id: int
    group_type: int
    def __init__(self,
        *,
        group_id: Optional[int] = ...,
        group_type: Optional[int] = ...,
        ) -> None: ...
    def HasField(self, field_name: Literal["group_id",b"group_id","group_type",b"group_type"]) -> bool: ...
    def ClearField(self, field_name: Literal["group_id",b"group_id","group_type",b"group_type"]) -> None: ...

class Signature(Message):
    DESCRIPTOR: Descriptor
    KEY_TYPE_FIELD_NUMBER: int
    SESSION_APP_ID_FIELD_NUMBER: int
    SESSION_KEY_FIELD_NUMBER: int
    key_type: int
    session_app_id: int
    session_key: bytes
    def __init__(self,
        *,
        key_type: Optional[int] = ...,
        session_app_id: Optional[int] = ...,
        session_key: Optional[bytes] = ...,
        ) -> None: ...
    def HasField(self, field_name: Literal["key_type",b"key_type","session_app_id",b"session_app_id","session_key",b"session_key"]) -> bool: ...
    def ClearField(self, field_name: Literal["key_type",b"key_type","session_app_id",b"session_app_id","session_key",b"session_key"]) -> None: ...

class Token(Message):
    DESCRIPTOR: Descriptor
    BUF_FIELD_NUMBER: int
    C2C_TYPE_FIELD_NUMBER: int
    SERVICE_TYPE_FIELD_NUMBER: int
    buf: bytes
    c2c_type: int
    service_type: int
    def __init__(self,
        *,
        buf: Optional[bytes] = ...,
        c2c_type: Optional[int] = ...,
        service_type: Optional[int] = ...,
        ) -> None: ...
    def HasField(self, field_name: Literal["buf",b"buf","c2c_type",b"c2c_type","service_type",b"service_type"]) -> bool: ...
    def ClearField(self, field_name: Literal["buf",b"buf","c2c_type",b"c2c_type","service_type",b"service_type"]) -> None: ...

class User(Message):
    DESCRIPTOR: Descriptor
    UIN_FIELD_NUMBER: int
    APP_ID_FIELD_NUMBER: int
    INSTANCE_ID_FIELD_NUMBER: int
    APP_TYPE_FIELD_NUMBER: int
    CLIENT_IP_FIELD_NUMBER: int
    VERSION_FIELD_NUMBER: int
    PHONE_NUMBER_FIELD_NUMBER: int
    PLATFORM_ID_FIELD_NUMBER: int
    LANGUAGE_FIELD_NUMBER: int
    EQUIP_KEY_FIELD_NUMBER: int
    uin: int
    app_id: int
    instance_id: int
    app_type: int
    client_ip: int
    version: int
    phone_number: Text
    platform_id: int
    language: int
    equip_key: bytes
    def __init__(self,
        *,
        uin: Optional[int] = ...,
        app_id: Optional[int] = ...,
        instance_id: Optional[int] = ...,
        app_type: Optional[int] = ...,
        client_ip: Optional[int] = ...,
        version: Optional[int] = ...,
        phone_number: Optional[Text] = ...,
        platform_id: Optional[int] = ...,
        language: Optional[int] = ...,
        equip_key: Optional[bytes] = ...,
        ) -> None: ...
    def HasField(self, field_name: Literal["app_id",b"app_id","app_type",b"app_type","client_ip",b"client_ip","equip_key",b"equip_key","instance_id",b"instance_id","language",b"language","phone_number",b"phone_number","platform_id",b"platform_id","uin",b"uin","version",b"version"]) -> bool: ...
    def ClearField(self, field_name: Literal["app_id",b"app_id","app_type",b"app_type","client_ip",b"client_ip","equip_key",b"equip_key","instance_id",b"instance_id","language",b"language","phone_number",b"phone_number","platform_id",b"platform_id","uin",b"uin","version",b"version"]) -> None: ...
