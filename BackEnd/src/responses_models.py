from pydantic import BaseModel


class CodePayload(BaseModel):
    text: str


class CodeComparisonResponseModel(BaseModel):
    id: int
    version: int
    score: float
    payload: CodePayload
    vector: list[float] | None


class ListCodeComparisonResponseModel(BaseModel):
    message: list[CodeComparisonResponseModel]
