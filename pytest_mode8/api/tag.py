import requests


class Tag():
    # 定义创建tag
    def create_tag(self, token):
        tag_url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/create?access_token={token}"
        tag_data = {
            "tagname": "UI",
            "tagid": 12
        }
        r = requests.post(url=tag_url, json=tag_data)
        return r.json()

    # 定义更新tag
    def update_tag(self, token, id):
        update_tag_url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/update?access_token={token}"
        update_tag_data = {
            "tagid": id,
            "tagname": "UI design"
        }
        r = requests.post(url=update_tag_url, json=update_tag_data)
        return r.json()

    # 定义删除tag
    def delete_tag(self, token, tag_id):
        delete_tag_url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/delete?access_token={token}&tagid={tag_id}"
        r = requests.get(url=delete_tag_url)
        return r.json()

    # 定义获取tag列表
    def get_tag_list(self, token):
        tag_list_url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/list?access_token={token}"
        r = requests.get(url=tag_list_url)
        return r.json()
