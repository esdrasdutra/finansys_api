from crud.base import CRUDBase
from models.historico import Historico
from schemas.historico import HistoricoCreate, HistoricoUpdate, HistoricoRemove

class CRUDHistorico(CRUDBase[Historico, HistoricoCreate, HistoricoUpdate, HistoricoRemove]):
    ...

historico = CRUDHistorico(Historico)