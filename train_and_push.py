import mlflow
import mlflow.sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
mlflow.set_tracking_uri("http://localhost:5000")
# 1. Przykładowe dane
data = [
    ("Napisz raport finansowy", "Praca"),
    ("Kup mleko i chleb", "Zakupy"),
    ("Umyj okna w salonie", "Dom"),
    ("Przygotuj prezentację na spotkanie", "Praca"),
    ("Odbierz pranie", "Dom"),
    ("Zamów karmę dla psa", "Zakupy"),
    ("Kup jedzenie", "Zakupy")
]

texts, labels = zip(*data)

# 2. Ustawienie eksperymentu
mlflow.set_experiment("Task_Categorizer")

# Włączamy autologowanie - MLflow samo zapisze parametry i model!
mlflow.sklearn.autolog()

with mlflow.start_run():
    # 3. Budowa prostego modelu (Pipeline)
    # TF-IDF zamienia tekst na liczby, LogisticRegression klasyfikuje
    model = Pipeline([
        ('tfidf', TfidfVectorizer()),
        ('clf', LogisticRegression())
    ])

    # Trenujemy model
    model.fit(texts, labels)
    
    # Logujemy dodatkową informację ręcznie (opcjonalnie)
    mlflow.set_tag("release.version", "1.0.0")
    mlflow.sklearn.log_model(model, "model")
    print("Model wytrenowany i zapisany w MLflow!")