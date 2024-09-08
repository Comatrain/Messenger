"""001_init

Revision ID: 7e8e4ef67c0b
Revises: 
Create Date: 2024-09-08 23:34:51.532645

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7e8e4ef67c0b'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('account',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('login', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_account')),
    sa.UniqueConstraint('login', name=op.f('uq_account_login'))
    )
    op.create_index(op.f('ix_account_id'), 'account', ['id'], unique=False)
    op.create_table('company',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('address', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_company'))
    )
    op.create_index(op.f('ix_company_id'), 'company', ['id'], unique=False)
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('account_login', sa.String(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=False),
    sa.Column('last_name', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('company_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['account_login'], ['account.login'], name=op.f('fk_user_account_login_account')),
    sa.ForeignKeyConstraint(['company_id'], ['company.id'], name=op.f('fk_user_company_id_company')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_user'))
    )
    op.create_index(op.f('ix_user_id'), 'user', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_id'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_company_id'), table_name='company')
    op.drop_table('company')
    op.drop_index(op.f('ix_account_id'), table_name='account')
    op.drop_table('account')
    # ### end Alembic commands ###
