from fastapi import FastAPI
from pydantic import BaseModel
from routers.hello_world import router
from routers.task_router import task_router

app = FastAPI(title="Curso FastAPI + uv")

app.include_router(router)
app.include_router(task_router)