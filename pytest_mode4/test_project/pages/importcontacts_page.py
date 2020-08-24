# 导入通讯录类
from pytest_mode4.test_project.pages.base import Base


class ImportcontactsPage(Base):
    # 定义导入通讯录方法
    def import_contact(self):
        pass

    # 定义返回到通讯录页面
    def back_contacts(self):
        from pytest_mode4.test_project.pages.contact_page import ContactPage
        return ContactPage(self.driver)
