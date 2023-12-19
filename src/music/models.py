from sqlalchemy import SmallInteger, BigInteger, VARCHAR, Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import BaseModel


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

    albums: Mapped[list['AlbumModel']] = relationship(back_populates='band')


class AlbumModel(BaseModel):
    __tablename__ = 'album'

    id: Mapped[BigInteger] = mapped_column(
        BigInteger,
        primary_key=True,
        autoincrement=True,
        name='pk_id'
    )
    name: Mapped[VARCHAR(150)] = mapped_column(
        VARCHAR(150),
        nullable=False,
        name='name'
    )
    published_at: Mapped[Date] = mapped_column(
        Date,
        nullable=True,
        name='published_at'
    )
    band_id: Mapped[BigInteger] = mapped_column(
        BigInteger,
        ForeignKey('band.pk_id', ondelete='SET NULL'),
        nullable=False,
        name='fk_band_id'
    )

    band: Mapped['BandModel'] = relationship(back_populates='albums')
    tracks: Mapped[list['TrackModel']] = relationship(back_populates='album')
    genres: Mapped[list['GenreModel']] = relationship(secondary='album_genre')


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


class TrackModel(BaseModel):
    __tablename__ = 'track'

    id: Mapped[BigInteger] = mapped_column(
        BigInteger,
        primary_key=True,
        autoincrement=True,
        name='pk_id'
    )
    name: Mapped[VARCHAR] = mapped_column(
        VARCHAR(128),
        nullable=False,
        name='name'
    )
    length: Mapped[SmallInteger] = mapped_column(
        SmallInteger,
        nullable=False,
        name='length'
    )
    album_id: Mapped[BigInteger] = mapped_column(
        BigInteger,
        ForeignKey('album.pk_id', ondelete='CASCADE'),
        nullable=False,
        name='fk_album_id'
    )

    album: Mapped['AlbumModel'] = relationship(back_populates='tracks')
