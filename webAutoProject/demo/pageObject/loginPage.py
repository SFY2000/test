#coding='utf-8'
#雷小锋登录页面
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from common import config

from demo.pageObject.basePage import BasePage, doexcel, dataexcel


class Login(BasePage):
    # 登录数据
    loginDatalist = [[dataexcel.readExcel(1, 3), dataexcel.readExcel(1, 4)],  # 正确的用户名，密码
                     [dataexcel.readExcel(2, 3), dataexcel.readExcel(2, 4)],  # 用户名空，密码空
                     [dataexcel.readExcel(3, 3), dataexcel.readExcel(3, 4)],  # 用户名空，密码非空
                     [dataexcel.readExcel(4, 3), dataexcel.readExcel(4, 4)],  # 用户名非空，密码空
                     [dataexcel.readExcel(5, 3), dataexcel.readExcel(5, 4)],  # 用户名错误，密码正确
                     [dataexcel.readExcel(6, 3), dataexcel.readExcel(6, 4)],  # 用户名正确，密码错误
                     [dataexcel.readExcel(7, 3), dataexcel.readExcel(7, 4)],  # 用户名错误，密码错误
                     [dataexcel.readExcel(8, 3), dataexcel.readExcel(8, 4)],  # 用户名长度不够，密码正确
                     [dataexcel.readExcel(9, 3), dataexcel.readExcel(9, 4)],  # 用户名长度超出12位，密码正确
                     [dataexcel.readExcel(10, 3), dataexcel.readExcel(10, 4)],  # 用户名长度正确，密码不够
                     [dataexcel.readExcel(11, 3), dataexcel.readExcel(11, 4)],  # 用户名长度正确，密码超出20位
                     [dataexcel.readExcel(12, 3), dataexcel.readExcel(12, 4)],  # 用户名长度超过12位，密码超出21位
                     [dataexcel.readExcel(13, 3), dataexcel.readExcel(13, 4)]  # 用户名长度不够，密码长度不够
                     ]
    #用户名
    # usern = dataexcel.readExcel(1,2)
    # pwde = dataexcel.readExcel(2,2)
    # usererror = dataexcel.readExcel(3,2)
    # pwderror = dataexcel.readExcel(4,2)
    # usershort=dataexcel.readExcel(5,2)
    # pwdshort=dataexcel.readExcel(6,2)
    # userlong=dataexcel.readExcel(7,2)
    # pwdlong=dataexcel.readExcel(8,2)
    username=(By.CSS_SELECTOR,doexcel.readExcel(1,4))
    #密码
    password=(By.CSS_SELECTOR,doexcel.readExcel(2,4))
    #登录按钮
    loginclick=(By.CSS_SELECTOR,doexcel.readExcel(3,4))
    #错误信息
    logininfouser = (By.XPATH, doexcel.readExcel(4, 4))
    logininfopwd=(By.XPATH,doexcel.readExcel(5,4))
    #弹窗错误
    errormessahe=(By.XPATH,doexcel.readExcel(6,4))
    #错误提示确认按钮
    errerbutton=(By.XPATH,doexcel.readExcel(7,4))
    #登录方法
    def login(self,user=loginDatalist[0][0],pwd=loginDatalist[0][1]):
        #输入用户名
        self.inputValue(self.username,user)
        #输入密码
        self.inputValue(self.password,pwd)
        #点击登录按钮
        self.doclick(self.loginclick)
        sleep(10)
if __name__ == '__main__':
    driver=webdriver.Chrome()
    url=config.base_url
    page=Login(driver,url)
    page.open()
    page.login()
    # #输入为空的时候
    # page.login("","")
    # page.login()
    #  错误信息密码错误
    # erroruser=page.getElementValue(page.logininfopwd)
    # print(erroruser)
    # #账号错误
    # errorpwd=page.getElementValue(page.logininfouser)
    # print(errorpwd)
    # page.driver.quit()

    #正确的用户名，错误的密码
    # errormessage=page.getElementValue(page.errormessahe)
    # print(errormessage)
    # page.doclick(page.errerbutton)














