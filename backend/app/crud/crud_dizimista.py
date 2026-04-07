from app.crud.base import CRUDBase
from app.models.dizimista import Dizimista
from app.schemas.dizimista import DizimistaCreate, DizimistaUpdate, DizimistaRemove

class CRUDHistorico(CRUDBase[Dizimista, DizimistaCreate, DizimistaUpdate, DizimistaRemove]):
    ...

dizimista = CRUDHistorico(Dizimista)