# MLOps & Microservices Lab

This project is a hands-on laboratory environment designed to practice modern DevOps and MLOps workflows. It simulates a production-grade setup where machine learning models are served through a containerized microservices architecture managed by Kubernetes and deployed in helm chart.

## Tech Stack
- **Orchestration:** Kubernetes/AKS
- **Programming Languages:** C#/.NET, Python/Fastapi
- **Databases:** Postgres PaaS
- **MLOps:** MLflow
- **Storage:** AWS S3

## Architecture Overview

The system follows a microservices pattern with a clear separation of tasks. It includes both clustered and external infra. 

```mermaid
graph TB
    subgraph External_Infrastructure [External Infrastructure]
        MLF[MLflow Server]
        DB[(PostgreSQL Database)]
    end

    subgraph K8s [Kubernetes Cluster]
        FE[Frontend - .NET]
        BE[Backend - FastAPI]
        INF[Inference Service - FastAPI]
        S[(K8s Secrets)] -.->|Inject Credentials| BE

    end

    S3[AWS S3 STORAGE]

    DS[Data Scientist] -->|Uploads Models| MLF
    MLF -->|Store Model Files| S3
    
    FE -->|Requests Data| BE
    BE -->|CRUD| DB
    INF -->|Downloads Model| MLF
    BE -->|Calls for Prediction| INF
```

## TO DO:
- <del>Finish helm deploy</del>
- Add external secrets storage
- Implementation of monitoring (Grafana and Prometheus)
- <del>Create full CICD pipeline for deployment of application<del>
- Create MLOps pipeline for model training and update 

