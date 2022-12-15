#coding='utf-8'
#所有的配置文件的信息
import os.path
import time

#基本的页面地址
base_url="http://139.199.0.102/passport/login"
#项目路径
basePath="D:/pythonCoding/webAutoProject"
# photoPath=basePath+"\data\photos/"
photoPath=os.path.join(basePath,r"data/photos/")
#截图时间
current_time=time.strftime("%Y_%m_%d %H_%M_%S")
#当前日期
cur_date=time.strftime("%Y_%m_%d")
#log路径
# logPath=basePath+"\data\logs/"
logPath=os.path.join(basePath,r"data/logs/")
#excel路径
data_path=os.path.join(basePath,r"data/testDatas/")
#测试用例的路径
testcase_Path=os.path.join(basePath,r"demo/testCase/")
#测试报告路径
reportPath=os.path.join(basePath,r"data/reports/")
