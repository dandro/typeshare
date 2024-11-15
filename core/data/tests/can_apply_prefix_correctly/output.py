"""
 Generated by typeshare 1.12.0
"""
from __future__ import annotations

from pydantic import BaseModel
from typing import Dict, List, Literal, Union


class ItemDetailsFieldValue(BaseModel):
    hello: str

class AdvancedColorsString(BaseModel):
    AdvancedColorsTypes: Literal["String"] = "String"
    c: str

class AdvancedColorsNumber(BaseModel):
    AdvancedColorsTypes: Literal["Number"] = "Number"
    c: int

class AdvancedColorsNumberArray(BaseModel):
    AdvancedColorsTypes: Literal["NumberArray"] = "NumberArray"
    c: List[int]

class AdvancedColorsReallyCoolType(BaseModel):
    AdvancedColorsTypes: Literal["ReallyCoolType"] = "ReallyCoolType"
    c: ItemDetailsFieldValue

class AdvancedColorsArrayReallyCoolType(BaseModel):
    AdvancedColorsTypes: Literal["ArrayReallyCoolType"] = "ArrayReallyCoolType"
    c: List[ItemDetailsFieldValue]

class AdvancedColorsDictionaryReallyCoolType(BaseModel):
    AdvancedColorsTypes: Literal["DictionaryReallyCoolType"] = "DictionaryReallyCoolType"
    c: Dict[str, ItemDetailsFieldValue]

AdvancedColors = Union[AdvancedColorsString, AdvancedColorsNumber, AdvancedColorsNumberArray, AdvancedColorsReallyCoolType, AdvancedColorsArrayReallyCoolType, AdvancedColorsDictionaryReallyCoolType]
