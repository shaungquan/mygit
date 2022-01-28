

import datetime
from test_case import weather_test
data = weather_test.weather()
bakdir = "/www/backup/"
daytime = (datetime.datetime.now() + datetime.timedelta(days=0)).strftime("%Y-%m-%d")
def html():
    df_html = "测试表内容"
    df_html1 = ""
    title = "天气预报"
    head = \
        """
        <head>
            <meta charset="utf-8">
            <title>{title}</title>
            <style>
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
            <p align="center">日期:{date}</p>
            <p align="center">发送人：郭双全</p>
            <table class="table1">
            <!---表头-->
            <!---表内容-->
            <th>城市</th><td>{city}</td>
            <tr>
            <th>温度</th><td>{tem}</td>
            <tr>
            <th>风向</th><td>{direct}</td>
            </tr>
            <tr>
            <th>天气</th><td>{wea}</td>
            </tr>
            <tr>
            <th>昼夜温差</th><td>{tem_differ}</td>
            </tr>
            </tr>
            <th>穿衣建议</th><td>{dress_index}</td>
            </tr>
            </table>
        </body>
        """.format(title=title, df_html=df_html, df_html1=df_html1,
                   daytime=daytime,city=data[0], date=data[1],
                   tem=data[2], wea=data[3], direct=data[4],
                   dress_index=data[5], tem_differ=data[6])
    html_msg = "<html>" + head + body + "</html>"

    return html_msg

