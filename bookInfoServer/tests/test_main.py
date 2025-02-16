import pytest
from io import BytesIO
from src.main import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_upload_picture_no_file(client):
    response = client.post("/upload")
    assert response.status_code == 400
    assert b"No picture part in the request" in response.data


def test_upload_picture_with_file(client):
    data = {"picture": (BytesIO(b"my file contents"), "test.jpg")}
    response = client.post("/upload", content_type="multipart/form-data", data=data)
    assert response.status_code == 200
    assert b"bar" in response.data
