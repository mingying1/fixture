from appium import webdriver

from pytest_mode7.page.base_page import BasePage
from pytest_mode7.page.main_page import MainPage

"""
启动应用,重启应用,关闭应用,进入到首页

"""


class App(BasePage):
    def start(self):
        if self.driver == None:
            # 启动APP
            desire_cap = {
                "platformName": "android",
                "deviceName": "emulator-5554",
                "appPackage": "com.tencent.wework",
                "appActivity": ".launch.WwMainActivity",
                "noReset": "True",  # 记住上一次弹框等信息
                'settings[waitForIdleTimeout]': 0,  # 等待页面空闲的时间
                "newCommandTimeout": 300
            }
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
            self.driver.implicitly_wait(5)
        else:
            # 复用已有的driver  中appPackage,appActivity值
            # self.driver.start_activity(appPackage,appActivity)可以启用任何APP
            self.driver.launch_app()
        return self

    def restar(self):
        self.driver.close()
        self.driver.launch_app()

    def stop(self):
        self.driver.quit()

    def goto_main(self) -> MainPage:
        return MainPage(self.driver)
