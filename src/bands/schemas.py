from pydantic import BaseModel
from pydantic.types import date
from typing import Optional


class Band(BaseModel):
    name: str
    created_at: Optional[date]
