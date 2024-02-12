from typing import Any, Optional

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from api import deps
import crud

from schemas.historico import (
    Historico,
    HistoricoCreate,
    HistoricoSearchResults,
    HistoricoUpdateRestricted,
)

router = APIRouter()

@router.get("/all", status_code=200)
def fetch_historicos(
    *, 
    db: Session = Depends(deps.get_db),
) -> dict:
    """
    Fetch all historicos
    """
    results = crud.lancamento.get_all(db=db)
    if not results:
    # the exception is raised, not returned - you will get a validation
    # error otherwise.
        raise HTTPException(
            status_code=404, detail=f"Nenhum histórico encontrado"
        )

    return results

@router.get("/{historico_id}", status_code=200)
def fetch_historicos(
    *,
    historico_id: int,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Fetch a single Obreiro by ID
    """
    result = crud.historico.get(db=db, id=historico_id)
    if not result:
        # the exception is raised, not returned - you will get a validation
        # error otherwise.
        raise HTTPException(
            status_code=404, detail=f"historico with ID {historico_id} not found"
        )

    return result

@router.get("/search/", status_code=200)
def search_historicos(
    *,
    keyword: str = Query(None, min_length=3, example="Recibo Nª"),
    max_results: Optional[int] = 10,
    db: Session = Depends(deps.get_db),
) -> dict:
    """
    Search for Historicos based on label keyword
    """
    historicos = crud.historico.get_multi(db=db, limit=max_results)
    results = filter(lambda historico: keyword.lower() in historicos.label.lower(), historicos)

    return {"results": list(results)}


@router.post("/", status_code=201)
def create_historico(
    *,
    historico_in: HistoricoCreate,
    db: Session = Depends(deps.get_db),
) -> dict:
    """
    Create a new historico in the database.
    """
    historico = crud.historico.create(db=db, obj_in=historico_in)

    return historico


@router.put("/", status_code=201)
def update_historico(
    *,
    historico_in: HistoricoUpdateRestricted,
    db: Session = Depends(deps.get_db),
) -> dict:
    """
    Update historico in the database.
    """
    historico = crud.historico.get(db, id=historico_in.id)
    if not historico:
        raise HTTPException(
            status_code=400, detail=f"Historico with ID: {historico_in.id} not found."
        )

    updated_historico = crud.historico.update(db=db, db_obj=historico, obj_in=historico_in)
    return updated_historico

@router.delete('/{historico_id}', status_code=200)
def delete_historico(*, historico_id: int) -> dict:
    print('REMOVENDO OBJ')
