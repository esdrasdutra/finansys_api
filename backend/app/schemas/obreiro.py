from pydantic import BaseModel, HttpUrl
from typing import Sequence

class ObreiroBase(BaseModel):
    name: str
    func: str
    cong: str


class ObreiroCreate(ObreiroBase):
    name: str
    func: str
    cong: str


class ObreiroUpdate(ObreiroBase):
    id: int

class ObreiroRemove(ObreiroBase):
    id: int


class ObreiroUpdateRestricted(BaseModel):
    id: int
    name: str


# Properties shared by models stored in DB
class ObreiroInDBBase(ObreiroBase):
    id: int
    submitter_id: int

    class Config:
        from_attributes = True


# Properties to return to client
class Obreiro(ObreiroInDBBase):
    pass


# Properties properties stored in DB
class ObreiroInDB(ObreiroInDBBase):
    pass


class ObreiroSearchResults(BaseModel):
    results: Sequence[Obreiro]
