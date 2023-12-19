"""change varchar length

Revision ID: 6431f315c41c
Revises: 795f155e89d8
Create Date: 2023-12-19 13:02:43.811880

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6431f315c41c'
down_revision: Union[str, None] = '795f155e89d8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('track', 'name',
               existing_type=sa.VARCHAR(length=64),
               type_=sa.VARCHAR(length=128),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('track', 'name',
               existing_type=sa.VARCHAR(length=128),
               type_=sa.VARCHAR(length=64),
               existing_nullable=False)
    # ### end Alembic commands ###
