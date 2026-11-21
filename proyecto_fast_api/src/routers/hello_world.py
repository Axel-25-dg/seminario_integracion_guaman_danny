from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Mensaje(BaseModel):
    texto: str
    prioridad: int = 1
    campo_interno: str 

@router.get("/")
def read_root() -> dict[str, str]:
    return {"mensaje": "Hola desde FastAPI + uv", 
            "autor":"Danny Guaman",
            "version" : "0.1.0"}

@router.get("/danny")
def endpoint_danny() -> Mensaje:
    return Mensaje(texto="Hola Danny", campo_interno= "desde danny link")

@router.get("/guaman", response_model=Mensaje)
def endpoint_guaman():
    return {"texto": "Hola guaman", 
            "prioridad": 5, 
            "campo_interno": "imprime desde endpoint guaman"}

@router.get("/campo-extra", response_model=Mensaje)
def endpoint_campo_extra():
    return {"texto": "Hola Danny", 
            "prioridad": 5, 
            "campo_interno": "si debe salir incluido en el modelo", 
            "campo_extra":"no deberia salir"}