"""
添加成员页面

"""
from appium.webdriver.common.mobileby import MobileBy

from pytest_mode7.page.base_page import BasePage
from pytest_mode7.page.contcat_edit_page import ContactEditPage


class MemberInvitePage(BasePage):
    addmemeber_element = (MobileBy.XPATH, '//*[@text="手动输入添加"]')

    # def __init__(self, driver):
    #     self.driver = driver
    # 手动添加成员
    def addcontact_menual(self):
        # self.driver.find_element(MobileBy.XPATH, '//*[@text="手动输入添加"]').click()
        self.find_and_click(self.addmemeber_element)
        return ContactEditPage(self.driver)

    def get_toast(self):
        # mytoast = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        mytoast = self.gettoast_text()
        return mytoast
