from datetime import date
from pydantic import BaseModel
from typing import Sequence

class LancamentoBase(BaseModel):
    recibo: str
    data_lan: date
    data_ven: date
    tipo_doc: str
    num_doc: str
    entrada: str
    saida: str
    cong: str
    forn: str
    dizimista: str
    obs: str
    valor: str
    conta: str
    situacao: str
    tipo_lanc: str
    historico: str
    status_lanc: str

class LancamentoCreate(LancamentoBase):
    recibo: str
    data_lan: date
    data_ven: date
    tipo_doc: str
    num_doc: str
    entrada: str
    saida: str
    cong: str
    forn: str
    dizimista: str
    obs: str
    valor: str
    conta: str
    situacao: str
    tipo_lanc: str
    historico: str
    status_lanc: str

class LancamentoUpdate(LancamentoBase):
    id: int
    recibo: str
    data_lan: date
    data_ven: date
    tipo_doc: str
    num_doc: str
    entrada: str
    saida: str
    cong: str
    forn: str
    dizimista: str
    obs: str
    valor: str
    conta: str
    situacao: str
    tipo_lanc: str
    historico: str
    status_lanc: str

class LancamentoRemove(LancamentoBase):
    id: int

class LancamentoUpdateRestricted(BaseModel):
    id: int
    recibo: str
    data_lan: date
    data_ven: date
    tipo_doc: str
    num_doc: str
    entrada: str
    saida: str
    cong: str
    forn: str
    dizimista: str
    obs: str
    valor: str
    conta: str
    situacao: str
    tipo_lanc: str
    historico: str
    status_lanc: str


# Properties shared by models stored in DB
class LancamentoInDBBase(LancamentoBase):
    id: int

    class Config:
        from_attributes = True


# Properties to return to client
class Lancamento(LancamentoInDBBase):
    pass


# Properties properties stored in DB
class LancamentoInDB(LancamentoInDBBase):
    pass


class LancamentoSearchResults(BaseModel):
    results: Sequence[Lancamento]
