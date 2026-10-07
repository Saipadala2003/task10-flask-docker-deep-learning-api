# Task 10 - Containerizing Flask Deep Learning API

This repository contains the completed Task 10 practical for packaging a Flask-based MNIST CNN inference API into a Docker container and validating the deployment locally.

## Objectives
- Create a Dockerfile for the Flask deep learning API.
- Build a Docker image.
- Run the API inside a Docker container.
- Verify the root, health, and prediction endpoints.
- Inspect container resource usage and image layers.
- Apply Docker image optimization and runtime practices.

## Project Structure
```text
task10-flask-docker-deep-learning-api/
├── Dockerfile
├── flask_api.py
├── requirements.txt
├── test_api.py
├── docker-compose.yml
├── .dockerignore
├── DOCKER_COMMANDS.txt
├── README.md
├── screenshots/
│   ├── 01_docker_build.png
│   ├── 02_container_prediction.png
│   ├── 03_health_check.png
│   ├── 04_docker_stats.png
│   ├── 05_docker_image_size.png
│   ├── 06_docker_history.png
│   └── 07_api_validation.png
└── report/
    └── Task_10_Final_Containerizing_Flask_Deep_Learning_API_Report.pdf
```

## Model Prerequisite
Place the compatible trained model from the previous Flask/MNIST task in the project root with the exact filename:

`deep_learning_model.h5`

The Dockerfile copies that model into the image. The model is intentionally not substituted or fabricated; prediction results must use the actual trained model.

## Build
```powershell
docker build --pull -t task10-flask-dl-api .
```

## Run
```powershell
docker run --rm --name task10-flask-dl-api -p 5000:5000 task10-flask-dl-api
```

The container listens on port 5000 and uses Gunicorn for the container runtime.

## API Endpoints
### Root
```text
GET http://127.0.0.1:5000/
```

### Health
```text
GET http://127.0.0.1:5000/health
```

Expected health response includes:
```json
{"success":true,"status":"healthy","model_loaded":true}
```

### Prediction
```powershell
curl.exe -X POST "http://127.0.0.1:5000/predict" -F "file=@7.png"
```

The endpoint returns the predicted digit, confidence, and class probabilities.

## Validation Evidence
The completed local validation recorded:
- Docker image built successfully as `task10-flask-dl-api:latest`.
- Container ran with port mapping `5000:5000`.
- `/health` returned HTTP 200 with `model_loaded=true`.
- `/predict` returned a successful prediction for the supplied digit image.
- `docker stats` was used to record CPU and memory usage.
- `docker images` was used to record image disk/content size.
- `docker history` was used to inspect image layers.
- `test_api.py` confirmed successful `GET /` and `GET /health` responses.

## Optimization Practices
- Python 3.12 slim base image.
- Multi-stage build with a dedicated virtual environment.
- `pip --no-cache-dir`.
- Minimal runtime OS dependency (`libgomp1`).
- `.dockerignore` to reduce build context.
- Non-root runtime user.
- Docker `HEALTHCHECK`.
- Gunicorn instead of Flask development server.
- One Gunicorn worker by default to avoid unnecessary duplicate model copies in memory.

## Submission
The `report/` directory contains the final deployment report for LMS/trainer review. The `screenshots/` directory is intended for the ordered Docker evidence captured during the practical.

Author: **Saikumar Padala**  
Course: **MSc Artificial Intelligence**
