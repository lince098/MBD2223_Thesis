import uvicorn
from transformers import pipeline
from typing import Annotated
from fastapi import FastAPI, status, UploadFile, Response, Form, File
from fastapi.responses import RedirectResponse
from src.constants import OK_MESSAGE, NO_FILE_RETREIVED_MESSAGE
from pydantic_settings import BaseSettings
from qdrant_client import QdrantClient
from src.pydantic_models import ListCodeComparisonResponseModel
from src.utils import get_number_of_lines


class Settings(BaseSettings):
    QDRANT_CLUSTER_HOST: str = "localhost"
    QDRANT_CLUSTER_PORT: int = 6333


settings = Settings()
qdrant_client = QdrantClient(
    settings.QDRANT_CLUSTER_HOST, port=settings.QDRANT_CLUSTER_PORT, timeout=200
)

app = FastAPI()
pipe = pipeline("feature-extraction", model="microsoft/codebert-base")


@app.get("/")
async def main():
    """Redirect to /docs (relative URL)"""
    return RedirectResponse(url="/docs", status_code=status.HTTP_302_FOUND)


@app.post("/v1/compareCodeFile", status_code=status.HTTP_202_ACCEPTED)
async def compare_code_file(
    file: Annotated[UploadFile, File()],
    limit: Annotated[str, Form()],
    response: Response,
) -> ListCodeComparisonResponseModel:
    if not file:
        response.status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
        return {"message": NO_FILE_RETREIVED_MESSAGE}

    content = str(await file.read())

    embbedding = pipe(content, padding=True, truncation=True)[0][0]

    result = qdrant_client.search("code", embbedding, limit=limit)

    return {"message": result}


@app.get("/healthz", status_code=status.HTTP_200_OK)
async def healthz():
    return {"message": OK_MESSAGE}


@app.on_event("shutdown")
def on_shutdown():
    qdrant_client.close()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
