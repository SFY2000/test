import unittest

from common import doSuite, doreport

if __name__ == '__main__':
    #获取测试套件
    # suite=unittest.TestSuite()
    # suite=doSuite.addTestByMethod(suite)
    suite=doSuite.addTestByAuto()
    #执行套件
    # run=doreport.doTextPeport(suite)
    # doreport.doHtmlTestRunner(suite)
    doreport.doHTMlTestReport(suite)
