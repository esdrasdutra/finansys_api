from fastapi import APIRouter

from api.api_v1.endpoints import documentos, historicos, lancamentos, dizimistas, obreiros

api_router = APIRouter()
api_router.include_router(obreiros.router, prefix="/obreiros", tags=["obreiros"])
api_router.include_router(lancamentos.router, prefix="/lancamentos", tags=["lancamentos"])
api_router.include_router(historicos.router, prefix="/historicos", tags=["historicos"])
api_router.include_router(dizimistas.router, prefix="/dizimistas", tags=["dizimistas"])
api_router.include_router(documentos.router, prefix="/documentos", tags=["documentos"])
