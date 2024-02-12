# Import all the models, so that Base has them before being
# imported by Alembic
from app.db.base_class import Base
from app.models.obreiro import Obreiro
from app.models.lancamento import Lancamento
from app.models.dizimista import Dizimista
from app.models.documento import Documento
from app.models.movimentacao import Entrada, Saida
from app.models.historico import Historico