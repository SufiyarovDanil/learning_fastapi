from pydantic import BaseModel
from datetime import date
from typing import Optional


class BandCreate(BaseModel):
    name: str
    created_at: Optional[date]


class BandUpdate(BaseModel):
    id: int
    name: Optional[str]
    created_at: Optional[date]
