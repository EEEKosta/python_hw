from module_4_2_task_1.conftest import faker, create_booking
from module_4_2_task_1.constant import BASE_URL


class TestBooking:

    def test_create_booking(self, auth_session, booking_data):
        create_booking = auth_session.post(f"{BASE_URL}/booking", json=booking_data)
        assert create_booking.status_code == 200, "Ошибка при создании брони"
        booking_id = create_booking.json().get("bookingid")
        assert booking_id is not None, "id брони не найден в ответе"

        assert create_booking.json()["booking"]["firstname"] == booking_data["firstname"], "Имя не совпадает"
        assert create_booking.json()["booking"]["totalprice"] == booking_data["totalprice"], "Стоимость не совпадает"

        get_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_booking.status_code == 200, "Бронь не найдена"
        assert get_booking.json()["lastname"] == booking_data["lastname"], "Фамилия не совпадает"

        deleted_booking = auth_session.delete(f"{BASE_URL}/booking/{booking_id}")
        assert deleted_booking.status_code == 201, "Бронь не найдена"

        get_booking = auth_session.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_booking.status_code == 404, "Бронь не удалена"

    # проверка обновления брони
    def test_update_booking(self, auth_session, booking_data, booking_data_2):
        create_booking = auth_session.post(f"{BASE_URL}/booking", json=booking_data)
        assert create_booking.status_code == 200, "Ошибка при создании брони"

        booking_id = create_booking.json().get("bookingid")
        assert booking_id is not None, "id брони не найден в ответе"

        update_booking = auth_session.put(f"{BASE_URL}/booking/{booking_id}", json=booking_data_2)
        assert create_booking.json()["booking"]["firstname"] != update_booking.json()["firstname"]

    # проверка того что список additionalneeds добавилс
    def test_update_booking_additionalneeds(self, auth_session, booking_data, booking_data_2):
        create_booking = auth_session.post(f"{BASE_URL}/booking", json=booking_data)
        assert create_booking.status_code == 200, "Ошибка при создании брони"

        boking_id = create_booking.json().get("bookingid")
        assert boking_id is not None, "id брони не найден в ответе"

        update_booking = auth_session.put(f"{BASE_URL}/booking/{boking_id}", json=booking_data_2)
        assert update_booking.json()["additionalneeds"] is not None, "Список отсутствует"

    # проверка частичного изменения, одного поля
    def test_partial_update_booking(self, auth_session, create_booking, booking_data, booking_data_2):
        booking = create_booking
        booking_id = booking.get("bookingid")
        assert booking_id is not None, "id брони не найден в ответе"

        update_booking = auth_session.patch(f"{BASE_URL}/booking/{booking_id}", json={"firstname": faker.first_name()})
        assert booking["booking"].get('firstname') != update_booking.json().get("firstname")

    # проверка того что созданая бронь есть в общем списке
    def test_get_booking(self, auth_session, booking_data):
        create_booking = auth_session.post(f"{BASE_URL}/booking", json=booking_data)
        assert create_booking.status_code == 200, "Ошибка при создании брони"

        booking_id = create_booking.json().get("bookingid")
        get_booking = auth_session.get(f"{BASE_URL}/booking")
        assert any(item["bookingid"] == booking_id for item in get_booking.json()), "Бронь не найдена"

    # проверка json schema
    def test_get_booking_json(self, auth_session, booking_data):
        response = auth_session.get(f"{BASE_URL}/booking")
        assert response.status_code == 200, "Ошибка при получении списка броней"

        data = response.json()
        assert isinstance(data, list), "Ответ не является списком"

        for item in data:
            assert isinstance(item, dict), "Элемент должен быть словарем"
            assert "bookingid" in item, "Нет ключа 'bookingid'"
            assert isinstance(item["bookingid"], int), "bookingid должен быть числом"
