from fastapi import FastAPI

app = FastAPI(swagger_ui_parameters={"syntaxHighlight": False})

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def prediction(task: str):
    return "testreturn"