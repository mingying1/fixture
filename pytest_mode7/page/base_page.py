"""
基类:初始化driver,find等方法

"""
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    # 初始化driver
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    # find方法
    def find(self, locator):
        return self.driver.find_element(*locator)

    # 查找并点击方法
    def find_and_click(self, locator):
        self.find(locator).click()

    # 查找并输入
    def find_and_sendkeys(self, locator, valua):
        self.find(locator).send_keys(valua)

    # 滑动找到并点击
    def find_by_scroll_and_click(self, text):
        ele = (MobileBy.ANDROID_UIAUTOMATOR,
               'new UiScrollable(new UiSelector()'
               '.scrollable(true).instance(0))'
               '.scrollIntoView(new UiSelector()'
               f'.text("{text}").instance(0));')

        self.find_and_click(ele)

    # 查找获取他的text
    def find_and_get_text(self, locator):
        return self.find(locator).text

    # 获取toast弹框中的信息
    def gettoast_text(self):
        element = (MobileBy.XPATH, "//*[@class='android.widget.Toast']")
        return self.find_and_get_text(element)

    # finds方法
    def finds(self, locator):
        return self.driver.find_elements(*locator)

    # 显示等待
    def show_wait(self, element):
        # 显示等待元素可见
        return WebDriverWait(self.driver, 10).until(expected_conditions.invisibility_of_element_located(element))
