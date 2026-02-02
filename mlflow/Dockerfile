FROM ghcr.io/mlflow/mlflow:latest

RUN pip install --no-cache-dir boto3 botocore

ENTRYPOINT [ "mlflow", "server"]
CMD ["--host", "0.0.0.0", "--serve-artifacts", "--allowed-hosts", \
    "*", \
     "--artifacts-destination", "s3://mlflow-bucket/"]