import time
import logging
from Common import project_path
from logging.handlers import RotatingFileHandler


fmt = " %(asctime)s  %(levelname)s %(filename)s %(funcName)s [ line:%(lineno)d ] %(message)s"
datefmt = '%a, %d %b %Y %H:%M:%S'

handler_1 = logging.StreamHandler()

curTime = time.strftime("%Y-%m-%d")
# 拼接日志路径+日志文件名称
handler_2 = RotatingFileHandler(project_path.log_path + "/Api_Autotest_log_{0}.Log".format(curTime), backupCount=20,
                                encoding='utf-8')
# 输出控制台+文件
# logging.basicConfig(format=fmt, datefmt=datefmt, level=logging.INFO, handlers=[handler_1, handler_2])
#只输出控制台
logging.basicConfig(format=fmt, datefmt=datefmt, level=logging.INFO, handlers=[handler_2])
