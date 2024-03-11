from typing import Any, Optional

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from api import deps
import crud

from schemas import (
    DizimistaCreate,
    DizimistaUpdateRestricted,
)

router = APIRouter()

@router.get("/all", status_code=200)
def fetch_dizimistas(
    *, 
    db: Session = Depends(deps.get_db),
) -> dict:
    """
    Fetch all Dizimistas
    """
    results = crud.dizimista.get_all(db=db)
    if not results:
    # the exception is raised, not returned - you will get a validation
    # error otherwise.
        raise HTTPException(
            status_code=404, detail=f"Nenhum Dizimista encontrado"
        )

    return results

@router.get("/{dizimista_id}", status_code=200)
def fetch_dizimista(
    *,
    dizimista_id: int,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Fetch a single Dizimista by ID
    """
    result = crud.dizimista.get(db=db, id=dizimista_id)
    if not result:
        # the exception is raised, not returned - you will get a validation
        # error otherwise.
        raise HTTPException(
            status_code=404, detail=f"Dizimista with ID {dizimista_id} not found"
        )

    return result

@router.get("/search/", status_code=200)
def search_dizimistas(
    *,
    keyword: str = Query(None, min_length=3, example="Alberto"),
    max_results: Optional[int] = 10,
    db: Session = Depends(deps.get_db),
) -> dict:
    """
    Search for Dizimistas based on label keyword
    """
    dizimistas = crud.dizimista.get_multi(db=db, limit=max_results)
    results = filter(lambda dizimista: keyword.lower() in dizimistas.label.lower(), dizimistas)

    return {"results": list(results)}


@router.post("/", status_code=201)
def create_dizimista(
    *,
    dizimista_in: DizimistaCreate,
    db: Session = Depends(deps.get_db),
) -> dict:
    """
    Create a new dizimista in the database.
    """
    dizimista = crud.dizimista.create(db=db, obj_in=dizimista_in)

    return dizimista


@router.put("/", status_code=201)
def update_dizimista(
    *,
    dizimista_in: DizimistaUpdateRestricted,
    db: Session = Depends(deps.get_db),
) -> dict:
    """
    Update dizimista in the database.
    """
    dizimista = crud.dizimista.get(db, id=dizimista_in.id)
    if not dizimista:
        raise HTTPException(
            status_code=400, detail=f"dizimista with ID: {dizimista_in.id} not found."
        )

    updated_dizimista = crud.dizimista.update(db=db, db_obj=dizimista, obj_in=dizimista_in)
    return updated_dizimista

@router.delete('/{dizimista_id}', status_code=200)
def delete_dizimista(*, dizimista_id: int) -> dict:
    print('REMOVENDO OBJ')