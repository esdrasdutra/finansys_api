
from fastapi.params import Query
from pydantic import BaseModel
from sqlalchemy import Enum


class SortEnum(Enum):
    ASC = 'asc',
    DESC = 'desc'

class Pagination(BaseModel):
    perPage: int
    page: int
    order: SortEnum

    class Config:
        arbitrary_types_allowed = True
    
def pagination_params(
    page: int = Query(ge=1, required=False, default=1),
    perPage: int = Query(ge=1, le=100, required=False, default=5),
    order: SortEnum = SortEnum.DESC
):
    return Pagination(perPage=perPage, page=page, order=order.value)