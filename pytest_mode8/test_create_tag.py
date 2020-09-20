import requests


class TestTag:

    # 获取token
    def setup(self):
        # 定义凭证
        corpid = "ww25b6fbd2e78cdc72"
        corpsecret = "GiE9PpMvDFigTgbF8LeVX4ZrPUmXn8qzeXwKxYJ-940"
        # 接口请求地址
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        # 定义请求参数
        params = {
            "corpid": corpid,
            "corpsecret": corpsecret
        }
        # 调用requests的get请求,给URL和params传参
        r = requests.get(url=url, params=params)
        # 打印响应数据
        self.token = r.json()["access_token"]

    def test_create_tag(self):
        """
        定义创建标签方法
        获取tag列表信息
        断言创建的标签名称等于taglist里面的tagname
        """
        tag_url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/create?access_token={self.token}"
        tag_data = {
            "tagname": "UI",
            "tagid": 12
        }
        tag_list_url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/list?access_token={self.token}"
        requests.post(url=tag_url, json=tag_data)
        list = requests.get(url=tag_list_url)
        assert list.json()["taglist"][0]["tagname"] == "UI"

    def test_update_tag(self):
        """
               定义更新标签名称方法
               获取tag列表信息
               断言更新的标签名称等于taglist里面的tagname
               """
        update_tag_url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/update?access_token={self.token}"
        update_tag_data = {
            "tagid": 12,
            "tagname": "UI design"
        }
        tag_list_url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/list?access_token={self.token}"
        requests.post(url=update_tag_url, json=update_tag_data)
        list = requests.get(url=tag_list_url)
        assert list.json()["taglist"][0]["tagname"] == "UI design"

    def test_delete_tag(self):
        """
                 定义删除标签名称方法
                 获取tag列表信息
                 断言taglist的长度为0
                 """
        delete_tag_url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/delete?access_token={self.token}&tagid=12"
        tag_list_url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/list?access_token={self.token}"
        requests.get(url=delete_tag_url)
        list = requests.get(url=tag_list_url)
        assert len(list.json()["taglist"]) == 0
