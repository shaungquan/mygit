import requests
import hashlib,base64


def pw_encryption(password):
    h1 = hashlib.md5()
    h1.update(password.encode('utf-8'))
    d1 = h1.digest()  # 返回二进制数据字符串值
    return base64.b64encode(d1).decode('utf-8')


def login(user_name, password):
    user_name = user_name
    password = pw_encryption(password)
    params = app_from()
    url = 'http://api.591adb.com/jkb_api/v1/user/login'
    heads = {
            'X-Requested-With': 'XMLHttpRequest',
            'Content-Type': 'application/x-www-form-urlencoded',
            'auth-sign': params['auth-sign'],
            'auth-key': params['auth-key'],
            'auth-nonce': params['auth-nonce'],
            'auth-ts': params['auth-ts']
    }
    data = {
            "login_type": "2",
            "user_name": user_name,
            "sms_code": password,
            "password": "qQZEnVdp+nNh1+zGqj9tKA=="
            }
    rep = requests.post(url=url, json=data, headers=heads)
    print(rep.json())
    return rep.json()['result']['member_info']['token']

# if __name__ == '__main__':
#     pytest.main()





a = pw_encryption('123456abc')
print(a)
