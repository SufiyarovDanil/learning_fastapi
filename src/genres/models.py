from sqlalchemy import BigInteger, VARCHAR
from sqlalchemy.orm import Mapped, mapped_column
from database import BaseModel


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
