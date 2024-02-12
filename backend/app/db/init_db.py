import logging
from sqlalchemy.orm import Session

from app import crud, schemas
from db import base  # noqa: F401
from core.config import settings

logger = logging.getLogger(__name__)

OBREIROS = [
    {
        "id": 1,
        "name": "ADEMAR FARIAS BORGES",
        "func": "Presbitero",
        "cong": "Monte Horebe",
    },    
    {
        "id": 2,
        "name": "ADRIANO G. DE ALMEIDA",
        "func": "Missionário",
        "cong": "Templo Central",
    },
    {
        "id": 3,
        "name": "ADRIANO SENA SOUZA",
        "func": "Diácono",
        "cong": "Luz e Vida",
    },
]

# make sure all SQL Alchemy models are imported (app.db.base) before initializing DB
# otherwise, SQL Alchemy might fail to initialize relationships properly
# for more details: https://github.com/tiangolo/full-stack-fastapi-postgresql/issues/28


def init_db(db: Session) -> None:
    # Tables should be created with Alembic migrations
    # But if you don't want to use migrations, create
    # the tables un-commenting the next line
    # Base.metadata.create_all(bind=engine)
    for obreiro in OBREIROS:
        obreiro_in = schemas.ObreiroCreate(
            name=obreiro["name"],
            func=obreiro["func"],
            cong=obreiro["cong"],
        )
        crud.obreiro.create(db, obj_in=obreiro_in)
    
