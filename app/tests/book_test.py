from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_add_book_no_data():
    response = client.post("/api/v1/books/", json={})
    assert response.status_code == 422

def test_add_book_no_optional_data_desc():
    dummy_data = {
        "title": "soulaimane is testing",
        "author": "string",
        "published_year": 0,
    }
    response = client.post("/api/v1/books/", json=dummy_data)
    assert response.status_code == 200


def test_add_book_success():
    dummy_data = {
        "title": "soulaimane is testing",
        "author": "string",
        "published_year": 0,
        "description": "string"
    }
    response = client.post("/api/v1/books/", json=dummy_data)
    assert response.status_code == 200


def test_list_books():
    response = client.get("/api/v1/books/", headers={"X-Token": "coneofsilence"})
    assert response.status_code == 200

def test_get_book_by_id():
    response = client.get("/api/v1/books/67808c9c35e60976b9ae6b0e")
    assert response.status_code == 200


def test_update_book_by_id():
    dummy_data = {
        "title": "soulaimane is updated",
        "author": "string",
        "published_year": 0,
        "description": "string"
    }
    response = client.put("/api/v1/books/67808c9c35e60976b9ae6b0e", json=dummy_data)
    assert response.status_code == 200
    assert response.json().get("msg") == "Book updated"

def test_update_book_by_id_without_desc():
    dummy_data = {
        "title": "soulaimane is updated without desc",
        "author": "string",
        "published_year": 0,
    }
    response = client.put("/api/v1/books/67808c9c35e60976b9ae6b0e", json=dummy_data)
    assert response.status_code == 200
    assert response.json().get("msg") == "Book updated"


def test_delete_book_by_id():
    dummy_data = {
        "title": "soulaimane is updated",
        "author": "string",
        "published_year": 0,
        "description": "string"
    }
    response = client.put("/api/v1/books/67808c9c35e60976b9ae6b0e", json=dummy_data)
    assert response.status_code == 200
    assert response.json().get("msg") == "Book updated"