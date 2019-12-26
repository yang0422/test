__author__ = 'libo.yang'
# @time: 2018/11/13 11:08
# encoding: utf-8
import time
import pytest
from Common import project_path
from Common.to_email import Email

if __name__ == '__main__':
    now = time.strftime('%Y-%m-%d %H_%M')  # 时间戳%Y%m%d_%H%M%S
    html_path = project_path.report_path + '\\' + now + '.html'
    pytest.main(["-m=smoke", "--html=" + html_path, '--self-contained-html'])
    # t=Email().email_to(html_path)