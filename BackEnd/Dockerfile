FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip & pip install --no-cache-dir -r requirements.txt

COPY .  .

EXPOSE 8000

ENV QDRANT_CLUSTER_HOST="localhost"
ENV QDRANT_CLUSTER_PORT=6333

ENTRYPOINT uvicorn main:app --host 0.0.0.0