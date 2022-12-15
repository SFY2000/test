# coding='utf-8'
#处理不同的测试报告
import logging
import sys
import unittest

from HTMLTestRunner import HTMLTestRunner
from htmltestreport import HTMLTestReport

from common import config
from common.dologer import Logger

log=Logger(__name__,logging.ERROR)
#生成text格式的测试报告
def doTextPeport(suite):
    filename=config.reportPath+config.current_time+"_report.txt"
    try:
        with open(filename,"w",encoding="utf-8") as f:
            run=unittest.TextTestRunner(stream=f,verbosity=2)
            run.run(suite)
    except Exception as e:
        log.logger.exception("报告生成失败，原因是%s"%e,exc_info=True)
    else:
        log.logger.debug("报告生成成功")

#生成html的格式HTMLTestRunner
def doHtmlTestRunner(suite):
    filename=config.reportPath+config.current_time+"_report.html"
    try:
        with open(filename,"w",encoding="utf-8") as f:
            runner=HTMLTestRunner.HTMLTestRunner\
                (stream=f,verbosity=2,title="html测试报告",description="V1.0版本")
            runner.run(suite)
    except Exception as e:
        log.logger.exception("测试报告生成失败,失败原因是%s"%e,exc_info=True)
    else:
        log.logger.debug("测试报告生成成功")


#生成html的测试报告
def doHTMlTestReport(suite):
    filename=config.reportPath+config.current_time+"_bufRepoet.html"
    runner=HTMLTestReport(filename,title="雷小锋项目漂亮的测试报告",description="V1.0")
    runner.run(suite)

