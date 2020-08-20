from selenium.webdriver.common.by import By

from pytest_mode3.base import Bese


class Testimportcontact(Bese):

    def test_importcontact(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

        cookies = [
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688851887025887'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': 'T27v3RXSbSK-eIrgFKC5kyfUkZzpR-AQl9HVll8OMjNmXOoJeAuUBInXVgW_AQ6qeYAGyNaSBYe9SfX_aZmYTixcQc6fTaq8WbkXTGnJAhkHhACSlsRjczMbxlDcqdSSgy5qfv5HZiUDp0qX3QAiAa7ldVPA46_54YkLsutsWDjLO9gQ1WielRufOQeEajRlrK5OWxGXLq9cpxgxe85xL3cHzFoBRUilPajm5BI-sSIeRdBavh8Gr4P37eeLd7VA1kLBTdUmWKNHVC01U5kCMg'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688851887025887'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970324993157828'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': '1ZaVe2v8uOXjndpta-rlTVg2EpKmBaKih1MfYNESXM87yZx4I9V5VNJRgqIDVvC2'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a9191708'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d',
             'path': '/', 'secure': False, 'value': '1597850383'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
             'value': '372480165011197'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1597869644, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': False, 'value': 'ntg8fe'},
            {'domain': '.qq.com', 'expiry': 1597936839, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
             'value': 'GA1.2.1682663330.1597838109'},
            {'domain': '.qq.com', 'expiry': 1660922439, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
             'value': 'GA1.2.1357163629.1597502826'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1629038822, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': False, 'value': '0'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1600442442, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'zh-cn'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'}, {'domain': '.work.weixin.qq.com', 'expiry': 1629386382, 'httpOnly': False,
                             'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False,
                             'value': '1597502824,1597846432,1597847782,1597849378'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
             'value': 'direct'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
             'secure': False, 'value': '4300743235'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/',
             'secure': False, 'value': '2799241216'},
            {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False,
             'value': '773760178e01145b13ed502cabc440e712f0dca95462b4e25dfa8e15a1dcfc64'},
            {'domain': '.qq.com', 'expiry': 1598965507, 'httpOnly': False, 'name': 'lskey', 'path': '/',
             'secure': False,
             'value': '00010000265d510fbb4f100abe14c010fbc846f3f01fe15e7b8f912bd3ee025afc0b5d5a0b1855aeb3fc64c1'},
            {'domain': '.qq.com', 'expiry': 2147483852, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False,
             'value': '0Yr4pYvzVG'}]
        # 遍历cookies
        for cookie in cookies:
            # 把带有登录信息的cookie加到当前页面的cookie中
            self.driver.add_cookie(cookie)

        # 打开带有cookie信息的链接
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.find_element(By.LINK_TEXT, "导入通讯录").click()
        # 点击上传文件,并传入文件路径和名称
        self.driver.find_element_by_id("js_upload_file_input").send_keys("/Users/pro/Desktop/鑫博.xlsx")
        # 断言
        assert '鑫博.xlsx' == self.driver.find_element_by_id("upload_file_name").text
