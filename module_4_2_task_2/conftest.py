import pytest
import requests
from requests import Session

from module_4_2_task_2.constant import HEADERS, BASE_URL
from faker import Faker

faker = Faker()


@pytest.fixture(scope="session")
def auth_session():
    session = requests.Session()
    session.headers.update(HEADERS)

    response = requests.post(f"{BASE_URL}/auth", headers=HEADERS, json={"username": "admin", "password": "password123"})
    assert response.status_code == 200, "Ошибка авторизации"
    token = response.json().get("token")
    # token = response.json()["token"] - если так извлечь токен, то в случае его отсутствия мы упадем по KeyError
    assert token is not None, "Token not found"

    session.headers.update({"Cookie": f"token={token}"})
    return session


@pytest.fixture(scope="function")
def booking_data():
    return {
        "firstname": faker.first_name(),
        "lastname": faker.last_name(),
        "totalprice": faker.random_int(min=100, max=100000),
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
    }


@pytest.fixture(scope="function")
def booking_data_2():
    return {
        "firstname": faker.first_name(),
        "lastname": faker.last_name(),
        "totalprice": faker.random_int(min=100, max=100000),
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": [
            "Breakfast",
            "lunch"
        ]
    }


@pytest.fixture(scope="function")
def create_booking(auth_session, booking_data):
    response = Session().post(f"{BASE_URL}/booking", json=booking_data)
    assert response.status_code == 200, "Ошибка создания брони"

    booking_id = response.json().get("bookingid")
    assert booking_id is not None, "id брони не найден в ответе"

    return response
