import pytest
import allure
import requests
import json
import logging
from allure_commons.types import LinkType
import os
from test_case.test_port.premise import get_data, PublicAactivity, ReadActivityRule
import datetime
# 获取参数化的数据
data = get_data()
# 实例化共读活动
rule = ReadActivityRule()
# 实例化活动
activity = PublicAactivity()

class TestCreateActivity:
    @allure.description("活动名称为空是否能创建")
    @allure.title("活动名称为空")
    @allure.issue('https://www.baidu.com', name="百度")
    @pytest.mark.parametrize("activity_name, expect", data['activity_name_null'])
    def test_activity_name_null(self, activity_name, expect):
        re_data = activity.add_activity(activity_name)
        assert re_data['msg'] == expect
        print("期望结果:{}\n实际结果:{}".format(expect, re_data["msg"]))

    @allure.description("活动名称过长是否能创建")
    @allure.title("活动名称过长")
    # 参数化，调用yaml文件的数据
    @pytest.mark.parametrize("activity_name,activity_type,start_time, end_time, activity_content, expect", data['activity_name_long'])
    def test_activity_name_long(self, activity_name, activity_type, start_time, end_time, activity_content, expect):
        re_data = activity.add_activity(activity_name, activity_type, start_time, end_time, activity_content)
        assert re_data['msg'] == expect
        print("期望结果:{}\n实际结果:{}".format(expect, re_data["msg"]))

    @allure.description("开始时间为空是否能创建")
    @allure.title("开始时间为空")
    @pytest.mark.parametrize("activity_name,activity_type,start_time, expect", data['start_time_null'])
    def test_activity_time_null(self, activity_name, activity_type, start_time, expect):
        re_data = activity.add_activity(activity_name, activity_type, start_time)
        assert re_data['msg'] == expect
        print("期望结果:{}\n实际结果:{}".format(expect, re_data["msg"]))

    @pytest.mark.skip("活动数据太多，暂时跳过此用例")
    @allure.description("正常创建活动")
    @allure.title("正常创建活动")
    @pytest.mark.parametrize("activity_name,activity_type,start_time, end_time, activity_content, expect", data['activity_succeed'])
    def test_activity_succeed(self, activity_name, activity_type, start_time, end_time, activity_content, expect):
        today = datetime.datetime.now()
        start_time = datetime.timedelta(hours=+start_time)
        end_time = datetime.timedelta(days=+end_time)
        start_time = (today + start_time).strftime('%Y-%m-%d %H:%M:%S')
        end_time = (today + end_time).strftime('%Y-%m-%d %H:%M:%S')
        re_data = activity.add_activity(activity_name, activity_type, start_time, end_time, activity_content)
        assert re_data['msg'] == expect
        print("期望结果:{}\n实际结果:{}".format(expect, re_data["msg"]))


# 共读活动规则
class TestReadActivityRule:
    book_data = rule.get_book_data()
    book_id = book_data['book_id']
    book_name = book_data['book_name']

    # 前提条件，先获取未开始的共读活动id
    @pytest.fixture()
    def start_get_act_id(self):
        act_id = activity.get_not_started_activity_id(6)
        print("未开始的活动id:", act_id)
        # yield act_id

    @allure.description("不传活动id")
    @allure.title("活动id为空")
    @pytest.mark.parametrize("expect", data["activity_id_null"])
    def test_activity_id_null(self, expect):
        re_data = rule.rule()
        print("期望结果:{}\n实际结果:{}".format(expect, re_data["msg"]))
        assert re_data['msg'] in expect

    @allure.description("不传书籍信息验证是否能成功保存")
    @allure.title("书籍信息为空")
    @pytest.mark.usefixtures('start_get_act_id')
    @pytest.mark.parametrize("expect", data["book_null"])
    def test_book_null(self, expect, start_get_act_id):
        # actid = get_act_id.get_activity_id()
        re_data = rule.rule(act_id=start_get_act_id)
        print("期望结果:{}\n实际结果:{}".format(expect, re_data["msg"]))
        assert re_data['msg'] in expect

    @allure.description("不传团长姓名验证是否能保存")
    @allure.title("团长姓名为空")
    @pytest.mark.usefixtures('start_get_act_id')
    @pytest.mark.parametrize("expect", data["leader_name_null"])
    def test_leader_name_bull(self, expect, start_get_act_id):
        #
        # self.book_data = rule.get_book_data()
        #
        # self.book_id = self.book_data['book_id']
        # self.book_name = self.book_data['book_name']
        re_data = rule.rule(resource=self.book_name, resource_p_id=self.book_id, recom_switch=1, act_id=start_get_act_id)
        print("期望结果:{}\n实际结果:{}".format(expect, re_data["msg"]))
        assert re_data['msg'] in expect

    @allure.description("团长姓名过长是否能保存")
    @allure.title("团长姓名过长")
    @pytest.mark.usefixtures('start_get_act_id')
    @pytest.mark.parametrize("leader_name, expect", data["leader_name_long"])
    def test_leader_identity_null(self, leader_name, expect, start_get_act_id):
        re_data = rule.rule(resource=self.book_name, resource_p_id=self.book_id, recom_switch=1, act_id=start_get_act_id, leader_name=leader_name)
        print("期望结果:{}\n实际结果:{}".format(expect, re_data["msg"]))
        assert re_data['msg'] in expect


if __name__ == '__main__':
    # 执行pytest -q不生成报告,打印用例执行的简略过程
    # pytest.main(["-q", "test_activity.py"])
    # 生成allure报告
    pytest.main(['test_activity.py', '--alluredir', '../../report/tmp', '--clean-alluredir'])
    # pytest.main(['test_activity.py', '--allure-link-pattern=issue:www.baidu.com/{}', '--alluredir=../../report/tmp', '--clean-alluredir'])
    # pytest.main(['test_activity.py', '--alluredir', '../../report/tmp', '--allure-link-pattern = issue:{}', '--clean-alluredir'])
    # 清除上一次生成的报告
    os.system('allure generate ../../report/tmp -o ../../report/report --clean')