"""
 Задание № 3
 Распарсить json объект из ответа публичного API
"""
import requests
import random

# 1.Получаем список id, выбираем случайное ID is response data
response = requests.get('https://restful-booker.herokuapp.com/booking')
response_data = response.json()
random_id = response_data[random.randrange(len(response_data))].get('bookingid')

# 2. Находим информацию по полученному id, построчно выводим ключ - значение
response = requests.get('https://restful-booker.herokuapp.com/booking/' + str(random_id))
response_data = response.json()
for key in response_data:
    print(key.upper() + ": " + str(response_data.get(key)))
