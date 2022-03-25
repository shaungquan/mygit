import pytest
import allure
import requests
import json
import logging
import os
from test_case.test_port.premise import testdata

data = testdata()


def a1(activity_name='', activity_type='', start_time='', end_time='', activity_content=''):
    url = "http://cms.591adb.cn/admin/integrate_activity/add/app_id/1"

    payload = {
        "activity_name": activity_name,
        "activity_type": activity_type,
        "start_time": start_time,
        "end_time": end_time,
        "activity_content": activity_content
    }
    files = [

    ]
    headers = {
        'Cookie': 'PHPSESSID=eqpolipi8beq931mnekv5vsqq1; '
                  'acw_tc=2760777216480932534964372e24b8a5684c4e611eface653ed8f7a8489657',
        'X-Requested-With': 'XMLHttpRequest'
    }

    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    re_data = json.loads(response.text)
    return re_data


class TestCreateActivity:
    @allure.description("活动名称为空是否能创建")
    @pytest.mark.parametrize("activity_name, expect", data['activity_name_null'])
    def test_activity_name_null(self, activity_name, expect):
        re_data = a1(activity_name)
        assert re_data['msg'] == expect
        logging.info(("期望结果:{},实际结果:{}").format(expect, re_data["msg"]))

    @allure.description("活动名称过长是否能创建")
    @pytest.mark.parametrize("activity_name,activity_type,start_time, end_time, activity_content, expect", data['activity_name_long'])
    def test_activity_name_long(self, activity_name, activity_type, start_time, end_time, activity_content, expect):
        re_data = a1(activity_name, activity_type, start_time, end_time, activity_content)
        assert re_data['msg'] == expect

    # @allure.description("传入不存在的数据类型是否能创建成功aaa")
    # @pytest.mark.parametrize("activity_name,activity_type,start_time, end_time, activity_content, expect", data['activity_type_nonentity'])
    # def test_activity_type_nonentity(self,activity_name, activity_type, start_time, end_time, activity_content, expect):
    #     re_data = a1(activity_name, activity_type, start_time, end_time, activity_content)
    #     assert re_data['msg'] ==expect

    @allure.description("开始时间为空是否能创建")
    @pytest.mark.parametrize("activity_name,activity_type,start_time, expect", data['start_time_null'])
    def test_time_null(self, activity_name, activity_type, start_time, expect):
        re_data = a1(activity_name, activity_type, start_time)
        assert re_data['msg'] == expect

if __name__ == '__main__':
    # 执行pytest -q不生成报告,打印用例执行的简略过程
    # pytest.main(["-q", "test_sample.py"])

    # 生成allure报告
    pytest.main(['test_sample.py', '--alluredir', '../../report/tmp', '--clean-alluredir'])
    # os.system('allure generate ../../report/tmp -o ../../report/report --clean-alluredir')
    # 清除上一次生成的报告
    os.system('allure generate ../../report/tmp -o ../../report/report --clean')