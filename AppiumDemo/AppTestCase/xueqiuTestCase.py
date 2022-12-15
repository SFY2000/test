from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities={
    "platformName": "Android",
    "platformVersion": "7.1.2",
    "deviceName": "127.0.0.1:62001",
    "app": "D:\\孙菲悦\\xueqiu.apk",
    "noReset": True,
    "appPackage": "com.xueqiu.android",
    "appActivity": ".view.WelcomeActivityAlias",
    "unicodeKeyboard": True,
    "resetKeyboard": True,
    # "chromedriverExecutable": "D:\\pythonCoding\\AppiumDemo\\chromedriver\\chromedriver.exe"
    })
driver.implicitly_wait(60)
# driver.find_element(MobileBy.ID,"com.xueqiu.android:id/home_search").click()
driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("交易")').click()