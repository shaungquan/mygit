

import datetime

from email.mime.text import MIMEText
from email.header import Header
import smtplib
from smtplib import SMTP_SSL

bakdir = "/www/backup/"
daytime = (datetime.datetime.now() + datetime.timedelta(days=0)).strftime("%Y-%m-%d")
def html():
    df_html = "测试表内容"
    df_html1 = ""
    title = ""
    jianyi = '穿衣建议'
    head = \
        """
        <head>
            <meta charset="utf-8">
            <title>{title}</title>
            <style>
                .body1 {{background-image:url("C:/Users/Administrator/PycharmProjects/pytest-test/picture/beijin.jpg")}}
                .table1 td{{text-align:center}}
                .table1{{min-width:500px;font-size:15px;margin:0 auto;}}
                .table1 th,.table1 td{{padding:0px 10px 0px 10px;border:1px solid #fff;}}
                .table1 th{{line-height:40px;}}
                .table1 td,.table1 th{{background-color:#ABCDEF;color:#333;line-height:34px;}}
                .h31{{text-align:center;color:#06C;}}
                .table1 th{{white-space:nowrap;overflow:hidden;text-align:center}}
            </style>
        </head>
        """.format(title=title)

    body = \
        """
        <body class=""body1>
            <h2 class="h31">{title}</h2>
            <p align="center">天气预报:{daytime}</p>
            <p align="center">发送人：郭双全</p>
            <table class="table1">
            <!---表头-->
            <!---表内容-->
            <th>城市</th>
            <td>成都</td>
            <tr>
            <th>温度</th>
            <td>-15-19</td>
            <tr>
            <th>风向</th>
            <td>东南风</td>
            </tr>
            <tr>
            <th>天气</th>
            <td>多云</td>
            </tr>
            <tr>
            <th>昼夜温差</th>
            <td>问题不大</td>
            </tr>
            </tr>
            <th>{jianyi}</th>
            <td font-size:60px>天气极热，适宜着丝麻、轻棉织物制作的短衣、短裙、薄短裙、短裤等夏季服装。午后尽量减少户外活动，高温条件下作业和露天作业人员采取必要防护措施</td>
            </tr>
            </table>
        </body>
        """.format(title=title, df_html=df_html, df_html1=df_html1,daytime=daytime,jianyi=jianyi)
    html_msg = "<html>" + head + body + "</html>"

    return html_msg

def sendmail(html_msg):
    sender = '89398664@qq.com'
    receiver = '89398664@qq.com'
    smtpserver = 'smtp.qq.com'
    username = '89398664@qq.com'
    password = 'ltujpiqclccobgge'
    mail_title = '天气预报'
    message = MIMEText(html_msg, 'html', 'utf-8')
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = Header(mail_title, 'utf-8')

    try:
        smtp = SMTP_SSL(smtpserver)
        smtp.login(username, password)
        smtp.sendmail(sender, receiver, message.as_string())
        print("发送邮件成功！！！")
        smtp.quit()
    except smtplib.SMTPException as e:
        print("发送邮件失败！！！",e)


if __name__ == '__main__':
    html_msg = html()
    sendmail(html_msg)
