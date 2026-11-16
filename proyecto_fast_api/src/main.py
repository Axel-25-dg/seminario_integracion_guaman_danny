from importlib import import_module

from fastapi import FastAPI

PASO = 1

if PASO == 1:
    router_module = import_module("proyecto_fast_api.routers.paso1_bienvenida")
elif PASO == 2:
    router_module = import_module("proyecto_fast_api.routers.paso2_placeholder")
else:
    raise ValueError(f"No hay un router configurado para el paso {PASO}")

app = FastAPI(title="Curso FastAPI + uv")
app.include_router(router_module.router)
