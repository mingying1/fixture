import requests


class WeWork():

    def get_token(self):
        corp_id = "ww25b6fbd2e78cdc72"
        corp_secret = "GiE9PpMvDFigTgbF8LeVX4ZrPUmXn8qzeXwKxYJ-940"
        # 接口请求地址
        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corp_id}&corpsecret={corp_secret}"

        r = requests.get(url=url)
        # 获取token值
        return r.json()["access_token"]
