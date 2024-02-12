from crud.base import CRUDBase
from models.obreiro import Obreiro
from schemas.obreiro import ObreiroCreate, ObreiroUpdate, ObreiroRemove

class CRUDObreiro(CRUDBase[Obreiro, ObreiroCreate, ObreiroUpdate, ObreiroRemove]):
    ...

obreiro = CRUDObreiro(Obreiro)
