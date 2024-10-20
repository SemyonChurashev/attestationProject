"""
Написать простой скрипт для хрома (можно использовать сайт портала Совкомбанк), он должен:
1.	Заходить на страницу
2.	Выводить url, название вкладки
3.	Обновлять страницу
4.	Выводить cookies
5.	Делать окно браузера максимального размера и минимального размера
6.	Закрывать вкладку и браузер.
"""


from selenium import webdriver
import time

link = "https://pochtomat.ru/"  # Используется публичный сайт Почтоматов Халва
browser = webdriver.Chrome()
try:
    browser.get(link)
    # Получаем текущий URl, печатаем в консоль
    print(f'Текущий URL {browser.current_url}')
    time.sleep(2)
    # Обновить текущую страницу
    browser.refresh()
    # Получение и печать cookies
    cookies = browser.get_cookies()
    for cookie in cookies:
        print(cookie)

    # Делаем окно браузера максимальным и минимальным
    browser.maximize_window()
    time.sleep(2)
    # browser.minimize_window()
    browser.set_window_size(200, 200)
finally:
    time.sleep(3)
    browser.quit()

