"""
Задание № 1
Написать тестовую функцию проверки возраста
- на вход принимает возраст (строкой!),
если возраст > 18 выводит "Доступ разрешен", если возраст < 18 выводит "Доступ запрещен".
 Добавить в функцию обработку некорректных возрастов типа 1000 и спецсимволов/букв
- выводить сообщение "Неверно указаны входные данные $входные_данные".
Параметризовать функцию
"""

import pytest


def validate_age(age):
    if age.isnumeric() and int(age) < 100:
        return int(age)
    else:
        return False


@pytest.mark.parametrize('userage', ["165", "test", "99", "18", "12", "34FG", "45"])
def test_age(userage):
    age = validate_age(userage)
    if age is False:
        assert False, f"Неверно указаны входные данные '{userage}'"
    assert age > 18, "Доступ запрещен"
