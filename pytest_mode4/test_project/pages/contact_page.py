# 通讯录类
from selenium.webdriver.common.by import By

from pytest_mode4.test_project.pages.adddepartment_page import AdddepartmentPage

from pytest_mode4.test_project.pages.base import Base
from pytest_mode4.test_project.pages.importcontacts_page import ImportcontactsPage


class ContactPage(Base):
    _member_colRight = (By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
    _jstree1 = (By.CSS_SELECTOR, ".jstree-anchor")

    # 定义去到添加成员页面
    def go_to_addmember(self):
        from pytest_mode4.test_project.pages.addmember_page import AddmemberPage
        return AddmemberPage(self.driver)

    # 定义去到添加部门页面
    def go_to_adddepartment(self):
        return AdddepartmentPage(self.driver)

    # 定义去到导入通讯录页面
    def go_to_importcontacts(self):
        return ImportcontactsPage(self.driver)

    # 定义获取通讯录名字列表
    def get_memeber_list(self):
        ele = self.finds(*self._member_colRight)
        return [name.text for name in ele]

        # list1 = []
        # for name in ele:
        #     list1.append(name.text)
        # print(list1)

    def get_listname(self):
        ele2 = self.finds(*self._jstree1)
        return [name1.text for name1 in ele2]
        # list2 = []
        # for name1 in ele2:
        #     list2.append(name1.text)
        # print(list2)
