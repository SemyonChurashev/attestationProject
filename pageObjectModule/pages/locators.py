from selenium.webdriver.common.by import By


class MainPageLocators:
    PARCEL_SEARCH_INPUT = (By.CLASS_NAME, "search__field")
    PARCEL_SEARCH_BUTTON = (By.XPATH, "//div[@class='search__icon']")
    TRACKING_TITLE = (By.CLASS_NAME, "tracking__title")
    TRACKING_INPUT = (By.CLASS_NAME, "tracking__input")
