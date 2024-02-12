from pydantic import BaseModel
from typing import Sequence

class EntradaBase(BaseModel):
    nome: str
    desc: str

class EntradaCreate(EntradaBase):    
    nome: str
    desc: str

class EntradaUpdate(EntradaBase):
    id: int


class EntradaUpdateRestricted(BaseModel):
    id: int
    nome: int


# Properties shared by models stored in DB
class EntradaInDBBase(EntradaBase):
    id: int

    class Config:
        from_attributes = True


# Properties to return to client
class Entrada(EntradaInDBBase):
    pass


# Properties properties stored in DB
class EntradaInDB(EntradaInDBBase):
    pass


class EntradaSearchResults(BaseModel):
    results: Sequence[Entrada]
