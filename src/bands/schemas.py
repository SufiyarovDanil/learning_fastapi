from pydantic import BaseModel
from pydantic.types import date
from typing import Optional


class Band(BaseModel):
    name: str
    created_at: Optional[date]


class Album(BaseModel):
    name: str
    published_at: date
    band: Band


class Track(BaseModel):
    name: str
    length: int # in seconds
    album: Album


class Genre(BaseModel):
    name: str


class AlbumGenre(BaseModel):
    album: Album
    genre: Genre
