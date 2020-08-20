import shelve

from selenium.webdriver.common.by import By

from pytest_mode3.base import Bese


class TestShelve(Bese):
    # shelve是Python内置的模块,相当于小型的数据库
    def test_shelve(self):
        # #以下操作是将上方的cookies数据存储到mydbs中生成cookies.db文件
        # #打开创建的mydbs中的cookies
        db = shelve.open('./mydbs/cookies')
        # #db中的cookie是上方cookies中的信息
        # db['cookie'] = cookies
        # #关闭连接
        # db.close()
        # 如何获取出cookie数据
        cookies = db['cookie']
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
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
