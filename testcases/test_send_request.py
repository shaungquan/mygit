import requests
import pytest
import json

import encryption
from common.yaml_util import YamlUtil
import hashlib
import base64


# 加密密码
def pw_encryption(pw=None):
    h1 = hashlib.md5()
    h1.update(pw.encode('utf-8'))
    d1 = h1.digest()  # 返回二进制数据字符串值
    return base64.b64encode(d1).decode('utf-8')


class TestSendRequest:
    session = requests.session()
    app_key = "da6a9d132a861f28bd6e8c1b8b31f422"
    identify_key = "3a58782c204aef4cb984f8e4a1e682f9"
    @pytest.mark.parametrize("caseinfo", YamlUtil().read_tesecase_yaml('login.yml'))
    # @pytest.mark.parametrize("pw_encryption", YamlUtil().read_tesecase_yaml('login.yml')[0], indirect=True)
    def test_login(self, caseinfo):
        pw = encryption.common().pw_encryption(caseinfo['request']['data']['password'])
        print("这是", pw)
        pw = pw_encryption(caseinfo['request']['data']['password'])
        user_name = caseinfo['request']['data']['user_name']
        method = caseinfo['request']['method']
        ces = caseinfo['validata']
        print(ces)
        param = {
            "app_key": TestSendRequest.app_key,
            "identify_key": TestSendRequest.identify_key,
            "is_new": 0,
            "login_type": "2",
            "password": pw,
            "platform": "1",
            "user_name": user_name
}
        headers = {
            'X-Requested-With': 'XMLHttpRequest',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        # 字典转字符串，禁止中文转Unicode格式11
        va = json.dumps(param, ensure_ascii=False)
        # # 去掉字符串中的空格
        va1 = ''.join(va.split())
        url = "http://apis.183read.cc/open_api5/rest6.php?act=member.user.enter&param={}".format(va1)
        re = TestSendRequest.session.request(method, url=url, headers=headers)
        print("这是返回的数据：", re.json())
        if "member_info" in re.json()["result"]:
            YamlUtil().write_excract_yaml({"token": re.json()["result"]["member_info"]["token"]})
        else:
            assert caseinfo['validata'] == re.json()['result']['status_info']['status_message']
    def test_base(self):
        token = YamlUtil().read_extract_yaml("token")
        param = {
            "app_key": TestSendRequest.app_key,
            "identify_key": TestSendRequest.identify_key,
            "is_new": 0,
            "page_limit": "10",
            "page_num": "1",
            "platform": "1",
            "token": token
        }
        # 字典转字符串，禁止中文转Unicode格式
        va = json.dumps(param, ensure_ascii=False)
        # # 去掉字符串中的空格
        va1 = ''.join(va.split())
        url = "http://apis.183read.cc/open_api5/rest6.php?act=member.user.comment.list&param={}".format(va1)
        headers = {
            'X-Requested-With': 'XMLHttpRequest',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        re = TestSendRequest.session.request("get", url=url, headers=headers)
        print(re.json())

