from pytest_mode8.api.tag import Tag
from pytest_mode8.api.wework import WeWork


class TestTag():

    def setup_class(self):
        # 实例化wework和tag
        wework = WeWork()
        self.tag = Tag()
        self.token = wework.get_token()

    def test_create_tag(self):
        # 调用tag 中的创建tag
        self.tag.create_tag(self.token)
        # 获取tag的列表
        list1 = self.tag.get_tag_list(self.token)
        assert list1["taglist"][0]["tagname"] == "UI"

    def test_update_tag(self):
        # 调用tag 中的更新tag
        self.tag.update_tag(self.token, 12)
        list1 = self.tag.get_tag_list(self.token)
        assert list1["taglist"][0]["tagname"] == "UI design"

    def test_delete_tag(self):
        # 调用tag 中的删除tag
        self.tag.delete_tag(self.token, 12)
        list1 = self.tag.get_tag_list(self.token)
        assert len(list1["taglist"]) == 0
