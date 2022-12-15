#coding='utf-8'
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from demo.pageObject.loginPage import Login


class studentProfile(Login):
    studentProfile = (By.XPATH, "//div[text()='学员档案']")
    allstudents= (By.XPATH, "//div[text()='全部学员']")
    followedstudent=(By.XPATH, "//div[text()='待跟进学员']")
    studentprogress=(By.XPATH, "//div[text()='在读学员']")
    lossstudent=(By.XPATH, "//div[text()='流失学员']")
    # select = (By.CSS_SELECTOR, "[placeholder='请输入学员姓名、昵称、联系电话、招生老师']")
    select=(By.CSS_SELECTOR,".placeholder.ng-untouched.ng-pristine.ng-valid.ant-input.ng-star-inserted")
    selectbutton=(By.CSS_SELECTOR,"[class^='.c-secondary.ant-btn']")
    def studentprofile(self,value="大黄"):
        self.login()
        self.doclick(self.stuguanli)
        self.doclick(self.studentProfile)
        #全部学员
        self.doclick(self.allstudents)
        sleep(1)
        self.inputValue(self.select, value)
        self.doclick(self.selectbutton)
        sleep(5)
        #待跟进学员
        self.doclick(self.followedstudent)
        sleep(1)
        self.inputValue(self.select, value)
        self.doclick(self.selectbutton)
        sleep(5)
        #在读学员
        self.doclick(self.studentprogress)
        sleep(1)
        self.inputValue(self.select, value)
        self.doclick(self.selectbutton)
        sleep(5)
        #流失学员
        self.doclick(self.lossstudent)
        sleep(1)
        self.inputValue(self.select, value)
        self.doclick(self.selectbutton)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    stuprofile=studentProfile(driver)
    stuprofile.open()
    stuprofile.studentprofile()
    stuprofile.driver.quit()
