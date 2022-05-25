import time
import json
abc1 = 'http://cms.591adb.cn/admin/integrate_activity/index/id/1?page=1&limit=999&filter={"activity_name":"","activity_type":""}'
abc12 = 'http://cms.591adb.cn/admin/integrate_activity/index/id/1?page=1&limit=999&filter={}'
act_type = 1
dict1 = {"activity_name": "", "activity_type": act_type}


url = abc12.format(json.dumps(dict1, ensure_ascii=False))
print(url)
# print(abc12)
# c1 = abc12.format(type1="1")
# print(c1)