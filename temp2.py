import mlflow
import pandas as pd

mlflow.set_tracking_uri("http://localhost:5000")
logged_model = 'runs:/54c1be9f75ff4597995e28b873b7d493/model'
loaded_model = mlflow.pyfunc.load_model(logged_model)

# Przygotowujemy dane jako DataFrame
# Ważne: dane muszą być typu str (napisy)
tasks_list = ["Kupić chleb", "Naprawić błąd w kodzie"]
df_tasks = pd.DataFrame(tasks_list, columns=["text"])

# Upewniamy się, że wszystko to stringi (na wszelki wypadek)
df_tasks = df_tasks.astype(str)
print(df_tasks)
predictions = loaded_model.predict(df_tasks.tolist())
print(f"Wyniki: {predictions}")
