from appium.webdriver.common.mobileby import MobileBy

from pytest_mode7.page.base_page import BasePage
from pytest_mode7.page.contact_edit import ContactEdit

"""
个人信息页:点击编辑成员
"""


class DetailSetting(BasePage):
    setting_element = (MobileBy.XPATH, '//*[@text="编辑成员"]')

    def setting_contact(self):
        self.find_and_click(self.setting_element)
        # self.driver.find_element(MobileBy.XPATH, '//*[@text="编辑成员"]').click()
        return ContactEdit(self.driver)
