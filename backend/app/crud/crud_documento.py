from app.crud.base import CRUDBase
from app.models.documento import Documento
from app.schemas.documento import DocumentoCreate, DocumentoUpdate, DocumentoRemove

class CRUDdocumento(CRUDBase[Documento, DocumentoCreate, DocumentoUpdate, DocumentoRemove]):
    ...

documento = CRUDdocumento(Documento)