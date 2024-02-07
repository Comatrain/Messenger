"""create account table

Revision ID: 860ac0213ff3
Revises: 
Create Date: 2024-02-06 20:50:55.332663

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '860ac0213ff3'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String),
        sa.Column('email', sa.String),
        sa.Column('password', sa.String),
    )


def downgrade() -> None:
    pass
