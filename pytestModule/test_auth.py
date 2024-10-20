"""
Задание №2
Создать тест для проверки API (проверка может быть любая).
Написать для него фикстуру, в которой будет храниться HEADERS и BODY запроса.
"""
import requests
import pytest


@pytest.fixture(scope='module')
def authorize():
    url = "https://restful-booker.herokuapp.com/auth"
    credentials = {"username": "admin", "password": "password123"}
    headers = {"Content-Type": "application/json; charset=utf-8"}
    response = requests.post(url, json=credentials, headers=headers)
    return response


def test_httpcode(authorize):
    assert authorize.status_code == 200, (f"Неверный код ответа ожидалось 200, получено "
                                          f"'{authorize.status_code}'")


def test_body(authorize):
    data = authorize.json()
    key = "token"
    assert (key in data), f"В теле ответа не найден ключ {key}"


def test_token(authorize):
    data = authorize.json()
    token = data["token"]
    assert token.isalnum()
