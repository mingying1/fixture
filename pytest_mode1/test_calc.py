import pytest
import yaml

from pytest_mode1.calc import Calculator

# 打开calc文件
with open('test_calc.yml') as f:
    # 使用safe_laod读取add中的数据
    datas = yaml.safe_load(f)['add']
    # 取出datas数据
    adddatas = datas['datas']
    print(adddatas)
    # 取出myid数据
    myid = datas['myid']
    print(myid)
# 打开calc文件
with open('test_calc.yml') as a:
    # 读取div中的数据
    divdatas = yaml.safe_load(a)['div']
    divdata = divdatas['datas']
    print(divdata)
    divmyid = divdatas['myid']
    print(divmyid)

with open('test_calc.yml') as b:
    # 读取div中的数据
    subdatas = yaml.safe_load(b)['sub']
    subdata = subdatas['datas']
    print(divdata)
    submyid = subdatas['myid']
    print(divmyid)

with open('test_calc.yml') as c:
    muldatas = yaml.safe_load(c)['mul']
    muldata = muldatas['datas']
    print(muldata)
    mulmyid = muldatas['myid']
    print(mulmyid)


# 使用fixture生成add的别名
@pytest.fixture(params=adddatas, ids=myid)
def get_datas(request):
    data = request.param
    print('data')
    return data


# 使用fixture生成div的别名
@pytest.fixture(params=divdata, ids=divmyid)
def get_divdatas(request):
    datas = request.param
    print('datas')
    return datas


# 使用fixture生成sub的别名
@pytest.fixture(params=subdata, ids=submyid)
def get_subdatas(request):
    datas = request.param
    print('datas')
    return datas


# 使用fixture生成mul的别名
@pytest.fixture(params=muldata, ids=mulmyid)
def get_muldatas(request):
    datas = request.param
    print('datas')
    return datas


# @pytest.fixture(scope='module')
# def get_calc():
#     print("获取计算器实例")
#     calc = Calculator()
#     return calc

# 定义个计算类
class Testcalc():
    # #类级别前的准备工作使用setup_class定义
    # def setup_class(self):
    #     print("类级别开始计算")
    #     #实例化计算器
    #     self.calc = Calculator()
    # #类级别的结束清理方法使用teardown_class定义
    # def teardown_class(self):
    #     print("类级别结束计算")
    # 方法级别的开始计算
    # def setup(self):
    #     print('开始计算')
    # #方法级别的结束计算
    # def teardown(self):
    #         print('结束计算')

    # 参数化
    # @pytest.mark.parametrize('a,b,expect',adddatas,ids=myid)

    # 定义add方法
    def test_add(self, get_calc, get_datas):
        try:

            result = get_calc.add(get_datas[0], get_datas[1])
            print("===========")
            print(result)
            # 判断result为小数的时候使用round取小数点后两位
            if isinstance(result, float):
                result = round(result, 2)
        except:
            if isinstance(get_datas[0], str) or isinstance(get_datas[1], str):
                print("不支持字符串")
                return
            else:
                print(get_datas[0])
                print(get_datas[1])
                print('请输入正确的数据类型')
            # 断言
            assert get_datas[2] == result

    # @pytest.mark.parametrize('a,b,expect',divdata,ids=divmyid)
    # 定义div方法
    def test_div(self, get_calc, get_divdatas):
        try:
            # 判断除数为0,就打印除数不能为0,return
            if get_divdatas[1] == 0:
                print("除数不能为0")
                return
        except:
            if isinstance(get_divdatas[0], str) or isinstance(get_divdatas[1], str):
                print("不支持字符串")
                return
            else:
                print(get_divdatas[0])
                print(get_divdatas[1])
                print('请输入正确的数据类型')

            result = get_calc.div(get_divdatas[0], get_divdatas[1])
            # 断言
            assert get_divdatas[2] == result

    # @pytest.mark.parametrize('a,b,expect',subdata,ids=submyid)
    # 定义sub方法
    def test_sub(self, get_calc, get_subdatas):
        try:
            result = get_calc.sub(get_subdatas[0], get_subdatas[1])
            print(result)
            # 判断result为小数的时候使用round取小数点后两位
            if isinstance(result, float):
                result = round(result, 2)
            # 判断如果参数为字符型,打印不支持字符型
        except:
            if isinstance(get_subdatas[0], str) or isinstance(get_subdatas[1], str):
                print("不支持字符串")
                return
            else:
                print(get_subdatas[0])
                print(get_subdatas[1])
                print('请输入正确的数据类型')
            # 断言
            assert get_subdatas[2] == result

    # @pytest.mark.parametrize('a,b,expect',muldata,ids=mulmyid)
    # 定义mul方法
    def test_mul(self, get_calc, get_muldatas):
        try:
            result = get_calc.mul(get_muldatas[0], get_muldatas[1])
            # 判断result为小数的时候使用round取小数点后两位
            if isinstance(result, float):
                result = round(result, 6)
                # 判断如果参数为字符型,打印不支持字符型
        except:
            if isinstance(get_muldatas[0], str) or isinstance(get_muldatas[1], str):
                print("不支持字符串")
                return
            else:
                print(get_muldatas[0])
                print(get_muldatas[1])
                print('请输入正确的数据类型')
            assert get_muldatas[2] == result
