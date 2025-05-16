import pytest
import requests
from module_4_1.constant import HEADERS, BASE_URL
from faker import Faker

faker = Faker()
@pytest.fixture(scope='session')
def auth_session():
    session = requests.Session()
    session.headers.update(HEADERS)

    response = requests.post(f"{BASE_URL}/auth", headers=HEADERS, json={"username": "admin","password": "password123"})
    assert response.status_code == 200, "Ошибка авторизации"
    token = response.json().get("token")
    # token = response.json()["token"] - если так извлечь токен, то в случае его отсутствия мы упадем по KeyError
    assert token is not None, "Token not found"

    session.headers.update({"Cookie": f"token={token}"})
    return session

@pytest.fixture(scope='function')
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