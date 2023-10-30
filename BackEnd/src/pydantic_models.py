from pydantic import BaseModel


class CodePayload(BaseModel):
    author: str
    code_language: str
    date: str
    lines_of_code: int
    subject: str
    text: str


class CodeComparisonResponseModel(BaseModel):
    id: int
    version: int
    score: float
    payload: CodePayload
    vector: list[float] | None


class ListCodeComparisonResponseModel(BaseModel):
    message: list[CodeComparisonResponseModel]
