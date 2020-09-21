# 封装requests
import requests


class BaseApi:

    def sed_requests(self, req: dict):
        # req = {
        #     "method": "",
        #     "url": "",
        #     "param": {},
        #     "data": {}
        # }

        return requests.request(**req)
