#coding='utf-8'
#百度登录页面
from selenium import webdriver
from selenium.webdriver.common.by import By

from common import doExcel
from demo.pageObject.basePage import BasePage


# 定义一个百度登录页面的类
# 并完成数据剥离
# 理解下文件读取的原理
#
doexcel=doExcel.DoExcel("baiduelement","baidulogin.xlsx")
class baiduLogin(BasePage):
    #页面登录按钮

    login1=(By.CSS_SELECTOR,doexcel.readExcel(3,4))
    #用户名
    username=(By.CSS_SELECTOR,doexcel.readExcel(1,4))
    #密码
    password=(By.CSS_SELECTOR,doexcel.readExcel(2,4))
    #登录按钮
    login2=(By.CSS_SELECTOR,doexcel.readExcel(4,4))
    #错误信息
    errorinfo=(By.CSS_SELECTOR,doexcel.readExcel(5,4))
    def baidulogin(self,user,pwd):
        #点击页面登录按钮
        self.doclick(self.login1)
        #输入用户名
        self.inputValue(self.username,user)
        #输入密码
        self.inputValue(self.password,pwd)
        #点击登录按钮
        self.doclick(self.login2)

if __name__ == '__main__':
    driver=webdriver.Chrome()
    url="https://www.baidu.com/"
    baidu=baiduLogin(driver,url)
    baidu.open()
    baidu.baidulogin("17319744388","sunfeiyue")

    #获取错误信息
    error=baidu.getElementValue(baidu.errorinfo)
    print(error)

    baidu.driver.quit()



