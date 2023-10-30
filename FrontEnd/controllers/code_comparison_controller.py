from pydantic_settings import BaseSettings
import requests
from streamlit.runtime.uploaded_file_manager import UploadedFile


class Settings(BaseSettings):
    BACKEND_HOST: str = "http://localhost"
    BACKEND_PORT: int = 8000


settings = Settings()
BACKEND_URL = settings.BACKEND_HOST + ":" + str(settings.BACKEND_PORT)
ENDPOINT = BACKEND_URL + "/v1/compareCodeFile"


def search_code(code: UploadedFile, limit: int):
    queried_endpoint = ENDPOINT
    response = requests.post(
        queried_endpoint,
        files={"file": (code.name, code.read())},
        data={"limit": limit},
    )

    return response.json()["message"]
