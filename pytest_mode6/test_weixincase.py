from appium.webdriver.common.mobileby import MobileBy

from pytest_mode6.base import Base


class TestWechat(Base):
    def test_clock_in(self):
        self.driver.find_element(MobileBy.XPATH, '//*[@text="工作台"]').click()
        # 实现滚动查找元素
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0))'
                                 '.scrollIntoView(new UiSelector()'
                                 '.text("打卡").instance(0));').click()
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/hgs").click()
        # 模糊匹配
        self.driver.find_element(MobileBy.XPATH, '//*[contains(@text,"次外出")]').click()

        result = self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/oh").text
        print(result)
        assert "外出打卡成功" == result
