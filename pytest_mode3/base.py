from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Bese():
    def setup(self):
        option = Options()
        # option.debugger_address = '127.0.0.1:9222'
        # self.driver = webdriver.Chrome(options=option)
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardwon(self):
        self.driver.quit()
