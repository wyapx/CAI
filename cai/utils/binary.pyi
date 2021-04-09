"""Binary Tools Stub File.

Type hints in this file needs python>=3.10 or using ``pyright`` or ``pylance``...

:Copyright: Copyright (C) 2021-2021  cscs181
:License: AGPL-3.0 or later. See `LICENSE`_ for detail.

.. _LICENSE:
    https://github.com/cscs181/CAI/blob/master/LICENSE
"""
from typing_extensions import Unpack, TypeVarTuple
from typing import Any, List, Type, Tuple, Union, TypeVar, Generic, Optional, Callable, NewType

P = TypeVar("P", bound="BasePacket")
Ts = TypeVarTuple("Ts")

BOOL = NewType("BOOL", bool)
INT8 = NewType("INT8", int)
UINT8 = NewType("UINT8", int)
INT16 = NewType("INT16", int)
UINT16 = NewType("UINT16", int)
INT32 = NewType("INT32", int)
UINT32 = NewType("UINT32", int)
INT64 = NewType("INT64", int)
UINT64 = NewType("UINT64", int)
FLOAT = NewType("FLOAT", float)
DOUBLE = NewType("DOUBLE", float)
BYTE = NewType("BYTE", bytes)
BYTES = NewType("BYTES", bytes)
STRING = NewType("STRING", str)


class BasePacket(bytearray):

    @classmethod
    def build(cls: Type[P], *data: Union[bytes, "BasePacket"]) -> P:
        ...

    def write(self: P, *data: Union[bytes, "BasePacket"]) -> P:
        ...

    def write_with_length(
        self: P, *data: Union[bytes, "BasePacket"], offset: int = ...
    ) -> P:
        ...

    def unpack(self, format: Union[bytes, str]) -> Tuple[Any, ...]:
        ...

    def unpack_from(self,
                    format: Union[bytes, str],
                    offset: int = ...) -> Tuple[Any, ...]:
        ...

    def read_int8(self, offset: int = ...) -> INT8:
        ...

    def read_uint8(self, offset: int = ...) -> UINT8:
        ...

    def read_int16(self, offset: int = ...) -> INT16:
        ...

    def read_uint16(self, offset: int = ...) -> UINT16:
        ...

    def read_int32(self, offset: int = ...) -> INT32:
        ...

    def read_uint32(self, offset: int = ...) -> UINT32:
        ...

    def read_int64(self, offset: int = ...) -> INT64:
        ...

    def read_uint64(self, offset: int = ...) -> UINT64:
        ...

    def read_byte(self, offset: int = ...) -> BYTE:
        ...

    def read_bytes(self, n: int, offset: int = ...) -> BYTES:
        ...

    def read_string(self, offset: int = ...) -> STRING:
        ...


class Packet(BasePacket, Generic[Unpack[Ts]]):
    _query: str
    _cache: Tuple[Any, ...]
    _filters: List[Callable[[Any], Any]]

    def __init__(
        self,
        *args,
        cache: Optional[Tuple[Any, ...]] = None,
        **kwargs
    ) -> "Packet[()]":
        ...

    def bool(
        self: "Packet[Unpack[Ts]]"
    ) -> "Packet[Unpack[Ts], BOOL]":  # type: ignore
        ...

    def int8(
        self: "Packet[Unpack[Ts]]"
    ) -> "Packet[Unpack[Ts], INT8]":  # type: ignore
        ...

    def uint8(
        self: "Packet[Unpack[Ts]]"
    ) -> "Packet[Unpack[Ts], UINT8]":  # type: ignore
        ...

    def int16(
        self: "Packet[Unpack[Ts]]"
    ) -> "Packet[Unpack[Ts], INT16]":  # type: ignore
        ...

    def uint16(
        self: "Packet[Unpack[Ts]]"
    ) -> "Packet[Unpack[Ts], UINT16]":  # type: ignore
        ...

    def int32(
        self: "Packet[Unpack[Ts]]"
    ) -> "Packet[Unpack[Ts], INT32]":  # type: ignore
        ...

    def uint32(
        self: "Packet[Unpack[Ts]]"
    ) -> "Packet[Unpack[Ts], UINT32]":  # type: ignore
        ...

    def int64(
        self: "Packet[Unpack[Ts]]"
    ) -> "Packet[Unpack[Ts], INT64]":  # type: ignore
        ...

    def uint64(
        self: "Packet[Unpack[Ts]]"
    ) -> "Packet[Unpack[Ts], UINT64]":  # type: ignore
        ...

    def float(
        self: "Packet[Unpack[Ts]]"
    ) -> "Packet[Unpack[Ts], FLOAT]":  # type: ignore
        ...

    def double(
        self: "Packet[Unpack[Ts]]"
    ) -> "Packet[Unpack[Ts], DOUBLE]":  # type: ignore
        ...

    def byte(
        self: "Packet[Unpack[Ts]]"
    ) -> "Packet[Unpack[Ts], BYTE]":  # type: ignore
        ...

    def bytes(
        self: "Packet[Unpack[Ts]]", length: int
    ) -> "Packet[Unpack[Ts], BYTES]":  # type: ignore
        ...

    def string(
        self: "Packet[Unpack[Ts]]",
        head_bytes: int,
        encoding: str = ...
    ) -> "Packet[Unpack[Ts], STRING]":  # type: ignore
        ...

    def offset(self: "Packet[Unpack[Ts]]", offset: int) -> "Packet[Unpack[Ts]]":
        ...

    def _exec_cache(self: "Packet[Unpack[Ts]]") -> "Packet[Unpack[Ts]]":
        ...

    def execute(self: "Packet[Unpack[Ts]]") -> Tuple[Unpack[Ts]]:
        ...