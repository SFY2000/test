#coding='utf-8'
#基础的unittest,前置后置方法
import unittest

from selenium import webdriver

from demo.pageObject.loginPage import Login


class BaseUnitTest(unittest.TestCase):
    #步骤
    #第一步：执行的代码：setUpClass()类前置
    #第二步执行的代码：setUp()方法前置
    #第三步执行的代码时测试方法
    #第四步执行测试方法中的代码，直到完毕
    #第五步执行tearDown() 方法后置
    #第六步，找还有没有测试方法，有的话，执行方法前置setUp()
    #第七步，第六步有的话，执行测试方法中的代码，直到完毕
    #第八步，第六步有的话，执行teatDown() 方法后置
    #第九步，找还有没有测试方法，有的话，执行方法中的代码，没有的话，执行teatDown() 方法后置
     #类方法的前置
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver=webdriver.Chrome()
        cls.driver.maximize_window()

      #类方法的后置
    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
        #方法级别的前置方法
    def setUp(self) -> None:
        #定义雷小锋登录页面实例化
        self.loginPage=Login(self.driver)
        #打开页面
        self.loginPage.open()

        #方法级别的后置方法
    def tearDown(self) -> None:
        self.driver.refresh()
