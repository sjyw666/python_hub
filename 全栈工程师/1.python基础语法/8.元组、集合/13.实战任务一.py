#研发者：时间遗忘
#开发时间：2023/5/4 20:35
#携程机票界面：选择次数无限制，出发地和目的地不能相同，输入登录和账号有次数限制
'''
选择单程/往返--》
打印所有出发地（列表）--》选择出发地（根据索引取值）--》打印所有目的地（列表）--》选择目的地--》
出发地和目的地不能相同，相同时会提示while循环--》
字典嵌套字典
打印出发地和目的地（列表的遍历，修改序号），单程/往返，可选择航班信息（字典）--》
字典（1）的键是出发地 -目的地，值的类型是字典（2）类型，
字典（2）的键是单程/往返、键的类型是（总的）列表（单个列表元素也是列表，里面包含的是单个班次信息）双重列表，使用二重循环去遍历
判断是单程还是往返的情况（通过判断索引是否相同）
是否预定--》输入用户名和密码，输错三次退出（for循环）--》
打印机票信息--》输入出行人数、出行人--》
输入支付价格--》选择支付方式--》
祝您旅途愉快
'''
print("----------------------------携程旅行---------------------------------")


number_of_times_input=eval(input("请选择班次：1、单程  2、往返"))

if number_of_times_input==1:
    number_of_times="单程"
    print("已选择“单程”")
elif number_of_times_input==2:
    number_of_times="往返"
    print("已选择“往返”")
else:
    print("输入有误，请重新输入")
    while number_of_times_input != 1 or number_of_times_input != 2:
        number_of_times_input = eval(input("请选择班次：1、单程  2、往返"))
        if number_of_times_input==1:
            number_of_times="单程"
            print("已选择“单程”")
            break
        elif number_of_times_input==2:
            number_of_times="往返"
            print("已选择“往返”")
            break
        else:
            print("输入有误，请重新输入")





print("-"*70)
print("出发地：")
print("-"*70)
place_of_departure_list=["北京(BJS)","上海(SHA)","长春(龙嘉国际机场)(CGQ)"]
for Serial_Number,item in enumerate(place_of_departure_list,start=1):
    print(Serial_Number,item)
place_of_departure_input=eval(input("请选择出发地："))


print("-"*70)
print("目的地：")
print("-"*70)
destination_list=["北京(BJS)","上海(SHA)","长春(龙嘉国际机场)(CGQ)"]
for Serial_Number2,item in enumerate(place_of_departure_list,start=1):
    print(Serial_Number2,item)
destination_input=eval(input("请选择目的地："))


while place_of_departure_list[place_of_departure_input-1]==destination_list[destination_input-1]:
    print("出发地和目的地不能相同")
    place_of_departure_input = eval(input("请重新选择出发地："))
    destination_input = eval(input("请重新选择目的地："))





print("-"*70)
print("出发地：",place_of_departure_list[place_of_departure_input-1],"\t\t目的地：",destination_list[destination_input-1])
print("-"*70)


All_flight_information={
    "北京(BJS)-上海(SHA)":{
                            "单程":[['中国国航','CA1661 空客320(中)','20:00','21:55','首都国际机场T3','龙嘉国际机场T2',270,'经济舱1.3折'],
                                  ['海南航空','HU7101 波音737(中)','19:15','21:10','首都国际机场T2','龙嘉国际机场T2',298,'经济舱1.5折']],
                            "往返":[['中国国航','CA1661 空客320(中)','20:00','21:55','首都国际机场T3','龙嘉国际机场T2',504,'往返总价'],
                                  ['海南航空', 'HU7101 波音737(中)', '19:15', '21:10', '首都国际机场T2', '龙嘉国际机场T2', 536, '往返总价']]
                        },
    "北京(BJS)-长春(龙嘉国际机场)(CGQ)":{
                                        "单程":[['海南航空','HU7335 波音737(中)','23:05','01:45','首都国际机场T2','黄花国际机场T2',700,'经济舱4折'],
                                              ['厦门航空','CZ6137 空客320(中)','07:40','10:10','大兴国际机场','黄花国际机场T2',730,'经济舱3.8折']],
                                        "往返":[['河北航空','NS8061 波音737(中)','09:00','11:35','大兴国际机场','黄花国际机场T2',1020,'往返总价'],
                                              ['海南航空','HU7335 波音737(中)','23:05','01:45','首都国际机场T2','黄花国际机场T2',1195,'往返总价']]
                                    },
    "上海(SHA)-北京(BJS)":{
                            "单程":["暂无"],
                            "往返":["暂无"]
                        },
    "上海(SHA)-长春(龙嘉国际机场)(CGQ)":{
                            "单程":["暂无"],
                            "往返":["暂无"]
                        },
    "长春(龙嘉国际机场)(CGQ)-北京(BJS)":{
                            "单程":["暂无"],
                            "往返":["暂无"]
                        },
    "长春(龙嘉国际机场)(CGQ)-上海(SHA)": {
                            "单程":["暂无"],
                            "往返":["暂无"]
    }
}

Flight_Information_Dictionary1=All_flight_information.keys()#通过获取字典的key将所有的出发地到目的地赋予一个变量

for item in Flight_Information_Dictionary1:#再遍历这个变量
    '''
    item=
    北京(BJS)-上海(SHA)
    北京(BJS)-长春(龙嘉国际机场)(CGQ)
    上海(SHA)-北京(BJS)
    上海(SHA)-长春(龙嘉国际机场)(CGQ)
    长春(龙嘉国际机场)(CGQ)-北京(BJS)
    长春(龙嘉国际机场)(CGQ)-上海(SHA)
    '''

    if place_of_departure_list[place_of_departure_input-1]+"-"+destination_list[destination_input-1]==item:#输出选中的航班

        ways = All_flight_information.get(item)# 根据key获取值 key 是  “出发地-目的地”得到 一个字典 { '单程':[],'往返':[]}
        # 单程情况
        if number_of_times == list(ways.keys())[0]:  # list(ways.keys()) 获取所有的键 ，转成列表类型[ '单程','往返'] ,单程的索引是0，返往的索引是1
                                                     # 同时选择输出规定的航班次数对应的航班信息
            print('单程')
            print('-' * 70)

            plane_list = ways.get('单程')  # 根据key获取值  ，获取到的是一个二维列表[[第一个航班信息],[第二个航班信息]]

            index = 1
            print('序号\t航空公司\t\t\t机型\t\t\t起飞时间\t抵达时间\t\t起飞机场\t\t到达机场\t\t\t价格\t\t折扣')
            # 遍历二维列表
            for item in plane_list:  # item是航 班信息
                print(index, end='\t')    #\t控制输出序号和信息不换行
                for plane in item:  # 航班详情信息
                    print(plane, end='\t')
                index += 1
                print()  #输出完一条航班信息换行

        # 往返情况
        elif number_of_times==list(ways.keys())[1]:
            print('往返')
            print('-' * 70)
            plane_list = ways.get('往返')
            index = 1
            print('序号\t航空公司\t\t\t机型\t\t\t起飞时间\t抵达时间\t\t起飞机场\t\t到达机场\t\t\t价格\t类型')
            for item in plane_list:
                print(index, end='\t')
                for plane in item:
                    print(plane, end='\t')
                index += 1
                print()
        print('-' * 70)





for i1 in plane:
    pass




'''打印机票信息--》输入出行人数、出行人--》
输入支付价格--》选择支付方式--》'''
Yes_No=input("是否预定：y/n")
if Yes_No=="y":
    i=0
    while i<3:
        user_name = input("请输入账户名：")
        PassWord = eval(input("请输入账户密码："))
        if user_name == "zhao" and PassWord == 123456:
            plane_select = eval(input("请选择需要选择的机票：（输入序号）"))

            plane_select_information = plane_list[plane_select - 1]  # 请问航班号为什么减1  ，pt代表是一个航 班信息，列表
            print("已选择" + plane_select_information[0] + "公司")

            print('您选择的航号信息如下:')
            print('-' * 70)
            print('航空公司:', plane_select_information[0])  # 列表可以根据索引取值
            print('机型:', plane_select_information[1])
            print('起飞时间:', plane_select_information[2])
            print('到达时间:', plane_select_information[3])
            print('起飞机场:', plane_select_information[4])
            print('抵达机场:', plane_select_information[5])
            print('票价:￥', plane_select_information[6])
            print('折扣:', plane_select_information[7])

            Payment_method = eval(input("请选择您的支付方式：1、微信  2、支付宝  3、银行卡"))
            if Payment_method == 1:
                print("已选择微信支付，需支付",plane_select_information[6],"元")
                print("已支付",plane_select_information[6],"元，祝您旅途愉快")
                break
            elif Payment_method == 2:
                print("已选择支付宝支付，需支付",plane_select_information[6],"元")
                print("已支付"+plane_select_information[6]+"元，祝您旅途愉快")
                break
            elif Payment_method == 3:
                print("已选择银行卡支付，需支付",plane_select_information[6],"元")
                print("已支付",plane_select_information[6],"元，祝您旅途愉快")
                break
            else:
                print("输入错误，已取消支付")
                break
        else:
            i+=1
            if i < 3:
                print("账号或密码错误，请重新输入")
            elif i == 3:
                print("账号或密码输错三次，已取消订单")
                break
else:
    print("已取消预订")


