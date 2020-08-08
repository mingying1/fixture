import pytest

from pytest_mode1.calc import Calculator


# 使用fixture方法,将scope设置为模块类
@pytest.fixture(scope='module')
#定义get_calc方法,实例化Calculator
def get_calc():
    print("获取计算器实例")
    calc = Calculator()
    return calc


#使用fixture方法,将scope设置为方法类
@pytest.fixture(scope='function')
def get_calc():
    print("开始计算")
    calc = Calculator()
    yield calc
    print("结束计算")
