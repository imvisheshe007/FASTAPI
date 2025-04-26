from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "ML GenAI API"
    debug: bool = True
    openai_api_key: str
    model_name: str = "gpt2"

    class Config:
        OPENAI_API_KEY=sk-xxxxx
        MODEL_NAME=gpt2 # Load variables from .env

settings = Settings()
