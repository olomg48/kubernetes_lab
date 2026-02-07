import mlflow
import mlflow.sklearn
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_recall_fscore_support
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline
import os

os.environ['MLFLOW_S3_ENDPOINT_URL'] = "https://03be178ef694-10-244-6-58-30901.spch.r.killercoda.com"
os.environ['AWS_ACCESS_KEY_ID'] = "admin"
os.environ['AWS_SECRET_ACCESS_KEY'] = "password123"

mlflow.set_tracking_uri("https://03be178ef694-10-244-6-58-30500.spch.r.killercoda.com/")
mlflow.set_experiment("TodoClassifier")
#mlflow.sklearn.autolog()
print(f"Tracking URI: {mlflow.get_tracking_uri()}")
print(f"Registry URI: {mlflow.get_registry_uri()}")

df = pd.read_csv('data.csv')
X_train, X_test, y_train, y_test = train_test_split(df['Task'], df['Category'], test_size=0.35, random_state=19)


with mlflow.start_run():
    model = Pipeline([
        ('tfidf', TfidfVectorizer()),
        ('clf', LinearSVC())
    ])
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    mlflow.log_artifact("test.txt")
    acc = accuracy_score(y_test, y_pred)
    precision, recall, f1, _ = precision_recall_fscore_support(y_test, y_pred, average='weighted')
    mlflow.log_metric("accuracy", acc)
    mlflow.log_metric("f1_score", f1)
    mlflow.sklearn.log_model(sk_model=model, artifact_path="model", registered_model_name="TodoClassifier" )