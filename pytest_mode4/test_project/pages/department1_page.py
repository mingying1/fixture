import time

from selenium.webdriver.common.by import By

from pytest_mode4.test_project.pages.base import Base


class Department1(Base):
    _tabindex = (By.CSS_SELECTOR, "[tabindex='-1']")

    def get_name(self):
        time.sleep(1)
        ele2 = self.finds(*self._tabindex)
        print(ele2)
        return [name.text for name in ele2]
        # list = []
        # for name in list:
        #     list.append(name.text)
        # print(list)
