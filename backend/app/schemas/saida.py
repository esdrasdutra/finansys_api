from pydantic import BaseModel
from typing import Sequence

class SaidaBase(BaseModel):
    nome: str
    desc: str

class SaidaCreate(SaidaBase):    
    nome: str
    desc: str

class SaidaUpdate(SaidaBase):
    id: int


class SaidaUpdateRestricted(BaseModel):
    id: int
    nome: int


# Properties shared by models stored in DB
class SaidaInDBBase(SaidaBase):
    id: int

    class Config:
        from_attributes = True


# Properties to return to client
class Saida(SaidaInDBBase):
    pass


# Properties properties stored in DB
class SaidaInDB(SaidaInDBBase):
    pass


class SaidaSearchResults(BaseModel):
    results: Sequence[Saida]
