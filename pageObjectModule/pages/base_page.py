import time


class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.url = "https://pochtomat.ru/"

    def open(self):
        self.browser.get(self.url)
        self.browser.maximize_window()

    def close(self):
        time.sleep(5)
        self.browser.quit()
