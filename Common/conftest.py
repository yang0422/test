__author__ = 'yang'

import pytest
from py._xmlgen import html
from datetime import datetime


def pytest_configure(config):
    # 添加接口地址与项目名称
    config._metadata["项目名称"] = "DM接口自动化测试项目v1.0"
    config._metadata['接口地址'] = 'http://dm.dev.deepexi.top/'
    # 删除Java_Home
    config._metadata.pop("JAVA_HOME")


@pytest.mark.optionalhook
def pytest_html_results_summary(prefix):
    prefix.extend([html.p("所属部门: 测试部")])
    prefix.extend([html.p("测试人员: 杨礼博")])
