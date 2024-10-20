"""
Задание № 2
Написать функцию, которая будет принимать строку (ФИО пользователя)
и выводить текст "Привет $имя_пользователя! В твоем ФИО $кол-во букв!".
"""
inputFio = input('Введите своё ФИО:\n')


def print_fio(rawinput: str):
    alphaсount = len([i for i in rawinput if i.isalpha()])
    print(f"Привет {rawinput}! В твоём ФИО {alphaсount} букв!")


print_fio(inputFio)
