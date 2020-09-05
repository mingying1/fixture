from appium import webdriver


class Base:
    def setup(self):
        # capabilities设置
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

    def teardown(self):
        self.driver.quit()
