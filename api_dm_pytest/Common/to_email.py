__author__ = 'xuan'
import time
import os
import smtplib
import configparser
from Common import project_path
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


class Email:
    def __init__(self, file_name=project_path.email_conf_path):
        '''
        读取配置文件参数
        :param file_name:配置文件的路径
        :return:
        '''
        conf = configparser.ConfigParser()
        conf.read(file_name, encoding='UTF-8')
        self.go = conf.get('EMAIL', 'go')
        self.to = conf.get('EMAIL', 'to')
        self.code = conf.get('EMAIL', 'code')
        self.themo = conf.get('EMAIL', 'theme')
        self.text = conf.get('EMAIL', 'text')

    def email_to(self, fp):
        '''
        发送邮件的参数
        :return:
        '''
        msg = MIMEMultipart()
        msg['Subject'] = self.themo
        msg['From'] = self.go
        msg['To'] = self.to
        try:
            mail_text = MIMEText(self.text)  # 发送邮件的正文
            msg.attach(mail_text)
            now = time.strftime('%Y-%m-%d %H_%M')  # 时间戳
            html_path = now + '.html'

            part = MIMEApplication(open(fp, 'rb').read(),'utf-8')  #
            part.add_header('Content-Disposition', 'attachment', filename=html_path)
            msg.attach(part)  # 发送附件 html格式

            att = MIMEText(open('C:\\API_DM\\TestData\\data_test.xlsx', 'rb').read(), 'base64', 'utf-8')
            att["Content-Type"] = 'application/octet-stream'
            att["Content-Disposition"] = 'attachment; filename="data_test.xlsx"'
            msg.attach(att)

            s = smtplib.SMTP_SSL("smtp.qq.com", 465)
            s.login(self.go, self.code)
            s.sendmail(self.go, self.to, msg.as_string())
            s.quit()
            return ("发送成功")
        except Exception as e:
            return ('发送失败,报错信息是:{}'.format(str(e)))


if __name__ == '__main__':
    t = Email().email_to('C:\\API_DM\\HtmlTestReport\\2019-12-17 10_39.html')
    print(t)
