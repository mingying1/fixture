import pytest
import requests


class TestToken:
    @pytest.mark.parametrize(
        "corp_id, corp_secret, errmsg",
        [("ww25b6fbd2e78cdc72", "GiE9PpMvDFigTgbF8LeVX4ZrPUmXn8qzeXwKxYJ-940", "ok"),
         ("ww25b6fbd2e78cdc72", "", "corpsecret missing"),
         ("", "GiE9PpMvDFigTgbF8LeVX4ZrPUmXn8qzeXwKxYJ-940", "corpid missing")])
    # 定义获取token的方法
    def test_get_token(self, corp_id, corp_secret, errmsg):
        # #定义凭证
        # corpid = "ww25b6fbd2e78cdc72"
        # corpsecret = "GiE9PpMvDFigTgbF8LeVX4ZrPUmXn8qzeXwKxYJ-940"
        # 接口请求地址
        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corp_id}&corpsecret={corp_secret}"

        # 调用requests的get请求,给URL和params传参
        r = requests.get(url=url)
        assert r.json()["errmsg"] == errmsg
