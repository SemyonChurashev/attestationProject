"""
Задание № 2
Конвертировать json объект в словарь
"""
import json
from utils import definitions

try:
    with open(definitions.TMP_DIR / 'payload.json', 'r') as f:
        dict_data = json.load(f)
    print(f"Тип данных {type(dict_data)} \nСодержание словаря {dict_data}")

except (FileNotFoundError, ValueError):
    print("Файл не найден или пустой")
