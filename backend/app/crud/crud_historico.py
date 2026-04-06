from app.crud.base import CRUDBase
from app.models.historico import Historico
from app.schemas.historico import HistoricoCreate, HistoricoUpdate, HistoricoRemove

class CRUDHistorico(CRUDBase[Historico, HistoricoCreate, HistoricoUpdate, HistoricoRemove]):
    ...

historico = CRUDHistorico(Historico)