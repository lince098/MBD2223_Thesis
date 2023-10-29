from transformers import pipeline
from fastapi import FastAPI, status, UploadFile, Response
from fastapi.responses import RedirectResponse
from src.constants import OK_MESSAGE, NO_FILE_RETREIVED_MESSAGE
from pydantic_settings import BaseSettings
from qdrant_client import QdrantClient
from src.responses_models import ListCodeComparisonResponseModel
from src.utils import get_number_of_lines


class Settings(BaseSettings):
    QDRANT_CLUSTER_HOST: str = "localhost"
    QDRANT_CLUSTER_PORT: int = 6333


settings = Settings()
qdrant_client = QdrantClient(
    settings.QDRANT_CLUSTER_HOST, port=settings.QDRANT_CLUSTER_PORT
)

app = FastAPI()
pipe = pipeline("feature-extraction", model="microsoft/codebert-base")


@app.get("/")
async def main():
    """Redirect to /docs (relative URL)"""
    return RedirectResponse(url="/docs", status_code=status.HTTP_302_FOUND)


@app.post("/v1/compareCodeFile", status_code=status.HTTP_202_ACCEPTED)
async def compare_code_file(
    file: UploadFile, limit: int, response: Response
) -> ListCodeComparisonResponseModel:
    if not file:
        response.status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
        return {"message": NO_FILE_RETREIVED_MESSAGE}

    content = str(await file.read())

    embbedding = pipe(content, padding=True, truncation=True)[0][0]

    embbedding.append(get_number_of_lines(content))

    result = qdrant_client.search("code", embbedding, limit=limit)

    print(result)

    return {"message": result}


@app.get("/healthz", status_code=status.HTTP_200_OK)
async def healthz():
    return {"message": OK_MESSAGE}


@app.on_event("shutdown")
def on_shutdown():
    qdrant_client.close()
