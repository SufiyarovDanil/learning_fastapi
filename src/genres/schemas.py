from pydantic import BaseModel
from typing import Optional


class GenreCreate(BaseModel):
    name: str


class GenreUpdate(BaseModel):
    id: int
    name: Optional[str]
