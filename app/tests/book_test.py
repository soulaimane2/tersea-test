from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# def test_add_book_no_data():
#     response = client.post("/api/v1/books/", json={})
#     assert response.status_code == 422

# def test_add_book_no_optional_data_desc():
#     dummy_data = {
#         "title": "soulaimane is testing",
#         "author": "string",
#         "published_year": 0,
#     }
#     response = client.post("/api/v1/books/", json=dummy_data)
#     assert response.status_code == 200


# def test_add_book_success():
#     dummy_data = {
#         "title": "soulaimane is testing",
#         "author": "string",
#         "published_year": 0,
#         "description": "string"
#     }
#     response = client.post("/api/v1/books/", json=dummy_data)
#     assert response.status_code == 200


# def test_list_books():
#     response = client.get("/api/v1/books/", headers={"X-Token": "coneofsilence"})
#     assert response.status_code == 200

def test_get_book_by_id():
    dummy_data = {
        "title": "soulaimane is testing to be found",
        "author": "string",
        "published_year": 0,
        "description": "string"
    }
    addBook = client.post("/api/v1/books/", json=dummy_data)
    response = client.get("/api/v1/books/"+addBook.json()["id"])
    assert response.status_code == 200