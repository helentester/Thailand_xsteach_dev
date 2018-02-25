# coding:utf-8
__author__ = 'Helen'
'''
description:邮件发送最新的测试报告
'''
import os,smtplib,os.path
from config import globalparameter as gl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from src.common import log


class send_email:
    def __init__(self):
        self.mylog = log.log()

    # 定义邮件内容
    def email_init(self,report,reportName):
        with open(report,'rb')as f:
            mail_body = f.read()

        # 创建一个带附件的邮件实例
        msg = MIMEMultipart()
        # 以测试报告作为邮件正文
        msg.attach(MIMEText(mail_body,'html','utf-8'))
        report_file = MIMEText(mail_body,'html','utf-8')
        # 定义附件名称（附件的名称可以随便定义，你写的是什么邮件里面显示的就是什么）
        report_file["Content-Disposition"] = 'attachment;filename='+reportName
        msg.attach(report_file) # 添加附件
        msg['Subject'] = '泰国官网自动化测试报告:'+reportName # 邮件标题
        msg['From'] = gl.email_name  #发件人
        msg['To'] = gl.email_To  #收件人列表
        try:
            server = smtplib.SMTP(gl.smtp_sever)
            server.login(gl.email_name,gl.email_password)
            server.sendmail(msg['From'],msg['To'].split(';'),msg.as_string())
            server.quit()
        except smtplib.SMTPException:
            self.mylog.error(u'邮件发送测试报告失败 at'+__file__)

    def sendReport(self):
        # 找到最新的测试报告
        report_list = os.listdir(gl.report_path)
        report_list.sort(key=lambda fn: os.path.getmtime(gl.report_path+fn) if not os.path.isdir(gl.report_path+fn) else 0)
        new_report = os.path.join(gl.report_path,report_list[-1])
        # 发送邮件
        self.email_init(new_report,report_list[-1])
