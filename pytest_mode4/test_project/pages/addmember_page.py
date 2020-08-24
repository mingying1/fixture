# 添加联系人类
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from pytest_mode4.test_project.pages.base import Base


class AddmemberPage(Base):
    # 私有化元素
    _username = (By.ID, "username")
    _memberAdd_acctid = (By.ID, "memberAdd_acctid")
    _memberAdd_phone = (By.ID, "memberAdd_phone")
    _js_btn_save = (By.CSS_SELECTOR, ".js_btn_save")
    _js_btn_cancel = (By.CSS_SELECTOR, ".js_btn_cancel")
    _cancel = (By.XPATH, "//*[@node-type='cancel']")

    # 定义添加成员方法
    def addmembers(self, name, acctid, phone):
        self.find(*self._username).send_keys(name)
        self.find(*self._memberAdd_acctid).send_keys(acctid)
        self.find(*self._memberAdd_phone).send_keys(phone)
        return self

    def save_member(self):
        self.find(*self._js_btn_save).click()
        from pytest_mode4.test_project.pages.contact_page import ContactPage
        return ContactPage(self.driver)

    def cancel_memeber(self):
        self.find(*self._js_btn_cancel).click()
        sleep(3)
        self.find(*self._cancel).click()
        sleep(3)

        from pytest_mode4.test_project.pages.contact_page import ContactPage
        return ContactPage(self.driver)
