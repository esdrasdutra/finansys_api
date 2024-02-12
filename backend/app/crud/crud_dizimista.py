from crud.base import CRUDBase
from models.dizimista import Dizimista
from schemas.dizimista import DizimistaCreate, DizimistaUpdate, DizimistaRemove

class CRUDHistorico(CRUDBase[Dizimista, DizimistaCreate, DizimistaUpdate, DizimistaRemove]):
    ...

dizimista = CRUDHistorico(Dizimista)