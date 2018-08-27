__author__ = 'zz'
import os
import time
import logging
from conf import read_path

#1：日志收集器
class MyLog:
    def __init__(self,log_name):
        self.log_name=log_name#日志收集器的名字

    def my_log(self,msg,level):
        logger=logging.getLogger(self.log_name)#
        logger.setLevel('DEBUG')#包含INFO级别在内以及以上的日志
        #格式：决定我们日志输出格式
        formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息:%(message)s')
        #2: 日志输出器 控制台  指定的文件
        ch=logging.StreamHandler()#渠道是指输出到控制台
        ch.setLevel('DEBUG')#只输出INFO以上的
        ch.setFormatter(formatter)

        now=time.strftime('%Y-%m-%d')#获取到了当天的时间
        path="test_api_"+now+".txt"#拼接路径
        #最终日志存放的地方
        new_log_path=os.path.join(read_path.log_path,path)

        fh=logging.FileHandler(new_log_path,encoding='UTF-8')
        fh.setLevel('DEBUG')
        fh.setFormatter(formatter)

        #3：对接啦
        logger.addHandler(ch)
        logger.addHandler(fh)

        if level=='DEBUG':
            logger.debug(msg)
        elif level=='INFO':
            logger.info(msg)
        elif level=='WARNING':
            logger.warning(msg)
        elif level=='ERROR':
            logger.error(msg)
        elif level=='CRITICAL':
            logger.critical(msg)

    def debug(self,msg):
        self.my_log(msg,'DEBUG')#调用my_log函数

    def info(self,msg):
        self.my_log(msg,'INFO')#调用my_log函数

    def warning(self,msg):
        self.my_log(msg,'WARNING')#调用my_log函数

    def error(self,msg):
        self.my_log(msg,'ERROR')#调用my_log函数

    def critical(self,msg):
        self.my_log(msg,'CRITICAL')#调用my_log函数

    #解决了日志重复的问题，添加如下代码？

if __name__ == '__main__':
    logger=MyLog('python8')
    logger.debug('这个是我们自己写的日志类')