import requests
import json
from jmeter.Smtp import maile
def test(username,phonenumber):
    url = "http://wwwz.bzzb.tv/comments/add"

    payload={'username': username,
    'phonenumber': phonenumber,
    'message': '',
    'formImg': ''}
    files=[

    ]
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    try:
        text = json.loads(response.text)
        print(text['msg'])
        maile().smtp('主题', response.text, '发件人', '收件人')
    except TypeError as e:
        print(e,"打印失败")
        maile().smtp('主题', e, '发件人', '收件人')

def message(username='',phonenumber=''):
    url = "http://wwwz.bzzb.tv/comments/add"

    payload={'username': username,
    'phonenumber': phonenumber,
    'message': '',
    'formImg': ''}
    files=[

    ]
    headers = {}
    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    return response.text


