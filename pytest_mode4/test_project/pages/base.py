from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver


class Base:
    base_url = ""

    def __init__(self, driver_base=None):
        # 避免driver重复实例化
        if driver_base is None:
            option = Options()
            option.debugger_address = '127.0.0.1:9222'
            self.driver = webdriver.Chrome(options=option)
            self.driver.maximize_window()

        else:
            self.driver: WebDriver = driver_base
        if self.base_url != "":
            self.driver.get(self.base_url)

        self.driver.implicitly_wait(5)

    def find(self, by, value):
        return self.driver.find_element(by, value)

    def finds(self, by, value):
        return self.driver.find_elements(by, value)
