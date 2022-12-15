# coding='utf-8'
# 2.新建测试用例py文件，完成工作台的测试用例
#   #用例1：工作台页面个人信息元素的断言
#   #用例2：左侧菜单列表的断言
import unittest
from time import sleep

from selenium.webdriver import ActionChains

from demo.testCase.baseUnittest import BaseUnitTest




class Testwork(BaseUnitTest):
    def test_infoname(self):
        self.loginPage.login()
        sleep(3)
        info = self.loginPage.getElementValue(self.loginPage.infoname)
        sleep(3)
        self.assertEqual("龚老师1", info)
    def test_infonum(self):
        self.loginPage.login()
        sleep(3)
        info = self.loginPage.getElementValue(self.loginPage.infonum)
        sleep(3)
        self.assertEqual("13986128128", info)
    def test_work_info(self):
        self.loginPage.login()
        sleep(3)
        self.loginPage.actionPerform()
        self.loginPage.doclick(self.loginPage.selfinfo)
        sleep(3)
        info=self.driver.title
        self.assertIn("个人信息",info)
    def test_work(self):
        self.loginPage.login()
        sleep(3)
        self.loginPage.doclick(self.loginPage.worktai)
        sleep(2)
        info=self.driver.title
        sleep(3)
        self.assertIn("工作台",info)
    def test_stumessage(self):
        self.loginPage.login()
        sleep(3)
        self.loginPage.doclick(self.loginPage.stuguanli)
        sleep(3)
        info = self.driver.title
        sleep(3)
        self.assertIn("学员管理", info)
    def test_teacher(self):
        self.loginPage.login()
        sleep(3)
        self.loginPage.doclick(self.loginPage.teacher)
        sleep(3)
        info = self.driver.title
        sleep(3)
        self.assertIn("教务管理", info)
    def test_management(self):
        self.loginPage.login()
        sleep(3)
        self.loginPage.doclick(self.loginPage.management)
        sleep(3)
        info = self.driver.title
        sleep(3)
        self.assertIn("机构管理", info)
    def test_data(self):
        self.loginPage.login()
        sleep(3)
        self.loginPage.doclick(self.loginPage.dataanalysis)
        sleep(3)
        info = self.driver.title
        sleep(3)
        self.assertIn("数据分析", info)
    def test_addstu(self):
        self.loginPage.login()
        sleep(3)
        self.loginPage.doclick(self.loginPage.admissions)
        sleep(3)
        info = self.driver.title
        sleep(3)
        self.assertIn("招生吧", info)
    def test_exam(self):
        self.loginPage.login()
        sleep(3)
        self.loginPage.doclick(self.loginPage.examination)
        sleep(3)
        info = self.driver.title
        sleep(3)
        self.assertIn("考级管理", info)
if __name__ == '__main__':
    unittest.main()
