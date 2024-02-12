"""Add Tables

Revision ID: 67cec0621335
Revises: 
Create Date: 2024-01-30 16:53:54.130400

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '67cec0621335'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dizimista',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=256), nullable=False),
    sa.Column('func', sa.String(length=256), nullable=True),
    sa.Column('cong', sa.String(length=256), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_dizimista_id'), 'dizimista', ['id'], unique=False)
    op.create_table('documento',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tipo_doc', sa.String(length=256), nullable=False),
    sa.Column('desc', sa.String(length=256), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_documento_id'), 'documento', ['id'], unique=False)
    op.create_table('entrada',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=256), nullable=False),
    sa.Column('desc', sa.String(length=256), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_entrada_id'), 'entrada', ['id'], unique=False)
    op.create_table('lancamento',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('recibo', sa.String(length=256), nullable=False),
    sa.Column('data_lan', sa.Date(), nullable=False),
    sa.Column('data_ven', sa.Date(), nullable=False),
    sa.Column('tipo_doc', sa.String(length=256), nullable=False),
    sa.Column('num_doc', sa.String(length=256), nullable=False),
    sa.Column('inflow', sa.String(length=256), nullable=False),
    sa.Column('outflow', sa.String(length=256), nullable=False),
    sa.Column('cong', sa.String(length=256), nullable=False),
    sa.Column('suplier', sa.String(length=256), nullable=False),
    sa.Column('tither', sa.String(length=256), nullable=False),
    sa.Column('value', sa.String(length=256), nullable=False),
    sa.Column('history', sa.String(length=256), nullable=False),
    sa.Column('status', sa.String(length=256), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_lancamento_id'), 'lancamento', ['id'], unique=False)
    op.create_table('obreiro',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=256), nullable=False),
    sa.Column('func', sa.String(length=256), nullable=False),
    sa.Column('cong', sa.String(length=256), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_obreiro_id'), 'obreiro', ['id'], unique=False)
    op.create_table('saida',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=256), nullable=False),
    sa.Column('desc', sa.String(length=256), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_saida_id'), 'saida', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_saida_id'), table_name='saida')
    op.drop_table('saida')
    op.drop_index(op.f('ix_obreiro_id'), table_name='obreiro')
    op.drop_table('obreiro')
    op.drop_index(op.f('ix_lancamento_id'), table_name='lancamento')
    op.drop_table('lancamento')
    op.drop_index(op.f('ix_entrada_id'), table_name='entrada')
    op.drop_table('entrada')
    op.drop_index(op.f('ix_documento_id'), table_name='documento')
    op.drop_table('documento')
    op.drop_index(op.f('ix_dizimista_id'), table_name='dizimista')
    op.drop_table('dizimista')
    # ### end Alembic commands ###