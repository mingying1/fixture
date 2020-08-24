# 加入部门类
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote import switch_to

from pytest_mode4.test_project.pages.base import Base


class AdddepartmentPage(Base):
    _js_create_dropdown = (By.CSS_SELECTOR, ".js_create_dropdown")
    _js_create_party = (By.CSS_SELECTOR, ".js_create_party")
    _inputDlg_item = (By.CSS_SELECTOR, ".inputDlg_item input:nth-child(2)")
    _inputDlg_item1 = (By.CSS_SELECTOR, ".inputDlg_item a:nth-child(2)")
    _jstree = (By.CSS_SELECTOR, ".jstree-anchor")
    _submit = (By.XPATH, "//*[@d_ck='submit']")
    _cancel = (By.CSS_SELECTOR, "[d_ck='cancel']")

    # 定义添加部门方法
    def add_department(self, name):
        # self.driver = webdriver.Chrome()
        self.find(*self._js_create_dropdown).click()

        self.find(*self._js_create_party).click()

        self.find(*self._inputDlg_item).send_keys(name)

        self.find(*self._inputDlg_item1).click()

        self.finds(*self._jstree)[4].click()
        sleep(3)

        return self

    # 定义保存添加部门的方法
    def save_department(self):
        self.find(*self._submit).click()
        from pytest_mode4.test_project.pages.department1_page import Department1
        return Department1(self.driver)

    def cancel_department(self):
        self.find(*self._cancel).click()
        from pytest_mode4.test_project.pages.contact_page import ContactPage
        return ContactPage(self.driver)
