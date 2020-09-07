from appium.webdriver.common.mobileby import MobileBy

from pytest_mode7.page.base_page import BasePage
from pytest_mode7.page.datail_setting_page import DetailSetting

"""
个人信息页:点击三个点
"""


class DetailPage(BasePage):
    detail_element = (MobileBy.ID, 'com.tencent.wework:id/hvd')

    def detail_click(self):
        self.find_and_click(self.detail_element)
        # self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/hvd').click()
        return DetailSetting(self.driver)
