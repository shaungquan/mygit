import pytest
import os
from config import YamlParse
import requests
import json
import datetime


# 获取yaml文件的数据
def get_data(url='activity'):
    testname = YamlParse.YamlParse()
    url = "../../data/{}.yaml".format(url)
    testname.loadyaml(url)
    # testname.loadyaml("../../data/'{}'.yaml").format(url)
    data = testname.getJson()
    return data


class PublicAactivity:
    data = get_data('url_data')

    # 调用创建活动接口
    def add_activity(self,activity_name='',
                     activity_type='',
                     start_time='',
                     end_time='',
                     activity_content=''):
        url = self.data['add_activity']

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
            'Cookie': self.data['cookie'],
            'X-Requested-With': 'XMLHttpRequest'
        }

        response = requests.request("POST", url, headers=headers, data=payload, files=files)
        re_data = json.loads(response.text)
        return re_data


    # 上传banner图和封面图
    def put_cover(self,get_id2):
        print("正在上传封面和banner图……")
        a = str(get_id2)
        url = self.data['put_cover'] + a
        heads = {
                # 'cookie': setting['cookie'],
                'Cookie': self.data['cookie'],
                'X-Requested-With': 'XMLHttpRequest'
            }
        type_id = [2, 13]  # 2为爱读宝H5，13为爱读宝小程序
        category = [1, 2]  # 1为封面，2为banner图
        i = 0
        while i < len(type_id):
            j = 0
            while j < len(category):

                if category[j] == 1:
                    try:
                        files = [
                            ('image_file', (
                                '330186.jpg',
                                open(self.data['cover_path'], 'rb'),
                                'image/jpeg'))
                        ]

                        bodys = {
                            'type_id': type_id[i],
                            'category': category[j]
                            }
                        re = requests.request("POST", url, headers=heads, files=files, data=bodys)
                        re = json.loads(re.text)
                        if re['code'] == 1 and re['msg'] != "上传成功":
                            print("呀！封面图上传失败,", re['msg'])
                            i = i + 1
                            break
                    except Exception as e:
                        print(e)
                        break
                if category[j] == 2:
                    try:
                        files = [
                            ('image_file', (
                                '690240.jpg',
                                open(self.data['banner_path'], 'rb'),
                                'image/jpeg'))
                            ]
                        bodys = {
                            'type_id': type_id[i],
                            'category': category[j]
                            }
                        re = requests.request("POST", url, headers=heads, files=files, data=bodys)
                        re = json.loads(re.text)
                        if re['code'] == 1 and re['msg'] != "上传成功":
                            print("呀！banner图上传失败", re['msg'])
                            break
                    except Exception as e:
                        print(e)
                        break
                j = j + 1
            i = i + 1

        print("H5和小程序banner图和封面上传成功！")


    # 搜索共读活动
    def get_activity_list(self):
        # data = test_data('url_data')
        url = self.data['search_activity']
        payload = {}
        files = []
        headers = {
            'Cookie': self.data['cookie'],
            'X-Requested-With': 'XMLHttpRequest'
        }
        response = requests.request("GET", url, headers=headers, data=payload, files=files)
        re_data = json.loads(response.text)
        return re_data

    # 获取未开始的活动
    def get_not_started_activity_id(self, act_type):
        dict1 = {"activity_name": "", "activity_type": act_type}
        url = self.data['search_activity']
        url = url.format(json.dumps(dict1, ensure_ascii=False))
        payload = {}
        files = []
        headers = {
            'Cookie': self.data['cookie'],
            'X-Requested-With': 'XMLHttpRequest'
        }
        response = requests.request("GET", url, headers=headers, data=payload, files=files)
        re_data = json.loads(response.text)
        a1 = datetime.datetime.now()
        i = 0
        activity_id = ''
        datalen = len(re_data['data'])
        while i < datalen:
            date1 = datetime.datetime.strptime(re_data['data'][i]['start_time'], '%Y-%m-%d %H:%M:%S')
            if a1 <= date1:
                activity_id = re_data['data'][i]['id']
                break
            i += 1
        return activity_id


# 共读活动规则
class ReadActivityRule:
    data = get_data('url_data')
    # act_id = GetActivityId().get_activity_id()
    # 获取未配置的书籍信息

    def get_book_data(self):
        book_list = {}
        url = self.data['get_book_data']
        payload = {}
        files = []
        headers = {
            'Cookie': self.data['cookie'],
            'X-Requested-With': 'XMLHttpRequest'
        }
        response = requests.request("GET", url, headers=headers, data=payload, files=files)
        re_data = json.loads(response.text)
        book_list['book_id'] = re_data['data'][0]['r_id']
        book_list['book_name'] = re_data['data'][0]['r_name']
        return book_list

    def rule(self, group_switch='',
             recom_switch='',
             leader_name='',
             leader_identity='',
             recommend_reason='',
             resource='',
             resource_p_id='',
             app_id=1,
             act_id=''):

        url = self.data['activity_rule']
        payload = {
            "group_switch": group_switch,
            "recom_switch": recom_switch,
            "leader_name": leader_name,
            "leader_identity": leader_identity,
            "recommend_reason": recommend_reason,
            "resource": resource,
            "resource_p_id": resource_p_id,
            "app_id": app_id,
            "active_id": act_id
        }
        files = []
        headers = {
            'Cookie': self.data['cookie'],
            'X-Requested-With': 'XMLHttpRequest'
        }
        response = requests.request("POST", url, headers=headers, data=payload, files=files)
        re_data = json.loads(response.text)
        return re_data



class LuckActivity:
    def rule(self):
        pass
a = PublicAactivity()
b = a.get_not_started_activity_id(6)
print(b)