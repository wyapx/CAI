from typing import Optional, List, TYPE_CHECKING
from dataclasses import dataclass, field

from cai.pb.msf.msg.comm import Msg
from .base import Event, BotEvent

if TYPE_CHECKING:
    from ..message_service.models import Element
    from ..status_service.jce import InstanceInfo


@dataclass
class NudgeEvent(Event):
    sender: int
    target: int
    action: str
    suffix: Optional[str]
    group: Optional[int] = None

    @property
    def type(self) -> str:
        return "NudgeEvent"


@dataclass
class BotOnlineEvent(BotEvent):
    qq: int


@dataclass
class BotOfflineEvent(BotEvent):
    qq: int
    reconnect: bool


@dataclass
class OtherClientChangedEvent(BotEvent):
    is_login: bool
    app_id: int
    client_type: int
    platform: int
    title: str
    description: str
    instance_list: List["InstanceInfo"]


@dataclass
class PrivateMessage(Event):
    seq: int
    time: int
    auto_reply: bool
    from_uin: int
    from_nick: str
    to_uin: int
    message: List["Element"]
    _msg: Msg = field(repr=False)

    @property
    def type(self) -> str:
        return "private_message"


@dataclass
class GroupMessage(Event):
    seq: int
    rand: int
    time: int
    group_id: int
    group_name: str
    group_level: int
    from_uin: int
    from_group_card: str
    message: List["Element"]
    _msg: Msg = field(repr=False)

    @property
    def type(self) -> str:
        return "group_message"


@dataclass
class TempMessage(Event):
    seq: int
    rand: int
    time: int
    group_id: int
    from_uin: int
    from_group_card: str
    message: List["Element"]
    _msg: Msg = field(repr=False)

    @property
    def type(self) -> str:
        return "temp_message"
