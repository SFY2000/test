#coding='utf-8'
import logging

from common import config


class Logger(object):
    def __init__(self,name,filelevel=logging.WARNING):
        #定义记录器，日志对象，日志文件的实例
        self.logger=logging.Logger(name)

        #定义日志输入等级
        self.logger.setLevel(filelevel)
        # 格式化日志
        fmt=logging.Formatter\
            ('%(asctime)s-%(filename)s:[%(lineno)s]-[%(levelname)s]-%(message)s')
        # cur_date是让生成的日志文件在当天的日志文件中不断追加，不会生成新的日志文件
        #处理器，写信息到日志文件，默认的打开文件的方式为追加模式
        logname=config.logPath+config.cur_date+".log"
        fh=logging.FileHandler(logname,encoding="utf-8")
        #设置下要让处理器按照什么格式书写日志
        fh.setFormatter(fmt)
        #将处理器加入记录器中：让处理器处理谁
        self.logger.addHandler(fh)


if __name__ == '__main__':
    #写DEBUG就会展示DEBUG及以上等级的信息,如果写WARNING就会出现WARNING及以上信息
    logger=Logger(__name__,logging.DEBUG)
    #写日志
    # logger.logger.log(logging.DEBUG,"我是DEBUG级别的日志，等级是10")
    logger.logger.debug("我是DEBUG级别的日志，等级是10")
    # logger.logger.log(logging.INFO, "我是INFO级别的日志，等级是20")
    logger.logger.info("我是INFO级别的日志，等级是20")
    # logger.logger.log(logging.WARNING, "我是WARNING级别的日志，等级是30")
    logger.logger.warning("我是WARNING级别的日志，等级是30")
    # logger.logger.log(logging.ERROR, "我是ERROR级别的日志，等级是40")
    logger.logger.error("我是ERROR级别的日志，等级是40")
    # logger.logger.log(logging.CRITICAL, "我是CRITICAL级别的日志，等级是50")
    logger.logger.critical("我是CRITICAL级别的日志，等级是50")

