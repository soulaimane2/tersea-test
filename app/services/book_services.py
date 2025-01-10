from app.db.connection import db
from app.db.models.book import Book
from bson import json_util
import json
from beanie import PydanticObjectId

async def get_all_books():
    books = await db["books"].find().to_list(100)
    response = json.loads(json_util.dumps(books))
    return response

async def get_book_by_id(book_id: PydanticObjectId):
    print(book_id)
    book = await db["books"].find_one({"_id": PydanticObjectId(book_id)})
    print(book)
    response = json.loads(json_util.dumps(book))
    return response

async def add_book(book: Book):
    result = await db["books"].insert_one(book.dict())
    return {"id": str(result.inserted_id)}

async def update_book(book_id: PydanticObjectId, book: Book):
    await db["books"].update_one({"_id": PydanticObjectId(book_id)}, {"$set": book.dict()})
    return {"msg": "Book updated"}

async def delete_book(book_id: PydanticObjectId):
    await db["books"].delete_one({"_id": PydanticObjectId(book_id)})
    return {"msg": "Book deleted"}
