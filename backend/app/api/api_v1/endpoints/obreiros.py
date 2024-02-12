import asyncio
from typing import Any, Optional

import httpx
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

import crud
from api import deps

from schemas.obreiro import (
    Obreiro,
    ObreiroCreate,
    ObreiroSearchResults,
    ObreiroUpdateRestricted,
)

router = APIRouter()

@router.get("/all", status_code=200)
def fetch_obreiros(
    *, 
    db: Session = Depends(deps.get_db),
) -> dict:
    """
    Fetch all obreiros
    """
    results = crud.obreiro.get_all(db=db)
    if not results:
    # the exception is raised, not returned - you will get a validation
    # error otherwise.
        raise HTTPException(
            status_code=404, detail=f"Nenhum obreiro encontrado"
        )

    return { "data": results, "message": "Busca feita com sucesso." }

@router.get("/{obreiro_id}", status_code=200)
def fetch_obreiro(
    *,
    obreiro_id: int,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Fetch a single Obreiro by ID
    """
    result = crud.obreiro.get(db=db, id=obreiro_id)
    if not result:
        # the exception is raised, not returned - you will get a validation
        # error otherwise.
        raise HTTPException(
            status_code=404, detail=f"Obreiro with ID {obreiro_id} not found"
        )

    return result

@router.get("/search/", status_code=200)
def search_obreiros(
    *,
    keyword: str = Query(None, min_length=3, example="Adriano"),
    max_results: Optional[int] = 10,
    db: Session = Depends(deps.get_db),
) -> dict:
    """
    Search for Obreiros based on label keyword
    """
    Obreiros = crud.obreiro.get_multi(db=db, limit=max_results)
    results = filter(lambda Obreiro: keyword.lower() in Obreiro.name.lower(), Obreiros)

    return {"results": list(results)}


@router.post("/", status_code=201)
def create_obreiro(
    *,
    Obreiro_in: ObreiroCreate,
    db: Session = Depends(deps.get_db),
) -> dict:
    """
    Create a new Obreiro in the database.
    """
    obreiro = crud.obreiro.create(db=db, obj_in=Obreiro_in)

    return obreiro


@router.put("/", status_code=201)
def update_Obreiro(
    *,
    Obreiro_in: ObreiroUpdateRestricted,
    db: Session = Depends(deps.get_db),
) -> dict:
    """
    Update Obreiro in the database.
    """
    Obreiro = crud.obreiro.get(db, id=Obreiro_in.id)
    if not Obreiro:
        raise HTTPException(
            status_code=400, detail=f"Obreiro with ID: {Obreiro_in.id} not found."
        )

    updated_obreiro = crud.obreiro.update(db=db, db_obj=Obreiro, obj_in=Obreiro_in)
    return updated_obreiro

@router.delete('/{obreiro_id}', status_code=200)
def delete_obreiro(*, obreiro_id: int) -> dict:
    print('REMOVENDO OBJ')
