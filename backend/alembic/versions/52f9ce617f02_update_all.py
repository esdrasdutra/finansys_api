"""Update All

Revision ID: 52f9ce617f02
Revises: e4de1ebfbf3b
Create Date: 2024-02-01 05:29:50.086758

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '52f9ce617f02'
down_revision = 'e4de1ebfbf3b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('lancamento', 'data_lan',
               existing_type=sa.DATE(),
               type_=sa.String(length=12),
               existing_nullable=False)
    op.alter_column('lancamento', 'data_ven',
               existing_type=sa.DATE(),
               type_=sa.String(length=12),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('lancamento', 'data_ven',
               existing_type=sa.String(length=12),
               type_=sa.DATE(),
               existing_nullable=False)
    op.alter_column('lancamento', 'data_lan',
               existing_type=sa.String(length=12),
               type_=sa.DATE(),
               existing_nullable=False)
    # ### end Alembic commands ###