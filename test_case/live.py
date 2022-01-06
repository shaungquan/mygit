import requests
import json
import time


# '%s'" %
yyid = [
6539,6541,2560,6538,6543,2561,6537,6540,6542,6469,6735,6643,3053,2562,6736,6459,2581,3052,6471,6550,6734,6687,6694,6738]
a1 = len(yyid)
a2 = 0
while a2 <= a1-1:

    if a2 <= a1-1:

        url = f"https://cloud.cn2030.com/sc/wx/HandlerSubscribe.ashx?act=CustomerProduct&id={yyid[a2]}&lat=30.64242&lng=104.04311"

        payload={}
        headers = {
          'Referer': 'https://servicewechat.com/wx2c7f0f3c30d99445/91/page-frame.html',
          'Cookie': 'Cookie_1=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE\
          2Mzg4NjY4NDkuNDUxMzgyNiwiZXhwIjoxNjM4ODcwNDQ5LjQ1MTM4MjYsInN1YiI6Ill\
          OVy5WSVAiLCJqdGkiOiIyMDIxMTIwNzA0NDcyOSIsInZhbCI6ImdhUUpBUUlBQUFBUVp\
          HTmtObUZtTW1VNVpESmlPREJqT1J4dmNYSTFielZOWkhCNFZUTXdjVWhvVG5nMWQyMU9\
          la1pWTm5SM0FCeHZcclxuVlRJMldIUXpValJwUTBzd1dISTJUWE5wZFZreVRFMTNla1Z\
          ORGpFeE55NHhOek11T0RjdU1UZzNBQkJuWVZGS1FWUTJXVUZCUVVsYVxyXG5hbEZDQVF\
          BQUFBQT0ifQ.yhOu-4TYzK7N4YHqgjldoOkc_qMKprXlKPuoKUAzn7w'
        }
        # 九价人乳头瘤病毒疫苗
        response = requests.request("GET", url, headers=headers, data=payload)
        time.sleep(3)
        a = json.loads(response.text)
        b = int(len(a['list']))
        c = 0
        while c <= b:
            if c <= b:
                if a['list'][c]['text'] == '九价人乳头瘤病毒疫苗':
                    if a['list'][c]['date'] != '暂无':
                        print(a['cname']+":"+a['list'][c]['date'])
                    break
            c += 1
    a2 += 1
print("结束搜索")


