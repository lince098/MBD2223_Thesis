FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY .  .

EXPOSE 8501

ENV BACKEND_HOST="http://localhost"
ENV BACKEND_PORT=8000

ENTRYPOINT streamlit run ./Code_Comparison.py