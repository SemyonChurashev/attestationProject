"""
Задание № 1
Написать функцию, которая будет считывать указанный файл и выводить его содержимое:
•Построчно
•Целиком
На вход функция должна принимать только название файла
"""
from utils import definitions


def print_file(name: str):
    try:
        file = open(definitions.TMP_DIR / name, 'r', encoding='utf-8')
        print("Вывод файла построчно" + "\n" + "-" * 100)
        for line in file:
            print(line.strip())
        file.seek(0)
        context = file.read()
        print("\nВывод файла целиком" + "\n" + "-" * 100)
        print(context)
        file.close()

    except FileNotFoundError:
        print("Файл не найден")


print_file("test.txt")
