
import re

import requests
import json
def weather():
    url = "http://apis.juhe.cn/simpleWeather/query?key=59122dd27c535531937ca925b38e9304&city=成都"

    payload={}
    headers = {
      'Cookie': 'aliyungf_tc=ac5cc29b187ee6db2ef682152862ee3ec0e5d0ac56ae4c54dc10d56700fa953b'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    weather_data = json.loads(response.text)
    if weather_data['error_code'] == 0:
        city = weather_data['result']['city']
        date = weather_data['result']['future'][1]['date']
        tem = weather_data['result']['future'][1]['temperature']
        wea = weather_data['result']['future'][1]['weather']
        direct = weather_data['result']['future'][1]['direct']
        min_tem = int(re.findall('-?\d+', tem)[0])
        max_tem = int(re.findall('-?\d+', tem)[1])
        dress_index = ""
        if max_tem < -15:
            dress_index = "天气寒冷，冬季着装棉衣、羽绒服、冬大衣、皮夹克加羊毛衫"
        elif max_tem >= 25 and max_tem < 5:
            dress_index = "天气冷，冬季着装：棉衣、羽绒衣、冬大衣、皮夹克、毛衣在外罩大衣等；年老体弱者尤其要注意保暖防冻。"
        elif max_tem >= 5 and max_tem < 15:
            dress_index = "天气凉，适宜着一到两件羊毛衫、大衣、毛套装、皮夹克等春秋着装；年老体弱者宜着大衣、夹衣或风衣加羊毛衫等厚型春秋着装。"
        elif max_tem >= 15 and max_tem < 20:
            dress_index = "天气温凉，适宜着夹衣、马甲衬衫、长裤、夹克衫、西服套装加薄羊毛衫等春秋服装。年老体弱者：夹衣或风衣加羊毛衫。"
        elif max_tem >= 20 and max_tem < 25:
            dress_index = "天气暖和，适宜着单层棉麻面料的短套装、T恤衫、薄牛仔衫裤、休闲服、职业套装等春秋过渡装。年老体弱者请适当增减衣服。"
        elif max_tem >= 25 and max_tem < 28:
            dress_index = "天气偏热，适宜着短衫、短裙、短套装、T恤等夏季服装。年老体弱者：单层薄衫裤、薄型棉衫。"
        elif max_tem >= 28 and max_tem < 33:
            dress_index = "天气炎热，适宜着短衫、短裙、短裤、薄型T恤衫、敞领短袖棉衫等夏季服装。"
        else:
            dress_index = "天气极热，适宜着丝麻、轻棉织物制作的短衣、短裙、薄短裙、短裤等夏季服装。午后尽量减少户外活动，高温条件下作业和露天作业人员采取必要防护措施。"
        tem_differ = "昼夜温差小"
        if max_tem-min_tem>=15:
            tem_differ = "昼夜温差大，请注意保暖哟"
        data = []
        data.append(city)
        data.append(date)
        data.append(tem)
        data.append(wea)
        data.append(direct)
        data.append(dress_index)
        data.append(tem_differ)
        return data

    else:
        return weather_data



