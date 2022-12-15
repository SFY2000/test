#coding='utf-8'
#基础页面类,存放所有页面都可能用到的公共方法及属性
#所有page类均继承该基础类
import logging
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from common import config
from common.doExcel import DoExcel
from common.dologer import Logger
doexcel=DoExcel()
dataexcel=DoExcel("loginData","testData.xlsx")
log=Logger(__name__,logging.DEBUG)
class BasePage(object):
    #重构初始化方法
    #工作台
    worktai=(By.CSS_SELECTOR,"[class*='.nav1.sel']>span")
    stuguanli=(By.XPATH,"//span[text()='学员管理']")
    teacher=(By.XPATH,"//span[text()='教务管理']")
    management=(By.XPATH,"//span[text()='机构管理']")
    dataanalysis=(By.XPATH,"//span[text()='数据分析']")
    admissions=(By.XPATH,"//span[text()='招生吧']")
    examination=(By.XPATH,"//span[text()='考级管理']")
    selfinfo=(By.XPATH,"//*[@id='headerH']/div[2]/div[5]/div[2]/div[1]")
    selfinfo1=(By.XPATH,"//span[text()='个人信息']")
    studentProfile = (By.XPATH, "//div[text()='学员档案']")
    enrollment = (By.XPATH, "//div[text()='招生跟进']")
    studentFees = (By.XPATH, "//div[text()='学员费用']")
    stuimport = (By.XPATH, "//div[text()='导入/导出']")
    enrolmentrate = (By.XPATH, "//div[text()='天']")
    infoname=(By.XPATH,"//span[text()='龚老师1']")
    infonum=(By.XPATH,"//span[text()='13986128128']")
    # 退出登录按钮
    img = (By.CSS_SELECTOR,doexcel.readExcel(12,4))
    loginout = (By.XPATH, doexcel.readExcel(13,4))
    logoutok = (By.CSS_SELECTOR, doexcel.readExcel(14,4))
    def __init__(self,driver,url=config.base_url):
        self.driver=driver
        self.url=url
    #打开页面
    def open(self):
        try:
            self.driver.get(self.url)

        except Exception as e:
            # print("异常发生，页面打开失败，失败内容时是：%s\n失败的页面是%s"%(e,self.url))
            log.logger.critical\
                ("异常发生，页面打开失败，失败内容时是：%s\n失败的页面是%s"%(e,self.url))
        else:
            # print("未发生异常页面打开成功：%s"%self.url)
            log.logger.info("未发生异常页面打开成功：%s"%self.url)
            self.driver.maximize_window()
            self.driver.implicitly_wait(10)
    #定位元素
    def findElment(self,*locater):
        try:
            ele=WebDriverWait(self.driver,5,0.1).\
                until(EC.visibility_of_element_located(locater))
        except Exception as e:
            log.logger.error("定位元素失败异常信息是：%s\n定位失败信息：%s"%(e,str(locater)))
            # print("定位元素失败异常信息是：%s\n定位失败信息：%s"%(e,str(locater)))
        else:
            # print("元素定位成功，定位成功信息是:%s"%str(locater))
            log.logger.debug("元素定位成功，定位成功信息是:%s"%str(locater))
            return ele
    #文本框输入
    def inputValue(self,inputbox,value):
        ele=self.findElment(*inputbox)
        try:
            ele.send_keys(value)
        except Exception as e:
            # print("输入内容失败：%s\n失败原因是%s"%(value,e))
            log.logger.error("输入内容失败：%s\n失败原因是%s"%(value,e))
        else:
            # print("输入内容成功")
            log.logger.debug("输入内容成功")
    #获取标签值
    def getElementValue(self,element):
        ele=self.findElment(*element)
        try:
            eleText=ele.text
        except Exception as e:
            # print("获取文本失败；%s\n错误信息是%s"%(str(element),e))
            log.logger.error("获取文本失败；%s\n错误信息是%s"%(str(element),e))
        else:
            # print("文本获取成功：%s"%eleText)
            log.logger.debug("文本获取成功：%s"%eleText)
            return eleText
    #截图
    def doPhoto(self,name):
        filement=config.photoPath+config.current_time+name+".png"
        try:
            self.driver.get_screenshot_as_file(filement)
        except Exception as e:
            # print("截图失败:%s失败信息是%s"%(filement,e))
            log.logger.error("截图失败:%s失败信息是%s"%(filement,e))
        else:
            # print("截图成功%s"%filement)
            log.logger.debug("截图成功%s"%filement)
    #元素点击
    def doclick(self,element):
        ele=self.findElment(*element)
        try:
            # ele.click()
            self.driver.execute_script("arguments[0].click();", ele)
        except Exception as e:
            # print("点击失败%s\n失败信息是：%s"%(str(element),e))
            log.logger.error("点击失败%s\n失败信息是：%s"%(str(element),e))
        else:
            # print("点击成功")
            log.logger.debug("点击成功")
    #退出登录
    def logoutFun(self,driver):
        self.actionPerform()
        #退出登录按钮
        self.doclick(self.loginout)
        self.doclick(self.logoutok)
        sleep(3)
    def actionPerform(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.findElment(*self.img))
        action.perform()

if __name__ == '__main__':
    driver=webdriver.Chrome()
    url="http://www.baidu.com"
    bspage=BasePage(driver,url)
    #打开页面
    bspage.open()
    bspage.driver.maximize_window()
    bspage.driver.implicitly_wait(10)

    #获取标签值
    locater_text=(By.ID,"s-usersetting-top")
    bspage.getElementValue(locater_text)
    #调用输入框
    locater=(By.ID,"kw")
    bspage.inputValue(locater,"python")
    #元素点击
    locater_click=(By.ID,"su")
    bspage.doclick(locater_click)
    #截图
    bspage.doPhoto("1")
    bspage.driver.quit()


    #雷小锋
    driver=webdriver.Chrome()
    url=config.base_url
    leiPath=BasePage(driver,url)
    #打开页面
    leiPath.open()
    leiPath.driver.maximize_window()
    leiPath.driver.implicitly_wait(10)
    #获取文本值
    locater_text=(By.CSS_SELECTOR,".forgot.ng-tns-c1-0")
    leiPath.getElementValue(locater_text)
    #文本输入框
    locater=(By.CSS_SELECTOR,"[formcontrolname='userName']")
    leiPath.inputValue(locater,"17319744388")
    locater1=(By.CSS_SELECTOR,"[formcontrolname='password']")
    leiPath.inputValue(locater1,"sunfeiyue2000")
    #点击登录
    locater_click=(By.CSS_SELECTOR,"[type='submit']")
    leiPath.doclick(locater_click)
    #截图
    leiPath.doPhoto("2")
    leiPath.driver.quit()

