# coding: utf-8

import sys
price=0
def sel_target():
    # 因为列表中元素的索引是从0开始，0--》 西安，  1 --》广州   ，2  上海
    from_citys=["西安", "广州", "上海"]
    to_citys=["杭州", "西安", "成都", "北京"]
    from_city=eval(input("请选择起点：1.西安  2.广州  3.上海  "))  # 选择序号，1--》西安，  2--》广州  3，上海
    while from_city<1 or from_city>3:                         # 选择序号比  序引大一，所以要进行在进行列表取值需要 -1
        print("起点有误，请重新选择！！！")
        sel_target()
    to_city = eval(input("请选择起点:1.杭州  2.西安  3.成都  4.北京"))
    while to_city<1 or to_city>4:
        print("终点有误，请重新选择！！！")
        sel_target()
    # 出发地与目的地不能相同
    # from_city是int类型 取值范围 是1，2，3   to_city是int类型，取值范围 是1，2，3，4
    # 出发地  0--》西安，选择序号是会选择1 ，  目的的  1--》西安，  选择序号是会选择2
    #  出发地序号为1   ，目的地序号为2      表示的都是西安， 怎么比较呢？ 目的地序号-1  =1 就与出发地相等了，（不相等的情况下）继续操作
    #if from_city!=to_city-1:    # 出发地不等于目的地
        # 出发地与目的地不相同时，执行下一步的操作，调用一个函数 ，函数传了两个参数， 出发地和目的地
    if from_citys[from_city-1]!=to_citys[to_city-1]:  # 这样更直观一些，根据索引取值之后进行比较
        process_disp(from_citys[from_city-1], to_citys[to_city-1])
    else:
        print("起点和终点一致，请另行选择出行工具..........")
        sel_target() # 出发地与目的地相同时，执行递归操作，  自己调用自己


def process_disp(begin, fin):
    '''
    :param begin:   出发地
    :param fin:    目的地
    :return:  无返回值
    '''
    typ=eval(input("请选择行程：1.单程  2.往返"))
    while typ<1 or typ>2:
        print("行程有误，请重新选择！！！")
        process_disp(begin,fin)  # 递归操作  ，如果输入 的不是1，不是2的话，就进行自己调用自己

    #           begin --出发地,fin -->目的地  typ  出行的类型，  单程还是返回
    disp_tickets(begin, fin, typ) # 调用一个函数

def disp_tickets(begin, fin, typ):
    '''

    :param begin:  出发地
    :param fin: 目的地
    :param typ:  出行的类型  单程 还是往返
    :return:   无返回值
    '''
    global price      # 全局变量 （使用范围整个Python文件）,表示的是价格
    # 从54行开始定义了一个字典  ，出发地作为字典的key, 航班信息作为字典的值，二维列表
    tickers={
        "西安":
            [  # 出发地-目的地  ，起飞机场          抵达机场               飞机型号  起飞时间    抵达时间 单程价格  往返价格
                ["西安 - 杭州", "咸阳国际机场T2", "杭州萧山国际机场T4", "空客A320", "18:00", "22:30", 865.0, 1340],
                ["西安 - 成都", "咸阳国际机场T1", "成都双流国际机场T3", "空客A320", "11:00", "11:40", 320.0, 460],
                ["西安 - 北京", "咸阳国际机场T1", "大兴国际机场T5", "麦道A110", "16:00", "17:40", 430.0, 720.0]
            ],
        "广州":
            [
                ["广州 - 杭州", "广州白云国际机场T2", "杭州萧山国际机场T4", "麦道A110", "18:00", "22:30", 865.0, 1340],
                ["广州 - 西安", "广州白云国际机场T3", "咸阳国际机场T3", "空客A320", "15:00", "17:30", 1030.0, 1860],
                ["广州 - 成都", "广州白云国际机场T2", "成都双流国际机场T3", "空客A350", "16:00", "21:40", 1600.0, 3000.0],
                ["广州 - 北京", "广州白云国际机场T4", "大兴国际机场T5", "麦道A110", "16:00", "17:40", 430.0, 720.0]
            ],
        "上海":
            [
                ["上海 - 杭州", "上海虹口国际机场T2", "杭州萧山国际机场T4", "空客A320", "18:00", "22:30", 865.0, 1340],
                ["上海 - 西安", "上海虹口国际机场T3", "咸阳国际机场T3", "空客A320", "18:00", "22:30", 865.0, 1340],
                ["上海 - 成都", "上海虹口国际机场T2", "成都双流国际机场T3", "空客A320", "11:00", "11:40", 320.0, 460],
                ["上海 - 北京", "上海虹口国际机场T4", "大兴国际机场T5", "空客A320", "16:00", "17:40", 430.0, 720.0]
            ]
    }
    print("行程\t\t\t起飞机场\t\t\t降落机场\t\t\t机型\t\t\t起飞时间\t\t\t降落时间\t\t\t票价")

    for item in range(len(tickers[begin])):  # tickers[beign] 得到出地发，假设，出发地是西安   len(tickers[begin])结果是多少？
#   for  item in  range(3)   :   假设出发地是 西安是的时候    ，item的取值为 0,1,2
         #这是一个字符串的判断  ， 目的地  在   “西安 - 杭州”是否存在
        if fin in tickers[begin][item][0]:  #  假设itme=0时  tickers['西安'][0][0] 得到  “西安 -  杭州”

            # 假设tickers['西安'][0][0]取出来的结果是 “西安 - 杭州”.index('-') 获取"-"的位置+ 1  切片的起始位置
            city2=tickers[begin][item][0][tickers[begin][item][0].index("-")+1:] # [tickers[begin][item][0].index("-")+1:]字符串的切片
            # city2 表示的是目的地
            lst=tickers[begin][item]  # 假设  出发地是“西安”，目的地是杭州  tickers['西安'][0] 得到第一条航班信息
            if city2.strip(" ")==fin:  # 为什么要使用strip(' ')?去除左右的空格 ，因为切片之后的 目的地 带了一个空格 ，只剩“杭州”
                # 单程
                if typ==1:                                           # 单程的价格  索引为6
                    print(lst[0],lst[1],lst[2],lst[3],lst[4],lst[5],lst[6],end="\t")
                    price=lst[6]
                # 往返
                else:                                             # 往返的价格，索引为7
                    print(lst[0],lst[1],lst[2],lst[3],lst[4],lst[5],lst[7],end="\t")
                    price=lst[7]


    print()
    while True:
        booked=input("是否预定？y/n")
        if booked=="y" or booked=="n":
            if booked=="y":
                login()   # 调用了一个登录的函数
                break
            else:
                print("您逗我玩呢........再见！")
                sys.exit()   # 直接退出应用程序
        else:
            print("输入有误，请重新选择！！！")  # 选择的不是y，不是n  ，就重新执行循环

def login():
    acc=input("请输入飞猪网账号：")
    pwd=input("请输入密码：")
    if acc=="admin" and pwd=="0000":
        print(f"欢迎你，{acc}.......")
        judgement_numbers() # 调用确认的函数
    else:
        print("账户信息有误！！！")
        login()                      # 用户名或密码不正确就递归，自己调用 自己，重新登录的操作

def judgement_numbers():
    num=eval(input("请输入乘坐人数："))
    if type(num)==int:
        cash=price*num
        print(f"此次行程需支付 ￥{cash} RMB")
        outcome(cash)     # 支付
    else:
        print("乘坐人数有误！！！")
        judgement_numbers()

def outcome(money):
    kind=eval(input("请选择支付种类：1.支付宝（优惠5元）  2.微信（优惠2元）  3.QQ钱包"))
    if type(kind)==int and 1<=kind<=3:
        if kind==1:
            money-=5
        if kind==2:
            money-=2
        print(f"此次行程最终需支付： ￥ {money} 元！")
    else:
        print("支付种类有误！！！")
        outcome(money)

# 这是函数的调用
sel_target()