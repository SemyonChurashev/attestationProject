
from pageObjectModule.pages.main_page import MainPage
from pageObjectModule.pages.assertions import Assertions
from selenium import webdriver

browser = webdriver.Chrome()
page = MainPage(browser)
try:
    page.open()
    input_case1 = page.input_text("QA-1232332-00-FFXX")
    Assertions.test_input_field_value(input_case1, "QA-1232332-00-FFXX")
    input_case2 = page.clear_text()
    Assertions.test_input_field_value(input_case2, "")
    page.find_parcel_button_and_click()
    result = page.wait_for_tracking_title()
    Assertions.test_is_element_present(result, "Заголовок Где заказ?")
    result = page.find_tracking_input()
    Assertions.test_is_element_present(result, "Ввод поиска для B2CPL посылок")
finally:
    page.close()
