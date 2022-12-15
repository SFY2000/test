# coding='utf-8'

# 3.新建测试用例py文件，完成学员管理的测试用例
#   #测试用例1，学员管理页面某个的断言
#   #测试用例2，学员管理有三个下拉菜单
import unittest
from time import sleep

from demo.testCase.baseUnittest import BaseUnitTest



class Teststu(BaseUnitTest):
    def test_stu_studentProfile(self):
        self.loginPage.login()
        sleep(2)
        self.loginPage.doclick(self.loginPage.stuguanli)
        sleep(2)
        self.loginPage.doclick(self.loginPage.studentProfile)
        sleep(2)
        title=self.driver.title
        sleep(2)
        self.assertIn("学员档案",title)
    def test_stu_enrollment(self):
        self.loginPage.login()
        sleep(2)
        self.loginPage.doclick(self.loginPage.stuguanli)
        sleep(2)
        self.loginPage.doclick(self.loginPage.enrollment)
        sleep(2)
        title = self.driver.title
        self.assertIn("招生跟进", title)
    def test_stu_stuimport(self):
        self.loginPage.login()
        sleep(2)
        self.loginPage.doclick(self.loginPage.stuguanli)
        sleep(2)
        self.loginPage.doclick(self.loginPage.stuimport)
        sleep(2)
        title = self.driver.title
        self.assertIn("导入/导出", title)
    def test_stu_studentFees(self):
        self.loginPage.login()
        sleep(2)
        self.loginPage.doclick(self.loginPage.stuguanli)
        sleep(2)
        self.loginPage.doclick(self.loginPage.studentFees)
        sleep(2)
        title = self.driver.title
        self.assertIn("学员费用", title)
if __name__ == '__main__':
    unittest.main()
