"""
1. Поработать с тестовыми API - использовать GET, POST, PUT, DELETE методы
2. Записать ответы от сервисов в json файл
3. Создать тело запроса из json

Сделал апи клиента для https://restful-booker.herokuapp.com
Метода POST GET PUT записываются в файлы /tmp
"""

import json
import requests
from utils import definitions


class ApiBookingClient:
    BASE_URL = "https://restful-booker.herokuapp.com"
    CREDENTIALS = {"username": "admin", "password": "password123"}
    HEADERS = {"Content-Type": "application/json; charset=utf-8"}
    NEW_BOOKING = {
        "firstname": "Samwell",
        "lastname": "Trader",
        "totalprice": 777,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2023-01-01",
            "checkout": "2024-01-01"
        },
        "additionalneeds": "Dinner"
    }
    CHANGE_BOOKING = {
        "firstname": "Samwell",
        "lastname": "Trader",
        "totalprice": 10000,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-01-01",
            "checkout": "2024-05-05"
        },
        "additionalneeds": "Dinner/VODKA/BEER"
    }
    token: str
    bookingId: int

    @classmethod
    def auth(cls):
        url = cls.BASE_URL + "/auth"
        response = requests.post(url, json=cls.CREDENTIALS, headers=cls.HEADERS)
        cls.token = response.json().get('token')

    @classmethod
    def get_bookings(cls):
        url = f"{cls.BASE_URL}/booking/{cls.bookingId}"
        response = requests.get(url, headers=cls.HEADERS)
        if response.status_code == 200:
            json_data = response.json()
            print(f"Успешно получена информация о бронировании ID {cls.bookingId}\n"
                  f"Данные записаны в файл: {definitions.TMP_DIR / 'BookingInfo.json'}")
            with open(definitions.TMP_DIR / 'BookingInfo.json', 'w+') as f:
                json.dump(json_data, f, indent=4, sort_keys=True)
        else:
            print(f"Не могу получить информацию о бронировании ID {cls.bookingId}\n"
                  f"КОд ответа метода GET {response.status_code}\n"
                  f"Тело ответа {response.text}")

    @classmethod
    def create_booking(cls):
        url = cls.BASE_URL + "/booking"
        response = requests.post(url, json=cls.NEW_BOOKING, headers=cls.HEADERS)
        if response.status_code == 200:
            json_data = response.json()
            cls.bookingId = json_data.get('bookingid')
            print(f"Успешно создано бронирование с ID {cls.bookingId}\n"
                  f"Данные записаны в файл: {definitions.TMP_DIR / 'createdBooking.json'}")
            with open(definitions.TMP_DIR / 'createdBooking.json', 'w+') as f:
                json.dump(json_data, f, indent=4, sort_keys=True)
        else:
            print(f"Не получилось создать бронирование"
                  f"КОд ответа метода POST {response.status_code}")

    @classmethod
    def update_booking(cls):
        url = f"{cls.BASE_URL}/booking/{cls.bookingId}"
        auth_header = {"Cookie": f"token={cls.token}"}
        cls.HEADERS.update(auth_header)
        response = requests.put(url, json=cls.CHANGE_BOOKING, headers=cls.HEADERS)
        if response.status_code == 200:
            json_data = response.json()
            print(f"Успешно обновлены данные о бронировании с ID {cls.bookingId}\n"
                  f"Данные записаны в файл: {definitions.TMP_DIR / 'updatedBooking.json'}")
            with open(definitions.TMP_DIR / 'updatedBooking.json', 'w+') as f:
                json.dump(json_data, f, indent=4, sort_keys=True)
        else:
            print(f"Не получилось обновить информацию о бронировании ID {cls.bookingId}\n"
                  f"КОд ответа метода PUT {response.status_code}")

    @classmethod
    def delete_booking(cls):
        url = f"{cls.BASE_URL}/booking/{cls.bookingId}"
        auth_header = {"Cookie": f"token={cls.token}"}
        cls.HEADERS.update(auth_header)
        response = requests.delete(url, headers=cls.HEADERS)
        if response.status_code == 201:
            print(f"Успешно удалено бронирование с ID {cls.bookingId}\n")
        else:
            print(f"Не получилось удалить бронирование с ID {cls.bookingId}\n"
                  f"КОд ответа метода DELETE {response.status_code}")


# Авторизация в сервисе
ApiBookingClient.auth()
# Создаем бронирование и записываем в файл
ApiBookingClient.create_booking()
# Обновляем бронирование и записываем в файл
ApiBookingClient.update_booking()
# Получаем информацию по ID бронирования и записываем в файл
ApiBookingClient.get_bookings()
# Удаляем бронирование с ID
ApiBookingClient.delete_booking()
# Пытаемся повторно получить информацию об удаленном бронировании
ApiBookingClient.get_bookings()
