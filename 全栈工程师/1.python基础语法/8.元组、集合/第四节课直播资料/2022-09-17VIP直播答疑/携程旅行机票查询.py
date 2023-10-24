# coding:utf-8
# author:杨淑娟
print('-' * 30, '携程旅行', '-' * 30)

print('-' * 70)
way_return = ''  # 出行的类型，是单程 还是往 返

choice = eval(input('请选择：1、单程  2、往返'))

while choice < 1 or choice > 2:  # 条件判断， 不是1和2的时候就循环
    print('选择有误，请重新选择!!!')
    choice = eval(input('请选择：1、单程  2、往返'))  # 因为eval与input一起使用可以进行值的类型转换

# 选择出发地，目的地
if choice == 1:
    way_return = '单程'
else:
    way_return = '往返'

print('-' * 70)
from_city_list = ['北京(BJS)', '上海(SHA)', '西安(SIA)']  # 出发地

to_city_list = ['长春(龙嘉国际机场)(CGQ)', '上海(SHA)', '长沙(CSX)']  # 目的地

print('出发地：')
print('-' * 70)

for index, item in enumerate(from_city_list, start=1):  # 这是列表的第几种输出方式？第三种输出方式，使用了序号，序号从1开始
    print(index, item)  # item是列表内容的输出，不加item或只写item输出结果会加小括号

choice_from_city = eval(input('请选择出发地:'))

print('目的地：')
print('-' * 70)
for index, item in enumerate(to_city_list, start=1):
    print(index, item)
choice_to_city = eval(input('请选择目的地:'))  # 40行到44行可以看得懂吗？

# choice_from_city-1这是什么意思？得到选择项的索引（下标）
# from_city_list[choice_from_city-1] 根据索引取值
# 当出发地和目的地的名称相同时， 无限循环，重新输入出发地和目的地
while from_city_list[choice_from_city - 1] == to_city_list[choice_to_city - 1]:  # 根据索引取值
    print('目的地与出发地不能相同，请重新选择')

    choice_from_city = eval(input('请选择出发地:'))
    choice_to_city = eval(input('请选择目的地:'))  # 52，53两行是循环体，出发地与目的地相同时，要重新选择

print('-' * 70)
print('出发地:', from_city_list[choice_from_city - 1], '目的地:', to_city_list[choice_to_city - 1])
print('-' * 70)
# 大家在写代码的时候，如果可以使用并列结构，就不使用嵌套结构， 因为嵌套的越多越复杂
plane_ticket = {
    '北京(BJS)-长春(龙嘉国际机场)(CGQ)':
        {
            '单程': [['中国国航', 'CA1661 空客320(中)', '20:00', '21:55', '首都国际机场T3', '龙嘉国际机场T2', 270, '经济舱1.3折'],
                   ['海南航空', 'HU7101 波音737(中)', '19:15', '21:10', '首都国际机场T2', '龙嘉国际机场T2', 298, '经济舱1.5折']],
            '往返': [['中国国航', 'CA1661 空客320(中)', '20:00', '21:55', '首都国际机场T3', '龙嘉国际机场T2', 504, '往返总价'],
                   ['海南航空', 'HU7101 波音737(中)', '19:15', '21:10', '首都国际机场T2', '龙嘉国际机场T2', 536, '往返总价']
                   ]
        }
    ,
    '北京(BJS)-上海(SHA)':
        {
            '单程': [['南方航空', 'CZ8889 波音737(中)', '18:45', '21:05', '大兴国际机场', '浦东国际机场T2', 290, '经济舱1.8折'],
                   ['厦门航空', 'MF4701 空客320(中)', '07:30', '09:45', '大兴国际机场', '虹桥国际机场T2', 350, '经济舱2.2折']],
            '往返': [['南方航空', 'CZ8879 波音737(中)', '07:30', '09:45', '大兴国际机场', '虹桥国际机场T2', 590, '往返总价'],
                   ['吉祥航空', 'HO1252 空客320(中)', '14:40', '16:50', '大兴国际机场', '虹桥国际机场T2', 635, '往返总价']]
        }
    ,
    '北京(BJS)-长沙(CSX)':
        {
            '单程': [['海南航空', 'HU7335 波音737(中)', '23:05', '01:45', '首都国际机场T2', '黄花国际机场T2', 700, '经济舱4折'],
                   ['厦门航空', 'CZ6137 空客320(中)', '07:40', '10:10', '大兴国际机场', '黄花国际机场T2', 730, '经济舱3.8折']],
            '往返': [['河北航空', 'NS8061 波音737(中)', '09:00', '11:35', '大兴国际机场', '黄花国际机场T2', 1020, '往返总价'],
                   ['海南航空', 'HU7335 波音737(中)', '23:05', '01:45', '首都国际机场T2', '黄花国际机场T2', 1195, '往返总价']]
        }
    ,
    '上海(SHA)-长春(龙嘉国际机场)(CGQ)':
        {
            '单程': [],
            '往返': []
        }
    ,
    '上海(SHA)-长沙(CSX)':
        {
            '单程': [],
            '往返': []
        }
    ,
    '西安(SIA)-长春(龙嘉国际机场)(CGQ)':
        {
            '单程': [],
            '往返': []
        }
    ,
    '西安(SIA)-上海(SHA)':
        {
            '单程': [],
            '往返': []
        }
    ,
    '西安(SIA)-长沙(CSX)':
        {
            '单程': [],
            '往返': []
        }

}

# 显示机票
for key in plane_ticket.keys():

    # 125行代码在做什么？
    if from_city_list[choice_from_city - 1] + '-' + to_city_list[choice_to_city - 1] == key:

        ways = plane_ticket.get(key)  # 根据key获取值 key 是  “出发地-目的地”得到 一个字典 { '单程':[],'往返':[]}
        # 单程情况
        if way_return == list(ways.keys())[0]:  # list(ways.keys()) 获取所有的键 ，转成列表类型[ '单程','往返'] ,单程的索引是0，返往的索引是1

            print('单程')
            print('-' * 70)

            pt_list = ways.get('单程')  # 根据key获取值  ，获取到的是一个二维列表[[第一个航班信息],[第二个航班信息]]

            index = 1
            print('序号\t航空公司\t\t\t机型\t\t\t起飞时间\t抵达时间\t\t起飞机场\t\t到达机场\t\t\t价格\t\t折扣')
            # 遍历二维列表
            for item in pt_list:  # item是航 班信息
                print(index, end='\t')
                for plane in item:  # 航班详情信息

                    print(plane, end='\t')
                index += 1
                print()

        # 往返情况
        elif way_return == list(ways.keys())[1]:
            print('往返')
            print('-' * 70)
            pt_list = ways.get('往返')
            index = 1
            print('序号\t航空公司\t\t\t机型\t\t\t起飞时间\t抵达时间\t\t起飞机场\t\t到达机场\t\t\t价格\t类型')
            for item in pt_list:
                print(index, end='\t')
                for plane in item:
                    print(plane, end='\t')
                index += 1
                print()

        print('-' * 70)

        answer = input('是否预定:')
        if answer == 'y':
            # 使用到的循环中的for...else结构，循环没有遇到break执行else,遇到break，就不会执行else了
            for i in range(3):
                login_user = input('请输入携程登录名:')
                pwd = input('请输入携程登录密码:')
                if login_user == 'admin' and pwd == 'admin':
                    print('登录成功')
                    print('-' * 70)
                    plane_no = eval(input('请输入航班序号:'))

                    pt = pt_list[plane_no - 1]  # 请问航班号为什么减1  ，pt代表是一个航 班信息，列表

                    print('您选择的航号信息如下:')
                    print('-' * 70)
                    print('航空公司:', pt[0])  # 列表可以根据索引取值
                    print('机型:', pt[1])
                    print('起飞时间:', pt[2])
                    print('到达时间:', pt[3])
                    print('起飞机场:', pt[4])
                    print('抵达机场:', pt[5])
                    print('票价:￥', pt[6])
                    print('折扣:', pt[7])

                    confirm = input('请确认(y/n):')
                    if confirm == 'y':
                        num = eval(input('请输入出行人数:'))
                        name_str = input('请输入出行人（多人之间使用逗号分隔）：')
                        name_lst = name_str.split(',')  # 使用逗号分隔出每个人 ，结果为 列表

                        # 遍历出行人员
                        for name in name_lst:
                            print(name, end='\t')

                        print(f'共{num}人，欢迎您选择:{pt[0]}出行，需要支付:￥{pt[6] * num}元')

                        pay_way = eval(input('请选择支付方式(1.微信  2.支付宝):'))
                        if pay_way == 1:
                            print(f'您已使用微信支付￥{pt[6] * num}元')
                        else:
                            print(f'您已使用支付宝支付￥{pt[6] * num}元')

                    else:
                        print('再见')
                    break
                else:
                    print('登录名或密码不正确，请重新输入!!!')
            else:
                print('对不起，您的账号暂时锁定20分钟！')

        else:
            print('再见')
