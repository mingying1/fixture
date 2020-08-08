import pytest

from pytest_mode1.calc import Calculator


@pytest.fixture(scope='module')
def get_calc():
    print("获取计算器实例")
    calc = Calculator()
    return calc


@pytest.fixture(scope='function')
def get_calc():
    print("开始计算")
    calc = Calculator()
    yield calc
    print("结束计算")
