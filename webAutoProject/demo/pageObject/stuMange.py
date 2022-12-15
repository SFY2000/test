#coding='utf-8'
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from demo.testCase.baseUnittest import BaseUnitTest


class stuMange(BaseUnitTest):
    studentProfile=(By.XPATH,"//div[text()='学员档案']")
    enrollment=(By.XPATH,"//div[text()='招生跟进']")
    studentFees=(By.XPATH,"//div[text()='学员费用']")
    stuimport=(By.XPATH,"//div[text()='导入/导出']")
    enrolmentrate=(By.XPATH,"//div[text()='天']")
    def stumange(self):
        self.loginPage.login()
        self.loginPage.doclick(self.loginPage.stuguanli)
        self.loginPage.doclick(self.enrolmentrate)
        sleep(2)
        self.loginPage.doclick(self.studentProfile)
        self.loginPage.doclick(self.enrollment)
        self.loginPage.doclick(self.studentFees)
        self.loginPage.doclick(self.stuimport)

if __name__ == '__main__':
    driver=webdriver.Chrome()
    student=stuMange()
    student.loginPage.open()
    student.stumange()
    student.driver.quit()
