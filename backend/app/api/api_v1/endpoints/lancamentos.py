from math import ceil
from typing import  Annotated, Optional
from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session
from fastapi_pagination.ext.sqlalchemy import paginate

from sqlalchemy import Enum, asc, desc, func, select

from fastapi_pagination import Page

import crud

from api import deps

from schemas.lancamento import (
    LancamentoBase,
    LancamentoRemove,
    LancamentoCreate,
    LancamentoUpdate,
    Lancamento,
    LancamentosList
)
from schemas.paginacao import Pagination, SortEnum, pagination_params

router = APIRouter()

@router.get("/", 
            name="Retorna, de forma paginada, as informações dos lançamentos", 
            status_code=200,
            )
def get_lancamentos(
    *,
    db: Session = Depends(deps.get_db),
    perPage: Optional[int],
    page: Optional[int],
    order: str = 'asc'
    ):
        
        result = crud.lancamento.get_all_page(db=db, perPage=perPage, page=page, order=order)

        if not result:
            # the exception is raised, not returned - you will get a validation
            # error otherwise.
            raise HTTPException(
                status_code=404, detail=f"Lancamento  not found"
            )

        return result

@router.get("/all", name="Retorna todas as informações dos lançamentos", status_code=200)
def get_all(*, db: Session = Depends(deps.get_db)):
    
    result = crud.lancamento.get_all(db=db)
    if not result:
            # the exception is raised, not returned - you will get a validation
            # error otherwise.
            raise HTTPException(
                status_code=404, detail=f"Lancamento  not found"
            )
    return result

@router.get("/all_crude", name="Retorna todas as informações dos lançamentos", status_code=200)
def get_all_crude(*, db: Session = Depends(deps.get_db)):
    
    result = crud.lancamento.get_all_crude(db=db)
    if not result:
            # the exception is raised, not returned - you will get a validation
            # error otherwise.
            raise HTTPException(
                status_code=404, detail=f"Lancamento  not found"
            )
    return result

@router.get("/{lancamento_id}", status_code=200)
def fetch_lancamento(
    *,
    lancamento_id: int,
    db: Session = Depends(deps.get_db),
) -> dict:
    """
    Fetch a single Lancamento by ID
    """
    result = crud.lancamento.get(db=db, id=lancamento_id)
    if not result:
        # the exception is raised, not returned - you will get a validation
        # error otherwise.
        raise HTTPException(
            status_code=404, detail=f"Lancamento with ID {lancamento_id} not found"
        )

    return result.to_dict()

@router.get("/search/", status_code=200)
def search_lancamentos(
    *,
    #keyword: str = Query(None, min_length=3, example="Recibo Nº"),
    max_results: Optional[int] = 10,
    page: Optional[int] = 20,
    db: Session = Depends(deps.get_db),
) -> dict:
    """
    Search for Lancamentos based on label keyword
    """
    lancamentos = crud.lancamento.get_multi(db=db, page=page, size=max_results)

    return {"results": list(lancamentos)}


@router.post("/", status_code=201)
def create_lancamento(
    *,
    lancamento_in: LancamentoCreate,
    db: Session = Depends(deps.get_db),
) -> dict:
    """
    Create a new Lancamento in the database.
    """
    lancamento = crud.lancamento.create(db=db, obj_in=lancamento_in)

    return lancamento.to_dict()


@router.put("/", status_code=201)
def update_lancamento(
    *,
    lancamento_in: LancamentoUpdate,
    db: Session = Depends(deps.get_db),
):
    """
    Update Lancamento in the database.
    """    
    lancamento = crud.lancamento.get(db, id=lancamento_in.id)

    if not lancamento:
        raise HTTPException(
            status_code=400, detail=f"Lançamento with ID: {lancamento_in.id} not found."
        )
    updated_lancamento = crud.lancamento.update(db=db, db_obj=lancamento, obj_in=lancamento_in)

    return updated_lancamento.to_dict()

@router.delete('/{lancamento_id}', status_code=200)
def remove_lancamento(
    *, 
    lancamento_id: int,
    db: Session = Depends(deps.get_db),
) -> dict:
    """
    Remove Lancamento from database
    """
    lancamento = crud.lancamento.get(db, id=lancamento_id)
    if not lancamento:            
        raise HTTPException(
            status_code=400, detail=f"Lançamento with ID: {lancamento_id} not found."
        )
    lancamento_removed = crud.lancamento.remove(db=db, id=lancamento_id)

    return lancamento_removed