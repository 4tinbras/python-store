import unittest

from python_store.main import app
from starlette.testclient import TestClient

client = TestClient(app)

def test_read_main() -> None:
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}