import pathlib

from pydantic import AnyHttpUrl, EmailStr, validator

from pydantic_settings import BaseSettings

from typing import List, Optional, Union

# Project Directories
ROOT = pathlib.Path(__file__).resolve().parent.parent

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"

    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    # e.g: '["http://localhost", "http://localhost:4200", "http://localhost:3000", \
    # "http://localhost:8080", "http://local.dockertoolbox.tiangolo.com"]'
    BACKEND_CORS_ORIGINS: List = [
        "http://localhost:4200",
        "http://localhost:8001",  # type: ignore
    ]

    # Origins that match this regex OR are in the above list are allowed
    BACKEND_CORS_ORIGIN_REGEX: Optional[
        str
    ] = r"https.*\.(netlify.app|herokuapp.com)"  # noqa: W605
    
    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> List[str]:
        if isinstance(v, str):
            # Verifica se é uma lista JSON ou uma string separada por vírgulas
            if v.startswith("[") and v.endswith("]"):
                import json
                return json.loads(v)
            return [i.strip() for i in v.split(",") if i.strip()]
        elif isinstance(v, list):
            return v
        raise ValueError(f"Formato inválido para BACKEND_CORS_ORIGINS: {v}")

    SQLALCHEMY_DATABASE_URI: Optional[str] = "sqlite:///fs.sqlite3"

    class Config:
        case_sensitive = True

settings = Settings()
