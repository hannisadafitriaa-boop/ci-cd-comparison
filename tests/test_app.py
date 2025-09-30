import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app

def test_hello():
    client = app.test_client()
    response = client.get("/")
    assert response.data == b"Hello, CI/CD!"
