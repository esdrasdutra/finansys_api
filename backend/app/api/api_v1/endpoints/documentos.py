from typing import Any, Optional

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.api import deps
import app.crud

from app.schemas.documento import (
    Documento,
    DocumentoCreate,
    DocumentoSearchResults,
    DocumentoUpdateRestricted,
)

router = APIRouter()

@router.get("/all", status_code=200)
def fetch_documentos(
    *, 
    db: Session = Depends(deps.get_db),
) -> dict:
    """
    Fetch all documentos
    """
    results = app.crud.documento.get_all(db=db)
    if not results:
    # the exception is raised, not returned - you will get a validation
    # error otherwise.
        raise HTTPException(
            status_code=404, detail=f"Nenhum documento encontrado"
        )

    return {"results": results}

@router.get("/{documento_id}", status_code=200)
def fetch_documento(
    *,
    documento_id: int,
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Fetch a single Documento by ID
    """
    result = crud.documento.get(db=db, id=documento_id)
    if not result:
        # the exception is raised, not returned - you will get a validation
        # error otherwise.
        raise HTTPException(
            status_code=404, detail=f"Documento with ID {documento_id} not found"
        )

    return result

@router.get("/search/", status_code=200)
def search_documentos(
    *,
    keyword: str = Query(None, min_length=3, example="RECIBO"),
    max_results: Optional[int] = 10,
    db: Session = Depends(deps.get_db),
) -> dict:
    """
    Search for Documentos based on label keyword
    """
    documentos = crud.documento.get_multi(db=db)
    filtered = filter(
        lambda documento: getattr(documento, "label", None) and keyword.lower() in getattr(documento, "label", "").lower(),
        documentos
    )
    results = list(filtered)[:max_results]

    return {"results": results}


@router.post("/", status_code=201)
def create_documento(
    *,
    documento_in: DocumentoCreate,
    db: Session = Depends(deps.get_db),
) -> Documento:
    """
    Create a new Documento in the database.
    """
    documento = crud.documento.create(db=db, obj_in=documento_in)

    return Documento.from_orm(documento)


@router.put("/", status_code=201)
def update_documento(
    *,
    documento_in: DocumentoUpdateRestricted,
    db: Session = Depends(deps.get_db),
) -> dict:
    """
    Update Documento in the database.
    """
    documento = crud.documento.get(db, id=documento_in.id)
    if not documento:
        raise HTTPException(
            status_code=400, detail=f"Documento with ID: {documento_in.id} not found."
        )

    updated_documento = crud.documento.update(db=db, db_obj=documento, obj_in=documento_in.dict())
    return {"result": Documento.from_orm(updated_documento)}

@router.delete('/{documento_id}', status_code=200)
def delete_documento(*, documento_id: int, db: Session = Depends(deps.get_db)) -> dict:
    documento = crud.documento.get(db, id=documento_id)
    if not documento:
        raise HTTPException(
            status_code=404, detail=f"Documento with ID {documento_id} not found"
        )
    crud.documento.remove(db=db, id=documento_id)
    return {"result": f"Documento with ID {documento_id} deleted"}