from time import sleep

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

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

    def test_delete(self):
        self.driver.find_element(MobileBy.XPATH, '//*[@text="通讯录"]').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="测试1"]/../../../..').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/hvd"]').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="编辑成员"]').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="删除成员"]').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="确定"]').click()
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element(MobileBy.XPATH, '//*[@text="企业通讯录"]'))
        ele = self.driver.find_elements(MobileBy.XPATH, '//*[@class="android.widget.TextView"]')
        list1 = []
        for name1 in ele:
            list1.append(name1.text)
        print(list1)
        assert "测试1" not in list1
