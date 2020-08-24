import pytest

from pytest_mode4.test_project.pages.main_page import MainPage
class TestAddmenber:
    def setup_class(self):
        self.main = MainPage()

    def teardown_class(self):
        self.main.driver.quit()

    # 定义主页添加成员
    def test_addmenber(self):
        # self.main = MainPage()
        # 通过主页进入添加成员页面,添加成员,保存成员,获取成员名称
        namelist = self.main.go_to_addmember().addmembers("哈哈4", "1244", "12345678301").save_member().get_memeber_list()
        assert "哈哈4" in namelist

    def test_addmenber_fail(self):
        namelist1 = self.main.go_to_addmember().addmembers("哈哈2", "1234",
                                                           "12345678901").cancel_memeber().get_memeber_list()
        assert "哈哈2" not in namelist1

    # 定义通讯录添加成员
    def test_contact_member(self):
        # self.main = MainPage()
        # 通过主页进入通讯录,进入添加成员页面添加成员
        self.main.go_to_contact().go_to_addmember().addmembers()

    # 定义导入通讯录
    def test_import_contact(self):
        # self.main = MainPage()
        # 通过主页进入导入通讯录页面,导入通讯录
        self.main.go_to_importcontacts().import_contact()

    # 定义添加部门
    def test_add_department(self):
        # 1,从首页进入通讯录  2,通讯录进入添加部门  3,添加部门,保存部门
        list = self.main.go_to_contact().go_to_adddepartment().add_department("1213").save_department().get_name
        print(list)
        assert "123" in list

    def test_add_department_fail(self):
        list = self.main.go_to_contact().go_to_adddepartment().add_department("销售").cancel_department().get_listname()

        assert "销售" not in list
