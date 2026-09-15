import pytest

from app import app, db


@pytest.fixture
def client():
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"

    with app.app_context():
        db.drop_all()
        db.create_all()

        with app.test_client() as client:
            yield client

        db.session.remove()
        db.drop_all()


def test_home_page(client):
    response = client.get("/")

    assert response.status_code == 200
    assert b"Social Feed" in response.data


def test_create_post(client):
    response = client.post(
        "/create",
        data={
            "username": "Test User",
            "content": "Testing the Social Media Feed.",
        },
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert b"Testing the Social Media Feed." in response.data


def test_empty_post_rejected(client):
    response = client.post(
        "/create",
        data={
            "username": "",
            "content": "",
        },
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert b"Please enter both your name and a post." in response.data