import json

import yaml
from jsonpath import jsonpath
from jsonschema import validate

from pytest_mode8.api.tag import Tag


class TestTag():

    def setup_class(self):
        # 实例化tag
        self.tag = Tag()
        # 定义读取config文件
        config_infor = yaml.safe_load(open("config.yaml"))
        # 调用tag中获取token的方法,从config文件中取出相对应的secret值
        self.tag.get_token(config_infor["token"]["corp_secret"])

    def test_create_tag(self):
        # 调用tag 中的创建tag
        self.tag.create_tag()
        # 获取tag的列表
        list1 = self.tag.get_tag_list()
        # print(list1)
        # #jsonpath后面要有json的返回体,和表达式
        # name = jsonpath(list1, "$..tagname")
        # print(name)
        # #断言UI这个名称在name中
        # assert "UI" in name
        # 读取jsonschema文件
        get_list_shchema = json.load(open("./json_schema/get_list_schema.json"))
        # 使用validate校验
        validate(list1, get_list_shchema)

    def test_update_tag(self):
        # 调用tag 中的更新tag
        self.tag.update_tag(12)
        list1 = self.tag.get_tag_list()
        name = jsonpath(list1, "$..tagname")
        assert "UI design" in name

    def test_delete_tag(self):
        # 调用tag 中的删除tag
        self.tag.delete_tag(12)
        list1 = self.tag.get_tag_list()
        print(list1)
        tag_id = jsonpath(list1, "$..taglist")
        print(tag_id)
        assert 12 not in tag_id
