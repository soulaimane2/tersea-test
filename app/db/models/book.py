from pydantic import BaseModel
from typing import Optional

class Book(BaseModel):
    title: str
    author: str
    published_year: int
    description: Optional[str] = None
