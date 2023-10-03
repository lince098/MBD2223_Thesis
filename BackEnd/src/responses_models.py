from pydantic import BaseModel


class CodePayload(BaseModel):
    text: str


class CodeComparisonResponseModel(BaseModel):
    id: int
    version: int
    score: float
    payload: CodePayload
    vector: list[float] | None
