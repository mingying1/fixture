"""
去到通讯录页面,去到工作台页面

"""
from appium.webdriver.common.mobileby import MobileBy

from pytest_mode7.page.addresslist_page import AddressListPage
from pytest_mode7.page.base_page import BasePage


class MainPage(BasePage):
    addresslist_element = (MobileBy.XPATH, '//*[@text="通讯录"]')

    # def __init__(self, driver):
    #     self.driver = driver
    # 进入到通讯录
    def goto_addresslist(self):
        # self.driver.find_element(MobileBy.XPATH, '//*[@text="通讯录"]').click()
        self.find_and_click(self.addresslist_element)
        return AddressListPage(self.driver)
