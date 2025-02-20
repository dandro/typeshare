from __future__ import annotations

from enum import Enum
from pydantic import BaseModel
from typing import List, Literal, Union


class ItemDetailsFieldValue(BaseModel):
    """
    Struct comment
    """
    pass
class AdvancedColorsTypes(str, Enum):
    STRING = "String"
    NUMBER = "Number"
    UNSIGNED_NUMBER = "UnsignedNumber"
    NUMBER_ARRAY = "NumberArray"
    REALLY_COOL_TYPE = "ReallyCoolType"

class AdvancedColorsString(BaseModel):
    """
    This is a case comment
    """
    type: Literal[AdvancedColorsTypes.STRING] = AdvancedColorsTypes.STRING
    content: str

class AdvancedColorsNumber(BaseModel):
    type: Literal[AdvancedColorsTypes.NUMBER] = AdvancedColorsTypes.NUMBER
    content: int

class AdvancedColorsUnsignedNumber(BaseModel):
    type: Literal[AdvancedColorsTypes.UNSIGNED_NUMBER] = AdvancedColorsTypes.UNSIGNED_NUMBER
    content: int

class AdvancedColorsNumberArray(BaseModel):
    type: Literal[AdvancedColorsTypes.NUMBER_ARRAY] = AdvancedColorsTypes.NUMBER_ARRAY
    content: List[int]

class AdvancedColorsReallyCoolType(BaseModel):
    """
    Comment on the last element
    """
    type: Literal[AdvancedColorsTypes.REALLY_COOL_TYPE] = AdvancedColorsTypes.REALLY_COOL_TYPE
    content: ItemDetailsFieldValue

# Enum comment
AdvancedColors = Union[AdvancedColorsString, AdvancedColorsNumber, AdvancedColorsUnsignedNumber, AdvancedColorsNumberArray, AdvancedColorsReallyCoolType]
class AdvancedColors2Types(str, Enum):
    STRING = "string"
    NUMBER = "number"
    NUMBER_ARRAY = "number-array"
    REALLY_COOL_TYPE = "really-cool-type"

class AdvancedColors2String(BaseModel):
    """
    This is a case comment
    """
    type: Literal[AdvancedColors2Types.STRING] = AdvancedColors2Types.STRING
    content: str

class AdvancedColors2Number(BaseModel):
    type: Literal[AdvancedColors2Types.NUMBER] = AdvancedColors2Types.NUMBER
    content: int

class AdvancedColors2NumberArray(BaseModel):
    type: Literal[AdvancedColors2Types.NUMBER_ARRAY] = AdvancedColors2Types.NUMBER_ARRAY
    content: List[int]

class AdvancedColors2ReallyCoolType(BaseModel):
    """
    Comment on the last element
    """
    type: Literal[AdvancedColors2Types.REALLY_COOL_TYPE] = AdvancedColors2Types.REALLY_COOL_TYPE
    content: ItemDetailsFieldValue

AdvancedColors2 = Union[AdvancedColors2String, AdvancedColors2Number, AdvancedColors2NumberArray, AdvancedColors2ReallyCoolType]
