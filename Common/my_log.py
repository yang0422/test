__author__ = 'xuan'
import time
import logging
from Common import project_path

class Mylog:
    def my_log(self, msg, msg_level, level='DEBUG'):
        # 日志收集器
        fmt = " %(asctime)s  %(levelname)s %(filename)s %(funcName)s [ line:%(lineno)d ] %(message)s"
        datefmt = '%a, %d %b %Y %H:%M:%S'
        curTime = time.strftime("%Y-%m-%d", time.localtime())
        logger = logging.getLogger()
        # 收集日志的级别
        logger.setLevel(level)
        #输出渠道
        fh = logging.FileHandler(project_path.log_path+"/Api_Autotest_log_{0}.Log".format(curTime),encoding='UTF-8')  #输出到文件
        sh = logging.StreamHandler()  #输出到控制台
        #输出日志的级别
        fh.setLevel(level)
        sh.setLevel(level)
        #添加日志格式
        formatter = logging.Formatter(fmt=fmt,datefmt=datefmt)
        fh.setFormatter(formatter)
        sh.setFormatter(formatter)

        #对接日志收集器以及输出渠道
        #输出到文件和控制台
        logger.addHandler(fh)
        logger.addHandler(sh)

        if msg_level == 'DEBUG':
            logger.debug(msg)
        elif msg_level == 'INFO':
            logger.info(msg)
        elif msg_level == 'WARNING':
            logger.warning(msg)
        elif msg_level == 'ERROR':
            logger.error(msg)
        elif msg_level == 'CRITICAL':
            logger.critical(msg)
        logger.removeHandler(sh)
        logger.removeHandler(fh)

    def debug(self, msg):
        self.my_log(msg, 'DEBUG')

    def info(self, msg):
        self.my_log(msg, 'INFO')

    def warning(self, msg):
        self.my_log(msg, 'WARNING')

    def error(self, msg):
        self.my_log(msg, 'ERROR')

    def critical(self, msg):
        self.my_log(msg, 'CRITICAL')


if __name__ == '__main__':
    Mylog().info('ss')

