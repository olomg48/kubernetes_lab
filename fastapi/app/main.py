from fastapi import FastAPI
from .routers import tasks
from prometheus_fastapi_instrumentator import Instrumentator


app = FastAPI(swagger_ui_parameters={"syntaxHighlight": False})
Instrumentator().instrument(app).expose(app)


@app.get("/health")
def health():
    return {"status": "ok"}

app.include_router(tasks.router)