from pydantic import BaseModel
from typing import Sequence

class DizimistaBase(BaseModel):
    nome: str
    func: str
    cong: str

class DizimistaCreate(DizimistaBase):
    name: str
    func: str
    cong: str


class DizimistaUpdate(DizimistaBase):
    id: int

class DizimistaRemove(DizimistaBase):
    id: int    


class DizimistaUpdateRestricted(BaseModel):
    id: int
    name: str


# Properties shared by models stored in DB
class DizimistaInDBBase(DizimistaBase):
    id: int

    class Config:
        from_attributes = True


# Properties to return to client
class Dizimista(DizimistaInDBBase):
    pass


# Properties properties stored in DB
class DizimistaInDB(DizimistaInDBBase):
    pass


class DizimistaSearchResults(BaseModel):
    results: Sequence[Dizimista]
