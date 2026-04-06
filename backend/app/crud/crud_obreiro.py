from app.crud.base import CRUDBase
from app.models.obreiro import Obreiro
from app.schemas.obreiro import ObreiroCreate, ObreiroUpdate, ObreiroRemove

class CRUDObreiro(CRUDBase[Obreiro, ObreiroCreate, ObreiroUpdate, ObreiroRemove]):
    ...

obreiro = CRUDObreiro(Obreiro)
