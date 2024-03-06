from typing import  Optional

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

import crud

from api import deps

from schemas.lancamento import (
    LancamentoRemove,
    LancamentoCreate,
    LancamentoUpdate,
    Lancamento
)

router = APIRouter()

@router.get("/all", status_code=200)
def fetch_lancamentos(
    *, 
    db: Session = Depends(deps.get_db),
) -> dict:
    """
    Fetch all Lancamentos
    """
    results = crud.lancamento.get_all(db=db)
    if not results:
    # the exception is raised, not returned - you will get a validation
    # error otherwise.
        raise HTTPException(
            status_code=404, detail=f"Nenhum lançamento encontrado"
        )

    return { "data": results, "message": "Busca feita com sucesso." }


@router.get("/{lancamento_id}", status_code=200)
def fetch_lancamento(
    *,
    lancamento_id: int,
    db: Session = Depends(deps.get_db),
) -> dict:
    """
    Fetch a single Obreiro by ID
    """
    result = crud.lancamento.get(db=db, id=lancamento_id)
    if not result:
        # the exception is raised, not returned - you will get a validation
        # error otherwise.
        raise HTTPException(
            status_code=404, detail=f"Lancamento with ID {lancamento_id} not found"
        )

    return result

@router.get("/search/", status_code=200)
def search_lancamentos(
    *,
    keyword: str = Query(None, min_length=3, example="Recibo Nº"),
    max_results: Optional[int] = 10,
    db: Session = Depends(deps.get_db),
) -> dict:
    """
    Search for Lancamentos based on label keyword
    """
    lancamentos = crud.lancamento.get_multi(db=db, limit=max_results)
    results = filter(lambda lancamento: keyword.lower() in lancamentos.label.lower(), lancamentos)

    return {"results": list(results)}


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

    return lancamento


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

    return updated_lancamento

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