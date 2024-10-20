"""
Написать функцию, которая будет принимать строку (имя пользователя) и выводить текст
"Привет $имя_пользователя! Сегодня $текущая_дата, вчера было $вчерашняя_дата, а завтра будет $завтрашняя_дата".
В датах должны быть - число, месяц, год, день недели и время
"""
from datetime import datetime, timedelta


def print_fio_date(fio: str):
    today = datetime.now()
    yesterday = today - timedelta(days=1)
    tomorrow = today + timedelta(days=1)
    print(f"Привет {fio}!\n"
          f"Сегодня: {today.strftime("%d-%m-%Y %A %I:%M:%S %p")}, "
          f"вчера было {yesterday.strftime("%d-%m-%Y %A %I:%M:%S %p")}, "
          f"а завтра будет {tomorrow.strftime("%d-%m-%Y %A %I:%M:%S %p")}")


print_fio_date(input('Введите свое имя:'))
