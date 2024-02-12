"""Update Lancamento

Revision ID: 2e0ab4c5d4e3
Revises: ebc48123e636
Create Date: 2024-02-01 05:52:52.415036

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2e0ab4c5d4e3'
down_revision = 'ebc48123e636'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('lancamento', sa.Column('recibo', sa.String(length=256), nullable=False))
    op.add_column('lancamento', sa.Column('data_lan', sa.Date(), nullable=False))
    op.add_column('lancamento', sa.Column('data_ven', sa.Date(), nullable=False))
    op.add_column('lancamento', sa.Column('tipo_doc', sa.String(length=256), nullable=False))
    op.add_column('lancamento', sa.Column('num_doc', sa.String(length=256), nullable=False))
    op.add_column('lancamento', sa.Column('entrada', sa.String(length=256), nullable=False))
    op.add_column('lancamento', sa.Column('saida', sa.String(length=256), nullable=False))
    op.add_column('lancamento', sa.Column('cong', sa.String(length=256), nullable=False))
    op.add_column('lancamento', sa.Column('forn', sa.String(length=256), nullable=False))
    op.add_column('lancamento', sa.Column('dizimista', sa.String(length=256), nullable=False))
    op.add_column('lancamento', sa.Column('obs', sa.String(length=256), nullable=False))
    op.add_column('lancamento', sa.Column('valor', sa.String(length=256), nullable=False))
    op.add_column('lancamento', sa.Column('conta', sa.String(length=256), nullable=False))
    op.add_column('lancamento', sa.Column('situacao', sa.String(length=256), nullable=False))
    op.add_column('lancamento', sa.Column('tipo_lanc', sa.String(length=256), nullable=False))
    op.add_column('lancamento', sa.Column('historico', sa.String(length=256), nullable=False))
    op.add_column('lancamento', sa.Column('status_lanc', sa.String(length=256), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('lancamento', 'status_lanc')
    op.drop_column('lancamento', 'historico')
    op.drop_column('lancamento', 'tipo_lanc')
    op.drop_column('lancamento', 'situacao')
    op.drop_column('lancamento', 'conta')
    op.drop_column('lancamento', 'valor')
    op.drop_column('lancamento', 'obs')
    op.drop_column('lancamento', 'dizimista')
    op.drop_column('lancamento', 'forn')
    op.drop_column('lancamento', 'cong')
    op.drop_column('lancamento', 'saida')
    op.drop_column('lancamento', 'entrada')
    op.drop_column('lancamento', 'num_doc')
    op.drop_column('lancamento', 'tipo_doc')
    op.drop_column('lancamento', 'data_ven')
    op.drop_column('lancamento', 'data_lan')
    op.drop_column('lancamento', 'recibo')
    # ### end Alembic commands ###