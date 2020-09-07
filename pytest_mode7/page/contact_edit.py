from appium.webdriver.common.mobileby import MobileBy

from pytest_mode7.page.base_page import BasePage

"""
个人编辑页:删除成员
"""


class ContactEdit(BasePage):
    del_element = (MobileBy.XPATH, '//*[@text="删除成员"]')
    define_element = (MobileBy.XPATH, '//*[@text="确定"]')

    def del_contact(self):
        self.find_and_click(self.del_element)
        self.find_and_click(self.define_element)
        # self.driver.find_element(MobileBy.XPATH, '//*[@text="删除成员"]').click()
        # self.driver.find_element(MobileBy.XPATH, '//*[@text="确定"]').click()
        from pytest_mode7.page.department_search_page import DepartmentSearch
        return DepartmentSearch(self.driver)
