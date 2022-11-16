import pytest
import hashlib
import base64
from common.yaml_util import YamlUtil


@pytest.fixture(scope="function")
def conn_database():
    print("这是前置条件")
    yield
    print("这是后置条件")


@pytest.fixture(scope="session", autouse=True)
def clear_yaml():
    YamlUtil().clear_excract_yaml()


# 密码加密
data = YamlUtil().read_tesecase_yaml("login.yml")
@pytest.fixture(scope="function")
def pw_encryption(request):
    pw = request.param['request']['data']['password']
    pw1 = ""
    if pw != None:
        h1 = hashlib.md5()
        h1.update(pw.encode('utf-8'))
        d1 = h1.digest()  # 返回二进制数据字符串值
        pw1 = base64.b64encode(d1).decode('utf-8')
    return pw1
    # return request.param
