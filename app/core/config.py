from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    PROJECT_NAME: str = "books tersea coding challenge"
    DATABASE_URL: str = os.environ["DATABASE_URL"]

settings = Settings()