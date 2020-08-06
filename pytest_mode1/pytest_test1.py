import pytest
import yaml

from pytest_mode1.calc import Calculator
#打开calc文件
with open('./calc.yml') as f:
    #使用safe_laod读取add中的数据
    datas = yaml.safe_load(f)['add']
    #取出datas数据
    adddatas = datas['datas']
    print(adddatas)
    #取出myid数据
    myid = datas['myid']
    print(myid)
# 打开calc文件
with open('./calc.yml') as a:
    #读取div中的数据
    divdatas = yaml.safe_load(a)['div']
    divdata = divdatas['datas']
    print(divdata)
    divmyid = divdatas['myid']
    print(divmyid)
#顶一个计算类
class Testcalc():
    #类级别前的准备工作使用setup_class定义
    def setup_class(self):
        print("类级别开始计算")
        #实例化计算器
        self.calc = Calculator()
    #类级别的结束清理方法使用teardown_class定义
    def teardown_class(self):
        print("类级别结束计算")
    #方法级别的开始计算
    def setup(self):
        print('开始计算')
    #方法级别的结束计算
    def teardown(self):
            print('结束计算')


    #参数化
    @pytest.mark.parametrize('a,b,expect',adddatas,ids=myid)


    #定义add方法
    def test_add(self,a,b,expect):
        result = self.calc.add(a,b)
        #判断result为小数的时候使用round取小数点后两位
        if isinstance(result,float):
            result = round(result,2)
        #断言
        assert expect == result


    @pytest.mark.parametrize('a,b,expect',divdata,ids=divmyid)
#定义div方法
    def test_div(self,a,b,expect):
        #判断b=0,就返回expect
        if b == 0:
            return expect

        result = self.calc.div(a,b)


        # 断言
        assert expect == result


