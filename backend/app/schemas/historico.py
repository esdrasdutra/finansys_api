from pydantic import BaseModel
from typing import Sequence
from datetime import date

class HistoricoBase(BaseModel):
    lanc_recibo: int
    lanc_obs: str
    lanc_tipo_recbico: str
    lanc_nome_dizimista: str
    lanc_movimentacao: str
    lanc_cong: str
    lanc_data_lan: str

class HistoricoCreate(HistoricoBase):
    lanc_recibo: int
    lanc_obs: str
    lanc_tipo_recbico: str
    lanc_nome_dizimista: str
    lanc_movimentacao: str
    lanc_cong: str
    lanc_data_lan: date


class HistoricoUpdate(HistoricoBase):
    id: int

class HistoricoRemove(HistoricoBase):
    id: int    


class HistoricoUpdateRestricted(BaseModel):
    id: int
    lanc_recibo: int


# Properties shared by models stored in DB
class HistoricoInDBBase(HistoricoBase):
    id: int

    class Config:
        from_attributes = True


# Properties to return to client
class Historico(HistoricoInDBBase):
    pass


# Properties properties stored in DB
class HistoricoInDB(HistoricoInDBBase):
    pass


class HistoricoSearchResults(BaseModel):
    results: Sequence[Historico]
