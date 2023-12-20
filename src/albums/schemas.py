from pydantic import BaseModel
from datetime import date
from typing import Optional


class Album(BaseModel):
    name: str
    published_at: Optional[date]
    band_id: int
