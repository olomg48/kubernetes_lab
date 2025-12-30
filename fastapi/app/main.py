from fastapi import FastAPI
from .routers import tasks
app = FastAPI(swagger_ui_parameters={"syntaxHighlight": False})

@app.get("/health")
def health():
    return {"status": "ok"}

app.include_router(tasks.router)