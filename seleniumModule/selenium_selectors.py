"""
1.	Находить элемент и выводить его текст
2.	Нажимать кнопки
3.	Вводить текст в поле, проверять, что текст введен
4.	Очищать поле, проверять, что поле очищено
5.	Нажимать кнопку с помощью js.
6.	Локаторы нужно применить разных типов (xpath, css, js)

"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

link = "https://pochtomat.ru/"  # Используется публичный сайт Почтоматов Халва
browser = webdriver.Chrome()
try:
    browser.get(link)
    browser.maximize_window()
    # Поиск элемента и вывод текста
    element = browser.find_element(By.CLASS_NAME, "main__text_head")
    text = element.text
    print(f'Текст элемента: {text}')
    # Проверка, что введен нужный текст
    element = browser.find_element(By.CSS_SELECTOR, '.input__field')
    element.send_keys("Тестовый ввод данных")
    time.sleep(2)
    input_value = element.get_attribute('value')
    assert input_value == "Тестовый ввод данных", f' Ожидалось "Тестовый ввод данных", получено {input_value}'
    # Удаление введенного текста и проверка, что value пустое
    element.clear()
    input_value = element.get_attribute('value')
    assert input_value == "", f'Ожидалось пустое поле, получено {input_value}'
    # Поиск кнопки и нажатие
    button = browser.find_element(By.XPATH, "//div[@class='search__icon']")
    button.click()
    # Ждем перехода на новую страницу, определяем переход по Заголовку Где заказ
    title = (WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "tracking__title")))
    )

finally:
    time.sleep(3)
    browser.quit()
