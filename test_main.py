from main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200


def test_countries():
    response = client.get("/countries")
    assert response.status_code == 200
    assert sorted(response.json()) == ["England", "France", "Germany", "Italy", "Peru", "Portugal", "Spain"]


def test_cities_by_country():
    response = client.get("/countries/Spain")
    assert response.status_code == 200
    assert sorted(response.json()) == ["Madrid", "Sevilla"]


def test_cities_by_country_not_found():
    response = client.get("/countries/Narnia")
    assert response.status_code == 404
    assert response.json() == {"detail": "Country not found"}