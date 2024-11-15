"""
 Generated by typeshare 1.12.0
"""
from __future__ import annotations

from enum import Enum
from pydantic import BaseModel
from typing import Literal, Union


class AddressDetails(BaseModel):
    pass

class AddressTypes(str, Enum):
    FIXED_ADDRESS = "FixedAddress"
    NO_FIXED_ADDRESS = "NoFixedAddress"

class AddressFixedAddress(BaseModel):
    AddressTypes: Literal["FixedAddress"] = "FixedAddress"
    content: AddressDetails

class AddressNoFixedAddress(BaseModel):
    AddressTypes: Literal["NoFixedAddress"] = "NoFixedAddress"

Address = Union[AddressFixedAddress, AddressNoFixedAddress]
