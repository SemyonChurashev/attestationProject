import time

from pageObjectModule.pages.base_page import BasePage
from pageObjectModule.pages.locators import MainPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import NoSuchElementException, TimeoutException


class MainPage(BasePage):
    def input_text(self, text):
        input_parcel = self.browser.find_element(*MainPageLocators.PARCEL_SEARCH_INPUT)
        input_parcel.send_keys(text)
        time.sleep(2)
        return input_parcel.get_attribute('value')

    def clear_text(self):
        input_parcel = self.browser.find_element(*MainPageLocators.PARCEL_SEARCH_INPUT)
        input_parcel.clear()
        time.sleep(2)
        return input_parcel.get_attribute('value')

    def find_parcel_button_and_click(self):
        button = self.browser.find_element(*MainPageLocators.PARCEL_SEARCH_BUTTON)
        button.click()

    def wait_for_tracking_title(self):
        try:
            WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located
                                                  (MainPageLocators.TRACKING_TITLE))
        except TimeoutException:
            return False
        return True

    def find_tracking_input(self):
        try:
            self.browser.find_element(*MainPageLocators.TRACKING_INPUT)
        except NoSuchElementException:
            return False
        return True
