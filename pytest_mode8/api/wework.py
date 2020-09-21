# import requests

from pytest_mode8.api.baseapi import BaseApi


# 继承baseapi,使用requests的二次封装
class WeWork(BaseApi):

    def get_token(self, corp_secret):
        corp_id = "ww25b6fbd2e78cdc72"
        # 因为不同模块可能用到不同的secret值,所以讲这个值放到config文件中,不在此处写死
        # corp_secret = "GiE9PpMvDFigTgbF8LeVX4ZrPUmXn8qzeXwKxYJ-940"
        req = {
            "method": "get",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corp_id}&corpsecret={corp_secret}"
        }
        # 接口请求地址
        # url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corp_id}&corpsecret={corp_secret}"
        #
        # r = requests.get(url=url)

        # 获取token值 调用baseapi的send_requesrts请求
        r = self.sed_requests(req)
        self.token = r.json()["access_token"]
        return self.token
