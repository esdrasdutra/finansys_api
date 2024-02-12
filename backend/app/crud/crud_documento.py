from crud.base import CRUDBase
from models.documento import Documento
from schemas.documento import DocumentoCreate, DocumentoUpdate, DocumentoRemove

class CRUDdocumento(CRUDBase[Documento, DocumentoCreate, DocumentoUpdate, DocumentoRemove]):
    ...

documento = CRUDdocumento(Documento)