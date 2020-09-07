from pytest_mode7.page.app import App


class TestContact:
    def setup(self):
        # 应用的启动
        self.app = App()
        self.main = self.app.start().goto_main()

    def teardown(self):
        # 应用的关闭
        self.app.stop()

    def test_addcontact(self):
        name = "测试1"
        gender = "男"
        phonenum = "13452732563"
        # 主页去到通讯录页,添加成员,手动输入添加,添加姓名,性别,电话,点击保存
        mypage = self.main.goto_addresslist().add_memeber().addcontact_menual().edit_name(name) \
            .edit_gender(gender).edit_phonenum(phonenum).click_save()
        # 获取toast
        mytoast = mypage.get_toast()

        assert "添加成功" == mytoast

    def test_delcontact(self):
        name = "测试1"
        # 主页-通讯录-搜索-输入名字-点击三个点-点击编辑成员-点击删除
        searchpage = self.main.goto_addresslist().search_click().search_send_name(name) \
            .detail_click().setting_contact().del_contact()
        list1 = searchpage.search_result_list()
        assert name not in list1
