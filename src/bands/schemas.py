from pydantic import BaseModel
from pydantic.types import date
from typing import Optional


class BandCreate(BaseModel):
    name: str
    created_at: Optional[date]


class BandUpdate(BaseModel):
    id: int
    name: Optional[str]
    created_at: Optional[date]
