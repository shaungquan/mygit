import requests
import pytest
import json
from common.yaml_util import YamlUtil


class TestSendRequest:
    session = requests.session()
    app_key = "da6a9d132a861f28bd6e8c1b8b31f422"
    identify_key = "3a58782c204aef4cb984f8e4a1e682f9"

    def test_login(self, pw_encryption):
        pw = pw_encryption
        user_name = "18281740124"
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
        # 字典转字符串，禁止中文转Unicode格式
        va = json.dumps(param, ensure_ascii=False)
        # # 去掉字符串中的空格
        va1 = ''.join(va.split())
        url = "http://apis.183read.cc/open_api5/rest6.php?act=member.user.enter&param={}".format(va1)
        print("这是url：", url)
        re = TestSendRequest.session.request("post", url=url, headers=headers)
        YamlUtil().write_excract_yaml({"token": re.json()["result"]["member_info"]["token"]})
        print(re.json())

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

