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


def test_upload_picture_with_base64_encoded_file(client):
    import base64

    with open("tests/images/books1.jpg", "rb") as file:
        encoded_string = base64.b64encode(file.read()).decode("utf-8")
        data = {"picture": encoded_string}
        response = client.post("/upload", json={"picture": encoded_string})
        assert response.status_code == 200


def test_upload_picture_with_base64_encoded_fil_and_get_some_results(client):
    import base64

    with open("tests/images/books1.jpg", "rb") as file:
        encoded_string = base64.b64encode(file.read()).decode("utf-8")
        data = {"picture": encoded_string}
        response = client.post("/upload", json={"picture": encoded_string})
        assert response.status_code == 200
        assert len(response.json) > 0
