__author__ = 'libo.yang'
# @time: 2016/10/18 17:00

import json
import pytest
import time
import logging
from Common import project_path
from Common.do_excel import DoExcel
from Common.read_config import ReadConfig
from Common.http_request import HttpRequest
from Common.do_mysql import DoMysql



list_3 = DoExcel(project_path.test_data_path, "test_data").read_file()

ids = [i['module'] for i in list_3]
IP = ReadConfig().read_config(project_path.url_conf_path, 'HTTP', 'ip')
TenantId = ReadConfig().read_config(project_path.url_conf_path, 'HTTP', 'tenantId')
TOKENS = None
headers = {"User-Agent": "Mozilla/5.0",
           "Content-Type": "application/json",
           "token": TOKENS}

t = DoExcel(project_path.test_data_path, "test_data")
p = DoExcel(project_path.test_result_path, 0)
f = DoExcel(project_path.test_result_path, 1)


@pytest.mark.smoke
class TestHttp():


    @pytest.mark.parametrize("data", list_3, ids=ids)
    def test_http(self, data):

        global TOKENS, result, check_sql_result, get_sql, up_sql

        if '$url_1' in json.dumps(data['url'], ensure_ascii=False):
            get_sql = DoMysql().do_msyql(eval(data['get_sql'])['sql'])
            url = data['url'].replace('$url_1', str(get_sql[0]))
        elif '$url_2' in json.dumps(data['url'], ensure_ascii=False):
            get_sql = DoMysql().do_msyql(eval(data['get_sql'])['sql'])
            url = data['url'].replace('$url_2', str(get_sql[0])).replace('$url_3', str(get_sql[1]))
        else:
            url = data['url']

        if '$data_1' in json.dumps(data['param'], ensure_ascii=False):  # 1个参数
            get_sql = DoMysql().do_msyql(eval(data['get_sql'])['sql'])
            param = data['param'].replace('$data_1', str(get_sql[0]))
        elif '$data_2' in json.dumps(data['param'], ensure_ascii=False):  # 2两个参数
            get_sql = DoMysql().do_msyql(eval(data['get_sql'])['sql'])
            param = data['param'].replace('$data_2', str(get_sql[0])).replace('$data_3', str(get_sql[1]))  # ID
        elif '$data_4' in json.dumps(data['param'], ensure_ascii=False):  # 4个参数和url结合的
            get_sql = DoMysql().do_msyql(eval(data['get_sql'])['sql'])
            param = data['param'].replace('$data_4', str(get_sql[1])).replace('$data_5', str(get_sql[2])).replace(
                '$data_6', str(get_sql[3]))
        elif '$data_7' in json.dumps(data['param'], ensure_ascii=False):  # 3个参数
            get_sql = DoMysql().do_msyql(eval(data['get_sql'])['sql'])
            param = data['param'].replace('$data_7', str(get_sql[0])).replace('$data_8', str(get_sql[1])).replace(
                '$data_9', str(get_sql[2]))
        else:
            param = data['param']

        logging.info('执行的是第{}条用例'.format(data['case_id']))
        logging.info('测试用例标题:{}'.format(data['description']))
        logging.info('接口请求地址是:{}'.format(url))
        logging.info('接口请求参数是:{}'.format(param))
        logging.info('接口请求参数是:{}'.format(data['method']))

        if param == None:
            res = HttpRequest(IP + url + TenantId).http_request(data['method'], headers=headers)
        else:
            res = HttpRequest(IP + url + TenantId, param).http_request(data['method'], headers=headers)

        if "token" in json.dumps(res.json(), ensure_ascii=False):
            TOKENS = res.json()['payload']["token"]

        if data['up_sql'] != None:
            up_sql = DoMysql().do_msyql(eval(data['up_sql'])['sql'])

        if data['check_sql'] != None:
            sql_result = DoMysql().do_msyql(eval(data['check_sql'])['sql'])
            try:
                assert  eval(data['check_sql'])['expected'] == str(sql_result[0])
                check_sql_result = 'PASS'
            except AssertionError as e:
                check_sql_result = 'FAIL'
                logging.error('报错的信息是:{}'.format(str(e)))
                raise e
            finally:
                t.write_sql(int(data['case_id']) + 1, str(sql_result), check_sql_result)
                logging.info('数据库断言结果：{}'.format(check_sql_result))
        try:
            assert   str(data['expectresult'])  in  json.dumps(res.json(), ensure_ascii=False)
            result = 'pass'
            p.Write_pass(url, data['method'], param, str(res.json()), result)
        except AssertionError as e:
            result = "fail"
            f.Write_fail(url, data['method'], param, str(res.json()), result)
            logging.error('报错的信息是:{}'.format(str(e)))
            raise e
        finally:
            t.write_data(int(data['case_id']) + 1, str(res.json()), result)
            logging.info('接口返回值断言结果:{}'.format(result))
