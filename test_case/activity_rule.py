import requests
import json
import random
from config import  url_message
def study_rule(activity_id, app_id=1, group_switch='', recom_switch=''):

    # 获取书籍id
    def books_data():
        url = url_message.books_data_url.format(app_id, activity_id)
        head = {
            'cookie': url_message.cookie1,
            'X-Requested-With': 'XMLHttpRequest'

        }
        try:
            data = requests.request("GET", url, headers=head)
            datas = json.loads(data.text)
            # print(datas['data'])
            print("获取书籍信息成功！")
            return datas['data']
        except Exception as e:
            print("呀！获取书籍信息失败了！请检查url是否正确！", e)
            return "false"

    # 配置共读活动规则
    def rule(group_switch=group_switch, recom_switch=recom_switch, leader_name='', leader_identity='', recommend_reason=''):
        '''
        :param group_switch:是否开启小组，默认关闭，传任意参数打开
        :param recom_switch:是否开启团长推荐，默认关闭，传任意参数打开
        :param leader_name: 团长姓名
        :param leader_identity:团长身份信息
        :param recommend_reason:团长推荐理由
        :return:
        '''
        print("正在配置规则……")
        book_data = books_data()
        if book_data != "false":
            resource_p_id = book_data[0]['r_id']
            resource = book_data[0]['r_name']
            if group_switch != '':
                group_switch = 1
            if recom_switch != '':
                recom_switch = 1
            # 随机生成团长信息
            if recom_switch == 1:
                leader_name = unicode(3)
                leader_identity = unicode(10)
                recommend_reason = unicode(15)
            url = url_message.study_activity_url
            payload = {'group_switch': group_switch,
                       'recom_switch': recom_switch,
                       'leader_name': leader_name,
                       'leader_identity': leader_identity,
                       'recommend_reason': recommend_reason,
                       'resource': resource,
                       'resource_p_id': resource_p_id,
                       'app_id': app_id,
                       'active_id': activity_id}
            headers = {
                'X-Requested-With': 'XMLHttpRequest',
                'cookie': url_message.cookie1
            }

            response = requests.request("POST", url, headers=headers, data=payload)
            try:
                datas = json.loads(response.text)
                if datas['code'] == 1 and datas['msg'] == "保存成功":
                    print("规则配置成功!")
            except Exception as e:
                print("呀！配置规则失败了，请检查url是否正确", e)
        else:
            return book_data

    rule()


def groups(activity_id, num=2):
    print("正在添加小组……")
    # print(activity_id)
    num1 = 0
    while num1<=num:
        url = url_message.group_url.format(activity_id)
        group_name = unicode(3)
        headers = {
            'cookie': url_message.cookie1,
            'X-Requested-With': 'XMLHttpRequest'
        }
        payload = {
            'group_name': group_name
        }
        try:
            response = requests.request("POST", url, headers=headers, data=payload)
            num1 = num1+1
        except Exception as e:
            print("呀！添加小组失败，请检查url是否正确！", e)
    message = json.loads(response.text)
    if message['code'] == 1 and message['msg'] == "保存成功":
        print("已成功添加3小组!")


# 随机生成文字
def unicode(num=1):
    num1 = 0
    str1 = ""
    while num1 < num:
        val = chr(random.randint(0x4e00, 0x9fbf))
        str1 = str1+val
        num1 = num1+1
    return str1

# groups(activity_id=138)

# study_rule(138)
