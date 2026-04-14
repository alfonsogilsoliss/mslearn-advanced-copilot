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


def test_monthly_average():
    response = client.get("/countries/Spain/Madrid/January")
    assert response.status_code == 200
    assert "high" in response.json()
    assert "low" in response.json()


def test_monthly_average_country_not_found():
    response = client.get("/countries/Narnia/Madrid/January")
    assert response.status_code == 404
    assert response.json() == {"detail": "Country not found"}


def test_monthly_average_city_not_found():
    response = client.get("/countries/Spain/Barcelona/January")
    assert response.status_code == 404
    assert response.json() == {"detail": "City not found"}


def test_monthly_average_month_not_found():
    response = client.get("/countries/Spain/Madrid/Octember")
    assert response.status_code == 404
    assert response.json() == {"detail": "Month not found"}