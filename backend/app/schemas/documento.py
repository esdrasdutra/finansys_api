
from pydantic import BaseModel
from typing import Sequence

class DocumentoBase(BaseModel):
    nome: str
    tipo: str
    desc: str

class DocumentoCreate(DocumentoBase):
    nome: str
    tipo: str
    desc: str



class DocumentoUpdate(DocumentoBase):
    id: int

class DocumentoRemove(DocumentoBase):
    id: int    


class DocumentoUpdateRestricted(BaseModel):
    id: int
    name: str


# Properties shared by models stored in DB
class DocumentoInDBBase(DocumentoBase):
    id: int

    class Config:
        from_attributes = True


# Properties to return to client
class Documento(DocumentoInDBBase):
    pass


# Properties properties stored in DB
class DocumentoInDB(DocumentoInDBBase):
    pass


class DocumentoSearchResults(BaseModel):
    results: Sequence[Documento]
