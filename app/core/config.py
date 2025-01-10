from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "books tersea coding challenge"
    DATABASE_URL: str = "mongodb://localhost:27017"

settings = Settings()