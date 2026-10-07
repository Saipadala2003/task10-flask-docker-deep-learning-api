# Task 10 - Containerizing Flask Deep Learning API

This project packages the Flask-based MNIST CNN inference API developed in the previous Flask/Streamlit task into a Docker image for local deployment.

## Project files

- `flask_api.py` - Flask REST API with `/`, `/health`, and `/predict` endpoints.
- `deep_learning_model.h5` - compatible trained CNN model from the previous task (add this file before building).
- `requirements.txt` - pinned runtime dependencies.
- `Dockerfile` - optimized two-stage Docker build using Python 3.12-slim.
- `.dockerignore` - reduces the Docker build context.
- `test_api.py` - basic HTTP smoke test for `/` and `/health`.
- `report/Task_10_Containerizing_Flask_Deep_Learning_API_Deployment_Report.pdf` - deployment report.

## Prerequisite

Place the trained model from the previous task in this folder using the exact filename:

`deep_learning_model.h5`

The image is intentionally not generated or substituted in this package. Prediction must use the same model and preprocessing convention used by the previous task.

## Build

```powershell
docker build -t task10-flask-dl-api .
```

## Run

```powershell
docker run --rm --name task10-flask-dl-api -p 5000:5000 task10-flask-dl-api
```

## Verify

Open in a browser:

- `http://127.0.0.1:5000/`
- `http://127.0.0.1:5000/health`

Expected health response includes `"status": "healthy"` and `"model_loaded": true`.

For prediction, send a multipart upload under the form field `file`:

```powershell
curl.exe -X POST "http://127.0.0.1:5000/predict" -F "file=@7.png"
```

## Docker inspection

```powershell
docker images task10-flask-dl-api
docker ps
docker inspect task10-flask-dl-api
docker stats task10-flask-dl-api --no-stream
docker history task10-flask-dl-api
```

## Optimization practices used

1. `python:3.12-slim` is used instead of a full Python image.
2. Dependencies are installed once into a virtual environment in a builder stage.
3. `pip --no-cache-dir` avoids retaining package caches.
4. `.dockerignore` removes Git metadata, Python caches, reports, screenshots, and local environments from the build context.
5. The runtime container includes only the runtime OS library, prepared virtual environment, model, and API source.
6. Gunicorn is used as the container entrypoint instead of Flask's development server.
7. The container runs as a non-root user.
8. A Docker `HEALTHCHECK` calls `/health`.
9. One Gunicorn worker is used by default because each ML worker can load its own model copy into memory.

## Important compatibility note

Keep the model preprocessing identical to the training pipeline. The supplied Flask implementation converts the uploaded image to grayscale, resizes/fits it to 28 x 28, normalizes pixels to [0, 1], and adapts to common Keras input shapes.
