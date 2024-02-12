from crud.base import CRUDBase
from models.lancamento import Lancamento
from schemas.lancamento import LancamentoCreate, LancamentoUpdate, LancamentoRemove

class CRUDlancamento(CRUDBase[Lancamento, LancamentoCreate, LancamentoUpdate, LancamentoRemove]):
    ...

lancamento = CRUDlancamento(Lancamento)