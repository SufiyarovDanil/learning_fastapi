from sqlalchemy import SmallInteger, BigInteger, VARCHAR, Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import BaseModel


class AlbumModel(BaseModel):
    __tablename__ = 'album'

    id: Mapped[BigInteger] = mapped_column(
        BigInteger,
        primary_key=True,
        autoincrement=True,
        name='pk_id'
    )
    name: Mapped[VARCHAR] = mapped_column(
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

    band = relationship('BandModel', back_populates='albums')
    tracks = relationship('TrackModel', back_populates='album')
    genres = relationship('GenreModel', secondary='album_genre')


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

    album = relationship('AlbumModel', back_populates='tracks')
