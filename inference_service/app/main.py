from fastapi import FastAPI
import mlflow.sklearn
from pydantic import BaseModel

app = FastAPI(swagger_ui_parameters={"syntaxHighlight": False})

model_uri = "models:/TodoClassifier@champion"
loaded_model = mlflow.sklearn.load_model(model_uri)

class TaskInput(BaseModel):
    task: str

@app.get("/health")
def health():
    if loaded_model:
        return {"status": "ok"}
    else:
        return{"status": "unhealthy"}


@app.post("/predict")
def prediction(input_data: TaskInput): # FastAPI automatycznie rozpakuje JSON-a
    prediction = loaded_model.predict([input_data.task])
    return prediction[0]
