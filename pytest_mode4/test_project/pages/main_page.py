from selenium import webdriver
from selenium.webdriver.common.by import By

from pytest_mode4.test_project.pages.addmember_page import AddmemberPage

from pytest_mode4.test_project.pages.base import Base


# 企业微信主页类
class MainPage(Base):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"
    _menu_contacts = (By.ID, "menu_contacts")
    _addmember = (By.CSS_SELECTOR, "[node-type='addmember']")
    _index_service_cnt_itemWrap = (By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(2)")

    # 定义方法去到通讯录页面
    def go_to_contact(self):
        # self.driver = webdriver.Chrome()
        self.driver.get(self._base_url)

        self.find(*self._menu_contacts).click()
        # 对ContactsPage类实例化,表示业务逻辑的转化关系
        from pytest_mode4.test_project.pages.contact_page import ContactPage
        return ContactPage(self.driver)

    # 定义方法去到添加成员页面
    def go_to_addmember(self):
        self.driver.get(self._base_url)

        self.find(*self._addmember).click()

        return AddmemberPage(self.driver)

    # 定义方法去到导入通讯录页面
    def go_to_importcontacts(self):
        self.driver.get(self._base_url)
        self.find(*self._index_service_cnt_itemWrap).click()

        from pytest_mode4.test_project.pages.importcontacts_page import ImportcontactsPage
        return ImportcontactsPage(self.driver)
