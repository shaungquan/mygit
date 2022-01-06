import requests
import json
url = "https://cloud.cn2030.com/sc/wx/HandlerSubscribe.ashx?act=CustomerProduct&id=6537&lat=30.64242&lng=104.04311"

payload={}
headers = {
  'Referer': 'https://servicewechat.com/wx2c7f0f3c30d99445/91/page-frame.html',
  'Cookie': 'Cookie_1=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2Mzg4NjY4NDkuNDUxMzgyNiwiZXhwIjoxNjM4ODcwNDQ5LjQ1MTM4MjYsInN1YiI6IllOVy5WSVAiLCJqdGkiOiIyMDIxMTIwNzA0NDcyOSIsInZhbCI6ImdhUUpBUUlBQUFBUVpHTmtObUZtTW1VNVpESmlPREJqT1J4dmNYSTFielZOWkhCNFZUTXdjVWhvVG5nMWQyMU9la1pWTm5SM0FCeHZcclxuVlRJMldIUXpValJwUTBzd1dISTJUWE5wZFZreVRFMTNla1ZORGpFeE55NHhOek11T0RjdU1UZzNBQkJuWVZGS1FWUTJXVUZCUVVsYVxyXG5hbEZDQVFBQUFBQT0ifQ.yhOu-4TYzK7N4YHqgjldoOkc_qMKprXlKPuoKUAzn7w'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
a = json.loads(response.text)
b = int(len(a['list']))
print(b)
c = 0
while c <= b:
    if c <= b:
        if a['list'][c]['text'] == '九价人乳头瘤病毒疫苗':
            print(a['cname']+":"+a['list'][c]['BtnLable'])
            break
    c += 1