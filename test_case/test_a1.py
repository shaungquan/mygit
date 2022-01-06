# file_name: test_abc.py
import pytest # 引入pytest包
import json
import requests

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



def test_a(): # test开头的测试函数
    print("------->test_a")
    text1=message()
    text = json.loads(text1)
    print('调试test_a')
    assert '请输入用户名' in text['msg'] # 断言成功
def test_b():
    print("------->test_b")
    text1=message('测试')
    text = json.loads(text1)
    assert '请输入手机号码' in text['msg'] # 断言成功
if __name__ == '__main__':
       pytest.main(["-s","test_abc.py"]) # 调用pytest的main函数执行测试


