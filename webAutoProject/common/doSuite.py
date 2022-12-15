#coding='utf-8'
#测试套件testSuite添加方式
import unittest

from common import config
from demo.testCase.Test_login import TestLogin


#第一种，通过测试类，及测试方法添加用例
def addTestByMethod(suite):
    suite.addTest(TestLogin("test_login_name_pwd_ok"))
    suite.addTest(TestLogin("test_login_name_pwd_kong"))
    return suite


#第二种，添加扩展
def addTestByClass(suite):
    suite.addTest\
        (unittest.defaultTestLoader.loadTestsFromTestCase(TestLogin))
    return suite

#第三种方法，使用testLoader
def addTestByAuto():
    suite=unittest.TestLoader().discover\
        (config.testcase_Path,pattern="Test*.py")
    return suite
# #定义空箱子
# suite1=unittest.TestSuite()
# #向空箱子中添加用例
# suite2=addTestByMethod(suite1)
# print("我调用的是第一个方法",suite2)
#
#
# suite3=addTestByClass(suite1)
# print("我调用的是第二个方法",suite3)
#
# #通过py文件自动匹配的方式，集合用例并打包成一个箱子
# suit4=addTestByAuto()
# print("我调用的第三种方法",suit4)