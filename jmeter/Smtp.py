import smtplib
from email.mime.text import MIMEText
from email.header import Header

class maile:
    def smtp(self,subject,body,From,To):
        self.subject = subject  # 主题
        self.heand = body   # 内容
        self.From = From    # 发件人
        self.To = To    # 收件人
        # 第三方 SMTP 服务
        self.mail_host = "smtp.qq.com"  # 设置服务器
        self.mail_user = "89398664@qq.com"  # 用户名
        self.mail_pass = "ltujpiqclccobgge"  # 口令

        self.sender = '89398664@qq.com'
        self.receivers = ['89398664@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

        self.message = MIMEText(self.heand, 'plain', 'utf-8')
        self.message['From'] = Header(self.From, 'utf-8')
        self.message['To'] = Header("研发部门", 'utf-8')


        self.message['Subject'] = Header(self.subject, 'utf-8')

        try:
            smtpObj = smtplib.SMTP()
            smtpObj.connect(self.mail_host, 25)  # 25 为 SMTP 端口号
            smtpObj.login(self.mail_user, self.mail_pass)
            smtpObj.sendmail(self.sender, self.receivers, self.message.as_string())
            print("邮件发送成功")
        except smtplib.SMTPException:
            print("Error: 无法发送邮件")

