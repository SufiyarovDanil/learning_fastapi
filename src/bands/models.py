from sqlalchemy import SmallInteger, BigInteger, VARCHAR, Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import BaseModel
import albums.models


class BandModel(BaseModel):
    __tablename__ = 'band'

    id: Mapped[BigInteger] = mapped_column(
        BigInteger,
        primary_key=True,
        autoincrement=True,
        name='pk_id'
    )
    name: Mapped[VARCHAR] = mapped_column(
        VARCHAR(64),
        nullable=False,
        name='name'
    )
    created_at: Mapped[Date] = mapped_column(
        Date,
        nullable=True,
        name='created_at'
    )

    albums: Mapped[list['albums.models.AlbumModel']] = relationship(back_populates='band')


class GenreModel(BaseModel):
    __tablename__ = 'genre'

    id: Mapped[BigInteger] = mapped_column(
        BigInteger,
        primary_key=True,
        autoincrement=True,
        name='pk_id'
    )
    name: Mapped[VARCHAR] = mapped_column(
        VARCHAR(32),
        nullable=False,
        unique=True,
        name='name'
    )


class AlbumGenreModel(BaseModel):
    __tablename__ = 'album_genre'

    album_id: Mapped[BigInteger] = mapped_column(
        BigInteger,
        ForeignKey('album.pk_id', ondelete='CASCADE'),
        primary_key=True,
        nullable=False,
        name='fk_album_id'
    )
    genre_id: Mapped[BigInteger] = mapped_column(
        BigInteger,
        ForeignKey('genre.pk_id', ondelete='CASCADE'),
        primary_key=True,
        nullable=False,
        name='fk_genre_id'
    )
