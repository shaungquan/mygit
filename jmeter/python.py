
import random
#欧洲球队
Europe_teams = ["俄罗斯","赛尔维亚","法国","德国","比利时","波兰","英格兰","西班牙","葡萄牙","冰岛","瑞士","克罗地亚","瑞典","丹麦"]
#亚洲球队
Asia_teams = ["日本","韩国","伊朗","沙特阿拉伯","澳大利亚"]
#南美洲球队
SouthAmerica_teams = ["阿根廷","哥伦比亚","巴西","乌拉圭","秘鲁"]
#非洲球队
Africa_teams = ["尼日利亚","埃及","塞内加尔","摩洛哥","突尼斯"]
#其它洲球队
others_teams = ["巴拿马","歌斯达黎加","墨西哥"]

#分组情况
group_names = ["A","B","C","D","E","F","G","H"]

while 1:
    #控制跳出循环初始值
    break_num = 0
    # 球队强度梯次
    groups_teams = {"A": [], "B": [], "C": [], "D": [], "E": [], "F": [], "G": [], "H": []}
    # 球队强度梯次
    first_teams = ["俄罗斯", "法国", "比利时", "巴西", "葡萄牙", "波兰", "阿根廷", "德国"]
    second_teams = ["哥伦比亚", "秘鲁", "墨西哥", "西班牙", "乌拉圭", "英格兰", "瑞士", "克罗地亚"]
    thired_teams = ["埃及", "塞内加尔", "伊朗", "丹麦", "冰岛", "突尼斯", "瑞典", "哥斯达黎加"]
    fourth_teams = ["澳大利亚", "韩国", "赛尔维亚", "摩洛哥", "巴拿马", "日本", "沙特阿拉伯", "尼日利亚"]
    for i in range(7):
        while 1:
            #设置统计初始值
            Europe_num,Asia_num,SouthAmerica_num,Africa_num,others_num = 0,0,0,0,0
            if i == 0:
                a = 0
            else:a = random.randint(0,7-i)
            #获取第一梯队队伍，并统计属于哪个州，计算各州球队数量
            new_first_team = first_teams[a]
            if new_first_team in Europe_teams:
                Europe_num+=1
            elif new_first_team in Africa_teams:
                Africa_num+=1
            elif new_first_team in SouthAmerica_teams:
                SouthAmerica_num+=1
            elif new_first_team in Asia_teams:
                Asia_num+=1
            else:
                others_num+=1
            # 获取第二梯队队伍，并统计属于哪个州，计算各州球队数量
            b= random.randint(0,7-i)
            new_second_team = second_teams[b]
            if new_second_team in Europe_teams:
                Europe_num+=1
            elif new_second_team in Africa_teams:
                Africa_num+=1
            elif new_second_team in SouthAmerica_teams:
                SouthAmerica_num+=1
            elif new_second_team in Asia_teams:
                Asia_num+=1
            else:
                others_num+=1
            # 获取第三梯队队伍，并统计属于哪个州，计算各州球队数量
            c = random.randint(0,7-i)
            new_thired_team = thired_teams[c]
            if new_thired_team in Europe_teams:
                Europe_num+=1
            elif new_thired_team in Africa_teams:
                Africa_num+=1
            elif new_thired_team in SouthAmerica_teams:
                SouthAmerica_num+=1
            elif new_thired_team in Asia_teams:
                Asia_num+=1
            else:
                others_num+=1
            # 获取第四梯队队伍，并统计属于哪个州，计算各州球队数量
            d = random.randint(0,7-i)
            new_fourth_team = fourth_teams[d]
            if new_fourth_team in Europe_teams:
                Europe_num+=1
            elif new_fourth_team in Africa_teams:
                Africa_num+=1
            elif new_fourth_team in SouthAmerica_teams:
                SouthAmerica_num+=1
            elif new_fourth_team in Asia_teams:
                Asia_num+=1
            else:
                others_num+=1
            #判断分组情况是否符合条件 ，否则重新开始该次分组
            if  Europe_num in[1,2] and Asia_num<=1 and Africa_num<=1 and SouthAmerica_num<=1 and others_num<=1 :
                #添加第一梯队选中的球队
                groups_teams[group_names[i]].append(first_teams[a])
                # 移除第一梯队选中的球队
                first_teams.remove(first_teams[a])
                # 添加第二梯队选中的球队
                groups_teams[group_names[i]].append(second_teams[b])
                # 移除第二梯队选中的球队
                second_teams.remove(second_teams[b])
                # 添加第三梯队选中的球队
                groups_teams[group_names[i]].append(thired_teams[c])
                # 移除第三梯队选中的球队
                thired_teams.remove(thired_teams[c])
                # 添加第四梯队选中的球队
                groups_teams[group_names[i]].append(fourth_teams[d])
                # 移除第四梯队选中的球队
                fourth_teams.remove(fourth_teams[d])
                # 判断剩余2组第一梯队和第二梯队元素全部属于非洲情况
                if i ==5 and set(first_teams).issubset(SouthAmerica_teams) and set(second_teams).issubset(SouthAmerica_teams):
                    #条件成立，则剩余分组总会有2个南美洲球队，剩余分组会一直失败，跳出循环设置初始值为1
                    break_num = 1
                    break
                #判断剩余2组第三梯队和第四梯队元素全部属于非洲情况
                if i == 5 and set(thired_teams).issubset(set(SouthAmerica_teams)) and set(fourth_teams).issubset(set(SouthAmerica_teams)):
                    #条件成立，则剩余分组总会有2个非洲球队，剩余分组会一直失败，跳出循环设置初始值为1
                    break_num = 1
                    break
                #判断剩余2组第三梯队和第四梯队元素是否没有欧洲球队
                is_tures = set(thired_teams).isdisjoint(set(Europe_teams)) and  set(fourth_teams).isdisjoint(set(Europe_teams))
                if i ==5 and is_tures:
                    #条件成立，剩余分组课正常分组，跳出该次循环
                    break
                #判断剩余2组第一梯队和第二梯队元素是全部是欧洲球队
                if  i == 5 and set(first_teams).issubset(set(Europe_teams))and set(second_teams).issubset(set(Europe_teams)) and is_tures is False:
                    #条件成立，剩余分组总会有3个欧洲球队，剩余分组会一直失败，跳出循环设置初始值为1
                    break_num = 1
                    break

                break
            #判断剩余分组是否成功
            if break_num == 1:
                break
    #判断剩余分组是否成功
    if break_num ==1:
        continue
    #判断最后 一次每个梯次 队伍剩余队伍情况是否符合要求，否则全部重新来过
    Europe_num, Asia_num, SouthAmerica_num, Africa_num, others_num = 0, 0, 0, 0, 0
    groups_teams["H"] = [first_teams[0],second_teams[0],thired_teams[0],fourth_teams[0]]
    for h_team in groups_teams["H"]:
        if h_team in Europe_teams:
            Europe_num += 1
        elif h_team in Africa_teams:
            Africa_num += 1
        elif h_team in SouthAmerica_teams:
            SouthAmerica_num += 1
        elif h_team in Asia_teams:
            Asia_num += 1
    if Europe_num in [1,2] and Asia_num<=1 and Africa_num<=1 and SouthAmerica_num<=1 and others_num<=1:
        break
#按要求输出球队信息
for team in groups_teams:
    print(team+":"+groups_teams[team][0]+" "+groups_teams[team][1]+" "+groups_teams[team][2]+" "+groups_teams[team][3])
