#coding='utf-8'
#处理excel文件
import logging

import xlrd

from common import config
from common.dologer import Logger

log=Logger(__name__,logging.DEBUG)
class DoExcel(object):
    #重构初始化方法
    def __init__(self,sheet="elements",wk="testData.xlsx"):
        filename=config.data_path+wk
        #打开工作簿
        try:
            self.wkbook=xlrd.open_workbook(filename)
            #获取sheet页,三种方式获取sheet页
            #第一种方式：列表的下标
            #返回excel所有的sheet页名称
            # totalsheet=self.wkbook.sheet_names()
            # print(totalsheet)
            # self.sheet=totalsheet[0]
            # self.sheet=self.wkbook.sheet_names()[0]
            #第二种方式：索引
            # self.sheet=self.wkbook.sheet_by_index(0)
            #第三种方式：sheet名称
        except Exception as e:
            log.logger.error("excel表打开失败%s"%e,exc_info=True)
        else:
            log.logger.debug("excel表打开成功")


        try:
            self.sheet=self.wkbook.sheet_by_name(sheet)
        except Exception as e:
            log.logger.error("sheet页定位失败%s"%e,exc_info=True)
        else:
            log.logger.debug("sheet页定位成功")

        #读取单元格内容
    def readExcel(self,rownum,colnum):
        try:
            value=self.sheet.cell_value(rownum,colnum)
        except Exception as e:
            log.logger.error("读取文件异常%s"%e,exc_info=True)
        else:
            log.logger.debug("读取文件成功%s"%value)
            return value








if __name__ == '__main__':
    ex=DoExcel()
    value=ex.readExcel(1, 4)
    print(value)