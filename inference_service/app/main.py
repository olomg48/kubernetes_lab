from fastapi import FastAPI
import mlflow.sklearn

app = FastAPI(swagger_ui_parameters={"syntaxHighlight": False})
print("test")
mlflow.set_tracking_uri("http://mlflow:5000")

model_uri = "models:/TodoClassifier@champion"
loaded_model = mlflow.sklearn.load_model(model_uri)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def prediction(task: str):
    prediction = loaded_model.predict([task])
    return prediction[0]
    #return("siematest")