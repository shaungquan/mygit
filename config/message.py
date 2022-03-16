import json


# 后台地址信息
# 测试后台
# domain_name = 'cms'
# 正式后台
domain_name = 'wms'
cookie1 = 'PHPSESSID=gjg1r6o1lopfm564fj0b3q0s90; acw_tc=2760823b16450787547277466e53a7087b60821c89ce0672fbfb6fa03e6603'
create_activity_url = 'https://{}.591adb.cn/admin/integrate_activity/add/app_id/1'.format(domain_name)  # 创建活动接口
put_cover_url = 'https://{}.591adb.cn/admin/integrate_activity/upimage/app_id/1/id/'.format(domain_name)  # 上传封面
study_activity_url = 'https://{}.591adb.cn/admin/integrate_activity/addresource'.format(domain_name)     #配置共读活动规则

# 需要单独修改域名的url
group_url ='https://wms.591adb.cn/admin/integrate_activity/addreadinggroup/app_id/1/id/{}'
books_data_url = 'https://wms.591adb.cn/admin/integrate_activity/searchresource/app_id/{}/active_id/{}/module_type/3?page=1&limit=1'
get_id_url = "https://wms.591adb.cn/admin/integrate_activity/index/id/1?page=1&limit=15&filter={}"  # 搜索活动获取活动id


cover_path = 'C:/Users/Administrator/PycharmProjects/pytest-test/picture/330186.jpg'
banner_path = 'C:/Users/Administrator/PycharmProjects/pytest-test/picture/690240.jpg'


# 数据库信息
user = 'root'
password = '1029@guo..'
host = 'localhost'
database = 'guo_1029'
