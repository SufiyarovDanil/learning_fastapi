"""init

Revision ID: b5cd8e5d4ac5
Revises: 
Create Date: 2023-12-20 20:48:13.336213

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b5cd8e5d4ac5'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('band',
    sa.Column('pk_id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=64), nullable=False),
    sa.Column('created_at', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('pk_id')
    )
    op.create_table('genre',
    sa.Column('pk_id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=32), nullable=False),
    sa.PrimaryKeyConstraint('pk_id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('album',
    sa.Column('pk_id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=150), nullable=False),
    sa.Column('published_at', sa.Date(), nullable=True),
    sa.Column('fk_band_id', sa.BigInteger(), nullable=False),
    sa.ForeignKeyConstraint(['fk_band_id'], ['band.pk_id'], ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('pk_id')
    )
    op.create_table('album_genre',
    sa.Column('fk_album_id', sa.BigInteger(), nullable=False),
    sa.Column('fk_genre_id', sa.BigInteger(), nullable=False),
    sa.ForeignKeyConstraint(['fk_album_id'], ['album.pk_id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['fk_genre_id'], ['genre.pk_id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('fk_album_id', 'fk_genre_id')
    )
    op.create_table('track',
    sa.Column('pk_id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=128), nullable=False),
    sa.Column('length', sa.SmallInteger(), nullable=False),
    sa.Column('fk_album_id', sa.BigInteger(), nullable=False),
    sa.ForeignKeyConstraint(['fk_album_id'], ['album.pk_id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('pk_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('track')
    op.drop_table('album_genre')
    op.drop_table('album')
    op.drop_table('genre')
    op.drop_table('band')
    # ### end Alembic commands ###
