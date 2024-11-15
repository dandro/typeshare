"""
 Generated by typeshare 1.12.0
"""
from __future__ import annotations

from enum import Enum
from pydantic import BaseModel
from typing import Literal, Union


class MoreOptionsExactlyInner(BaseModel):
    """
    Generated type representing the anonymous struct variant `Exactly` of the `MoreOptions` Rust enum
    """
    config: str


class MoreOptionsBuiltInner(BaseModel):
    """
    Generated type representing the anonymous struct variant `Built` of the `MoreOptions` Rust enum
    """
    top: MoreOptions


class MoreOptionsTypes(str, Enum):
    NEWS = "news"
    EXACTLY = "exactly"
    BUILT = "built"

class MoreOptionsNews(BaseModel):
    MoreOptionsTypes: Literal["news"] = "news"
    content: bool

class MoreOptionsExactly(BaseModel):
    MoreOptionsTypes: Literal["exactly"] = "exactly"
    content: MoreOptionsExactlyInner

class MoreOptionsBuilt(BaseModel):
    MoreOptionsTypes: Literal["built"] = "built"
    content: MoreOptionsBuiltInner

MoreOptions = Union[MoreOptionsNews, MoreOptionsExactly, MoreOptionsBuilt]
class OptionsTypes(str, Enum):
    RED = "red"
    BANANA = "banana"
    VERMONT = "vermont"

class OptionsRed(BaseModel):
    OptionsTypes: Literal["red"] = "red"
    content: bool

class OptionsBanana(BaseModel):
    OptionsTypes: Literal["banana"] = "banana"
    content: str

class OptionsVermont(BaseModel):
    OptionsTypes: Literal["vermont"] = "vermont"
    content: Options

Options = Union[OptionsRed, OptionsBanana, OptionsVermont]
