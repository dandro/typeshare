"""
 Generated by typeshare 1.12.0
"""
from __future__ import annotations

from pydantic import BaseModel
from pydantic.networks import AnyUrl


class Foo(BaseModel):
    url: AnyUrl

