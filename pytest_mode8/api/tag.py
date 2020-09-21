from pytest_mode8.api.wework import WeWork


class Tag(WeWork):
    # 定义创建tag
    def create_tag(self):
        tag_url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/create?access_token={self.token}"
        tag_data = {
            "tagname": "UI",
            "tagid": 12
        }
        # 使用req字典
        req = {
            "method": "post",
            "url": tag_url,
            "json": tag_data
        }
        r = self.sed_requests(req)
        # r = requests.post(url=tag_url, json=tag_data)
        return r.json()

    # 定义更新tag
    def update_tag(self, tag_id):
        update_tag_url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/update?access_token={self.token}"
        update_tag_data = {
            "tagid": tag_id,
            "tagname": "UI design"
        }
        # 使用req字典
        req = {
            "method": "post",
            "url": update_tag_url,
            "json": update_tag_data
        }
        r = self.sed_requests(req)
        # r = requests.post(url=update_tag_url, json=update_tag_data)
        return r.json()

    # 定义删除tag
    def delete_tag(self, tag_id):
        delete_tag_url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/delete?access_token={self.token}&tagid={tag_id}"
        # 使用req字典
        req = {
            "method": "get",
            "url": delete_tag_url
        }
        r = self.sed_requests(req)
        # r = requests.get(url=delete_tag_url)
        return r.json()

    # 定义获取tag列表
    def get_tag_list(self):
        tag_list_url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/list?access_token={self.token}"
        # 使用req字典
        req = {
            "method": "get",
            "url": tag_list_url
        }
        r = self.sed_requests(req)
        # r = requests.get(url=tag_list_url)
        return r.json()
