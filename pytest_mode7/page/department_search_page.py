from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from pytest_mode7.page.base_page import BasePage
from pytest_mode7.page.detail_page import DetailPage

"""
搜索联系人页面:
"""


class DepartmentSearch(BasePage):
    ele1 = (MobileBy.ID, 'com.tencent.wework:id/gfs')
    result_element = (MobileBy.XPATH, "//*[@text='{name}']")
    element = (MobileBy.ID, 'com.tencent.wework: id / hqj')


    # 搜索并输入name
    def search_send_name(self, name):
        # name = "测试1"
        self.find_and_sendkeys(self.ele1, name)
        # self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/hv_').send_keys(name)
        # ele = self.driver.find_elements(MobileBy.XPATH, f"//*[@text='{name}']")

        self.show_wait(self.element)

        # ele = self.driver.find_elements(MobileBy.XPATH, f"//*[@text='{name}']")
        ele = self.finds(self.find_by_text(name))

        beforenum = len(ele)
        if beforenum < 2:
            print("没有可删除的人员")
            return
        ele[1].click()

        return DetailPage(self.driver)

    # 获取name结果列表
    def search_result_list(self):
        # ele1 = self.driver.find_elements(MobileBy.XPATH, "//*[@text='{name}']")
        ele1 = self.finds(self.result_element)
        # list1 = []
        # for name1 in ele1:
        #     list1.append(name1.text)
        return [name1.text for name1 in ele1]
