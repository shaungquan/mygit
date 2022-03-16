import requests
import datetime
import json
from config import message
# cookie可能会变化，需要手动登录获取最新cookie

# 新增活动，并通过搜索获取活动id
from test_case import activity_rule


def create_activity(activity_name, activity_type, group_switch='', recom_switch='', start_time=0.33, end_time=7, activity_content='无话可说'):

    """
    :param activity_name: 活动名称
    :param activity_type: 活动类型，6是共读活动
    :param start_time: 开始时间，默认20分钟后开始，传1，说明是1小时后开始，传0，立即开始
    :param end_time: 结束时间，，默认7天后，传1，说明是1天后开始
    :param activity_content: 活动文本
    :return:
    """

    # 格式化开始时间
    def time1():
        today = datetime.datetime.now()
        offset = datetime.timedelta(hours=+start_time)
        re_date = (today + offset).strftime('%Y-%m-%d %H:%M:%S')
        print("格式化开始时间成功!")
        return re_date

    # 格式化结束时间
    def time2():
        today = datetime.datetime.now()
        offset = datetime.timedelta(days=+end_time)
        re_date = (today + offset).strftime('%Y-%m-%d %H:%M:%S')
        print("格式化结束时间成功!")
        return re_date

    # 创建活动
    def create():
        url = message.create_activity_url
        global start_time1
        start_time1 = time1()
        headers = {
          'Cookie': message.cookie1,
          'X-Requested-With': 'XMLHttpRequest'
        }
        bodys = {
            'activity_name': activity_name,
            'activity_type': activity_type,
            'start_time': start_time1,
            'end_time': time2(),
            'activity_content': activity_content
        }

        response = requests.request("POST", url, headers=headers, data=bodys)
        get_data = []
        return_datas = json.loads(response.text)
        try:
            if return_datas['code'] == 1 and return_datas['msg'] == '保存成功':
                get_data.append(activity_name)
                get_data.append(start_time1)
                print("新建活动成功，活动名称为:"+activity_name)
                return get_data
            else:
                return "接口数据返回错误，请检查"
        except Exception as e:
            print('出错了', e)
            return 'false'

    # 通过搜索获取新建活动的id
    def get_id():
        global start_time1
        # time.sleep(10)
        search_datas = {"activity_name": activity_name, "activity_type": activity_type}
        # 格式化url
        url = message.get_id_url.format(json.dumps(search_datas, ensure_ascii=False))
        payload = {}
        headers = {
            'Cookie': message.cookie1,
            'X-Requested-With': 'XMLHttpRequest'
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        try:
            data1 = json.loads(response.text)['data']
            # data1 = datas["data"]
            data_len = len(data1)
            s = 0
            # 循环搜索
            while s < data_len:
                if data1[s]["activity_name"] == activity_name and data1[s]["start_time"] == start_time1:
                    data1 = data1[s]["id"]
                    break
                s = s+1
            return data1
        except Exception as e:
            print('呀！搜素活动ID失败了', e)
            return 'false'

    c1 = create()
    if c1 == 'false':
        print('添加活动失败，请检查cookie或者url是否正确')
        return
    else:
        get_id1 = get_id()
        put_cover(get_id1)
        activity_data = []
        activity_data.append(get_id1)
        activity_data.append(activity_type)
        # 传入活动id调用生成规则配置函数，
        activity_rule.study_rule(get_id1,group_switch=group_switch, recom_switch=recom_switch)
        # 传入活动id调用添加小组函数,判断小组配置是否打开，打开则添加小组
        if recom_switch != '':
            activity_rule.groups(get_id1)
        # 返回新建活动的id和类型
        return activity_data


def put_cover(get_id2):
    print("正在上传封面…………")
    a = str(get_id2)
    url = message.put_cover_url + a
    heads = {'cookie': message.cookie1,
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
                            open(message.cover_path, 'rb'),
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
                            open(message.banner_path, 'rb'),
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
    print("一键上传封面成功!")


# 创建活动，活动类型6为共读，默认开始时间是当前时间+20分钟，默认结束时间是7天后
# recom_switch默认关闭，为任意值是则打开团长推荐
# group_switch默认关闭，为任意值时则打开，创建3个小组
create_activity("测试共读016", "6",)
# 调用上传封面和banner，传活动id即可
# put_cover('140')
