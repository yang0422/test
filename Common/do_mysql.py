__author__ = 'xuan'
import mysql.connector
from Common import project_path
from Common.my_log import Mylog
from Common.read_config import ReadConfig
from Common.do_excel import DoExcel

logger = Mylog()


class DoMysql:
    def do_msyql(self, sql):
        config = eval(ReadConfig().read_config(project_path.mysql_conf_path, 'DATAMYSQL', 'config'))
        cn = mysql.connector.connect(**config)  #
        cursor = cn.cursor()
        try:
            cursor.execute(sql)
            result = cursor.fetchone()
            cn.commit()  # 更新数据库要添加
            return result
        except Exception as e:
            logger.error("查询数据库出错，错误信息是:{}".format(str(e)))
        finally:
            cursor.close()
            cn.close()


if __name__ == '__main__':
    sql = 'SELECT count(*) FROM  activity  WHERE activity_name="API-测试转盘活动" AND  deleted=0 AND status=3'
    sql_s = DoMysql().do_msyql(sql)
    print(sql_s)
