import smtplib
from email.mime.text import MIMEText
from email.header import Header
import re

de_from = '测试部门'
de_to = '测试郭双全'
de_receivers = '89398664@qq.com'
# 校验邮箱格式
ex_email = re.compile(r'^[\w][a-zA-Z1-9.]{4,19}@[a-zA-Z0-9]{2,3}.[com|gov|net]')
def smtp(subject1,body1,From1=de_from,To1=de_to,receive=de_receivers):
    '''
    :param subject: 主题，必填项
    :param body: 文本内容，必填项
    :param From:发件人，可选，默认测试部门
    :param To:收件人，可选。默认测试郭双全
    :param receive:接收邮箱，默认89398664@qq.com
    :return:邮件成功或者发送失败
    '''

    subject = subject1  # 主题
    heand = body1   # 内容
    From = From1    # 发件人
    To = To1    # 收件人
    # 第三方 SMTP 服务
    mail_host = "smtp.qq.com"  # 设置服务器
    mail_user = "89398664@qq.com"  # 用户名
    mail_pass = "ltujpiqclccobgge"  # 口令

    sender = '89398664@qq.com'
    receivers = receive  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    result = ex_email.match(receivers)
    if not result:
        return print("邮箱格式有误，请检查后重新输入")
    message = MIMEText(heand, 'plain', 'utf-8')
    message['From'] = Header(From, 'utf-8')
    message['To'] = Header(To, 'utf-8')


    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException as e:
        print("Error: 无法发送邮件", e)




