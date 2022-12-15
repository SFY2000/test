#coding="utf-8"
#登录页面测试用例类
import unittest
from time import sleep

# from selenium.webdriver.common.by import By
#
# from common import doExcel
from demo.testCase.baseUnittest import BaseUnitTest



class TestLogin(BaseUnitTest):
    #登录成功，用户和密码正确
    def test_login_name_pwd_ok(self):
        self.loginPage.login()
        sleep(10)
        self.title=self.driver.title
        sleep(3)
        self.assertIn("工作台",self.title)
        self.loginPage.logoutFun(self.driver)
    #登录失败，密码用户名为空
    def test_login_name_pwd_kong(self):
        self.loginPage.login(self.loginPage.loginDatalist[1][0],self.loginPage.loginDatalist[1][1])
        sleep(10)
        nameText=self.loginPage.getElementValue(self.loginPage.logininfouser)
        self.assertEqual("请输入手机号码",nameText)
        pwdText=self.loginPage.getElementValue(self.loginPage.logininfopwd)
        self.assertEqual("请输入6-20位账户密码",pwdText)
    #登录失败-用户名空，密码正确
    def test_login_name_pwd_namekong(self):
        self.loginPage.login(self.loginPage.loginDatalist[2][0],self.loginPage.loginDatalist[2][1])
        sleep(20)
        nameText=self.loginPage.getElementValue(self.loginPage.logininfouser)
        sleep(3)
        self.assertEqual("请输入手机号码",nameText)
    #登录失败，用户名正确，密码空
    def test_login_name_pwd_pwdkong(self):
        self.loginPage.login(self.loginPage.loginDatalist[3][0],self.loginPage.loginDatalist[3][1])
        sleep(20)
        pwdText = self.loginPage.getElementValue(self.loginPage.logininfopwd)
        self.assertEqual("请输入6-20位账户密码", pwdText)
    #登录失败，用户名错误，密码正确
    def test_login_name_pwd_usererror(self):
        self.loginPage.login(self.loginPage.loginDatalist[4][0],self.loginPage.loginDatalist[4][1])
        errorname=self.loginPage.getElementValue(self.loginPage.errormessahe)
        self.assertIn("用户名或密码错误",errorname)
        self.loginPage.doclick(self.loginPage.errerbutton)
    #登录失败，用户名正确，密码错误
    def test_login_name_pwd_pwderror(self):
        self.loginPage.login(self.loginPage.loginDatalist[5][0],self.loginPage.loginDatalist[5][1])
        errorpwd=self.loginPage.getElementValue(self.loginPage.errormessahe)
        self.assertIn("用户名或密码错误",errorpwd)
        self.loginPage.doclick(self.loginPage.errerbutton)
    #登录失败，用户名错误，密码错误
    def test_login_name_pwd_error(self):
        self.loginPage.login(self.loginPage.loginDatalist[6][0],self.loginPage.loginDatalist[6][1])
        error=self.loginPage.getElementValue(self.loginPage.errormessahe)
        self.assertIn("用户名或密码错误",error)
        self.loginPage.doclick(self.loginPage.errerbutton)
    #登录失败，用户名长度不够，密码正确
    def test_user_pwd_usershort(self):
        self.loginPage.login(self.loginPage.loginDatalist[7][0], self.loginPage.loginDatalist[7][1])
        sleep(20)
        nameText = self.loginPage.getElementValue(self.loginPage.logininfouser)
        sleep(3)
        self.assertEqual("请输入手机号码", nameText)
    #登录失败，用户名正确，密码长度不够
    def test_user_pwd_pwdshort(self):
        self.loginPage.login(self.loginPage.loginDatalist[9][0], self.loginPage.loginDatalist[9][1])
        sleep(20)
        pwdText = self.loginPage.getElementValue(self.loginPage.logininfopwd)
        self.assertEqual("请输入6-20位账户密码", pwdText)
    #登录失败，用户名超过11位，密码正确
    def test_user_pwd_userlong(self):
        self.loginPage.login(self.loginPage.loginDatalist[8][0],self.loginPage.loginDatalist[8][1])
        sleep(20)
        error = self.loginPage.getElementValue(self.loginPage.errormessahe)
        self.assertIn("用户名或密码错误", error)
        self.loginPage.doclick(self.loginPage.errerbutton)
    #登录失败，用户名正确，密码多余20位
    def test_user_pwd_pwdlong(self):
        self.loginPage.login(self.loginPage.loginDatalist[10][0], self.loginPage.loginDatalist[10][1])
        sleep(20)
        error = self.loginPage.getElementValue(self.loginPage.errormessahe)
        self.assertIn("用户名或密码错误", error)
        self.loginPage.doclick(self.loginPage.errerbutton)
    # 用户名长度超过12位，密码超出21位
    def test_user_pwd_pwduserlong(self):
        self.loginPage.login(self.loginPage.loginDatalist[11][0], self.loginPage.loginDatalist[11][1])
        sleep(20)
        error = self.loginPage.getElementValue(self.loginPage.errormessahe)
        self.assertIn("用户名或密码错误", error)
        self.loginPage.doclick(self.loginPage.errerbutton)
    #用户名长度不够，密码长度不够
    def test_login_name_pwd_userpwdshort(self):
        self.loginPage.login(self.loginPage.loginDatalist[12][0],self.loginPage.loginDatalist[12][1])
        sleep(10)
        nameText=self.loginPage.getElementValue(self.loginPage.logininfouser)
        self.assertEqual("请输入手机号码",nameText)
        pwdText=self.loginPage.getElementValue(self.loginPage.logininfopwd)
        self.assertEqual("请输入6-20位账户密码",pwdText)
if __name__ == '__main__':
    unittest.main()
