from pathlib import Path
import time

from fastapi import FastAPI, APIRouter, Request, Depends
from fastapi_pagination import add_pagination
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from api.api_v1.api import api_router
from core.config import settings


BASE_PATH = Path(__file__).resolve().parent

root_router = APIRouter()
app = FastAPI(title="Finansys ADNA", openapi_url=f"{settings.API_V1_STR}/openapi.json")

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_origin_regex=settings.BACKEND_CORS_ORIGIN_REGEX,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

@root_router.get("/", status_code=200)
def root(
    request: Request,
) -> dict:
    return {"request": request, "obreiros": "Lista de Obreiros"}

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

app.include_router(api_router, prefix=settings.API_V1_STR)
app.include_router(root_router)

if __name__ == "__main__":
    # Use this for debugging purposes only
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=True)
