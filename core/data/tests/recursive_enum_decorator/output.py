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
    type: Literal[MoreOptionsTypes.NEWS] = MoreOptionsTypes.NEWS
    content: bool

class MoreOptionsExactly(BaseModel):
    type: Literal[MoreOptionsTypes.EXACTLY] = MoreOptionsTypes.EXACTLY
    content: MoreOptionsExactlyInner

class MoreOptionsBuilt(BaseModel):
    type: Literal[MoreOptionsTypes.BUILT] = MoreOptionsTypes.BUILT
    content: MoreOptionsBuiltInner

MoreOptions = Union[MoreOptionsNews, MoreOptionsExactly, MoreOptionsBuilt]
class OptionsTypes(str, Enum):
    RED = "red"
    BANANA = "banana"
    VERMONT = "vermont"

class OptionsRed(BaseModel):
    type: Literal[OptionsTypes.RED] = OptionsTypes.RED
    content: bool

class OptionsBanana(BaseModel):
    type: Literal[OptionsTypes.BANANA] = OptionsTypes.BANANA
    content: str

class OptionsVermont(BaseModel):
    type: Literal[OptionsTypes.VERMONT] = OptionsTypes.VERMONT
    content: Options

Options = Union[OptionsRed, OptionsBanana, OptionsVermont]
