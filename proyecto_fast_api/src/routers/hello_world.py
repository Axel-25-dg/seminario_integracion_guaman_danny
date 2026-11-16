from mimetypes import init

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class Mensaje(BaseModel):
    text: str
    prioridad: init = 1
    campo_interno: str



@router.get("/")
def read_root() -> dict[str, str]:
    return {
        "mensaje": "Bienvenido al curso de FastAPI + uv", 
        "autor": "Danny Guaman",
        "version": "0.1.0"
    }


@router.get("/danny")
def read_danny() -> dict[str, str]:
    return {
        "mensaje": "Bienvenido al curso de FastAPI + uv", 
        "autor": "Danny Guaman",
        "version": "0.1.0"
    }

