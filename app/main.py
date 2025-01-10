from fastapi import FastAPI
from app.api.v1.routes import books
from app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    version="1.0.0"
)

app.include_router(books.router, prefix="/api/v1/books", tags=["Books"])