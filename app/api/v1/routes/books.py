from fastapi import APIRouter, HTTPException
from app.services.book_services import (
    get_all_books,
    get_book_by_id,
    add_book,
    update_book,
    delete_book
)
from app.db.models.book import Book

router = APIRouter()

@router.get("/")
async def list_books():
    return await get_all_books()

@router.get("/{book_id}")
async def retrieve_book(book_id: str):
    book = await get_book_by_id(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.post("/")
async def create_book(book: Book):
    return await add_book(book)

@router.put("/{book_id}")
async def modify_book(book_id: str, book: Book):
    return await update_book(book_id, book)

@router.delete("/{book_id}")
async def remove_book(book_id: str):
    return await delete_book(book_id)
