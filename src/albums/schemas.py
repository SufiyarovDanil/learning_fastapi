from pydantic import BaseModel
from datetime import date
from typing import Optional


class AlbumCreate(BaseModel):
    name: str
    published_at: Optional[date]
    band_id: int


class AlbumUpdate(BaseModel):
    id: int
    name: Optional[str]
    published_at: Optional[date]
    band_id: Optional[int]
