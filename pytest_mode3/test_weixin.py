from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from pytest_mode3.base import Bese


class Testweixin(Bese):

    def test_login(self):
        # 给微信企业的首页链接
        self.driver.get("https://work.weixin.qq.com/")
        # 点击登录入口
        self.driver.find_element_by_class_name("index_top_operation_loginBtn").click()
        sleep(10)
        # 获取当前页面的cookies
        cookies = self.driver.get_cookies()
        print(cookies)

        # cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688851887025887'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'rouatLPH2_i45TSFoGKWOE8K1vjQyO_LRxW1PlwBf0ZxGo65IHQ1S6U5NwOaA9Ywc1dpUEzSWuiizapYaBkfV5h8A6nkjDfVD7s66QoarV3gcwRjzGDwm_n2RANd8tHgh8T3kwaJ2DxvRU1qAZJr5qoLUpwWvzbZDGVtkc5QDWbd0uCuMj0lOzPpl31KoxWC1yaVorUcfSStJvNqIh3ETIgUxnpmaNRnwMI1GYu_2kuB0aoP1-l_u6fypzIQxnVAjaazi7hrbq-Qizdkra0_IQ'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688851887025887'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970324993157828'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': '1ZaVe2v8uOXjndpta-rlTXbVkVGD0-Ds8upJRhSyHqt89DtpYC1InP_vHMsV5jTE'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a6188875'}, {'domain': 'work.weixin.qq.com', 'expiry': 1598224585, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '7njv1ne'}, {'domain': '.qq.com', 'expiry': 1598279455, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.1478521613.1598193051'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1598193050'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '37248016501849929'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'expiry': 1629729050, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1598193050'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.qq.com', 'expiry': 1598193111, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.qq.com', 'expiry': 1661265055, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.1272193944.1598193051'}, {'domain': '.work.weixin.qq.com', 'expiry': 1629729049, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.work.weixin.qq.com', 'expiry': 1600785058, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh-cn'}]
        # # 遍历cookies
        # for cookie in cookies:
        #     # 把带有登录信息的cookie加到当前页面的cookie中
        #     self.driver.add_cookie(cookie)
        #
        # # 打开带有cookie信息的链接
        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        # # #通过点击首页来断言是否登录成功
        # self.driver.find_element(By.LINK_TEXT, "首页").click()
        # categoryele = self.driver.find_element(By.LINK_TEXT, "首页")
        # print(categoryele.get_attribute("class"))
        # assert 'frame_nav_item frame_nav_item_Curr' == categoryele.get_attribute("class")
