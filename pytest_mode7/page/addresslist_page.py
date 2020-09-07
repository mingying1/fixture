"""
通讯录页:添加联系人

"""
from appium.webdriver.common.mobileby import MobileBy

from pytest_mode7.page.base_page import BasePage
from pytest_mode7.page.department_search_page import DepartmentSearch


class AddressListPage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver
    # 添加联系人
    addmemeber_text = "添加成员"
    search_element = (MobileBy.ID, 'com.tencent.wework:id/hvn')

    def add_memeber(self):
        self.find_by_scroll_and_click(self.addmemeber_text)
        # self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
        #                          'new UiScrollable(new UiSelector()'
        #                          '.scrollable(true).instance(0))'
        #                          '.scrollIntoView(new UiSelector()'
        #                          '.text("添加成员").instance(0));').click()

        from pytest_mode7.page.memeber_invite_page import MemberInvitePage
        return MemberInvitePage(self.driver)

    def search_click(self):
        self.find_and_click(self.search_element)

        return DepartmentSearch(self.driver)
