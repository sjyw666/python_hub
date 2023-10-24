# coding:utf-8
# author:杨淑娟
# 祝福语
import random
import time

money=eval(input('请输入红包金额'))
num=eval(input('请输入红包个数:'))
blessing=input('请输入祝福语：') # 如果祝福语为 空，则从默认中随机选一个祝福语
# 第11行是祝福语，使用的是元组,如果不使用元组，可以使用列表，集合，但是为什么使用元组呢？只需遍历，所以不可变对象节省空间
blessings=('万事如意','马到成功','生日快乐','金榜题名','大吉大利')
# 第13行代码，利用了什么性质？Python中每个对象都有一个布尔值这个性质， 空字符串的布尔值为False
if not blessing:    # 如果没有输入祝福语，blessing为空字符串False，对False取反结果为True
    ble=random.choice(blessings) # 随机从元组中抽取一个祝福语
print(ble)

# 18行依然使用了元组，目的是只有遍历不需要增，删，改的，所以元组更合适
friends=('韩梅梅','李雷','白蕊','张三峰','付流水','万里','吴云')  # 这是一个元组  ，表示的是你的微信好友
friends_str=' @ '.join(friends) # 19,20代码可以看得懂吗？
friends_str=' @ '+friends_str  # 为什么还在再加一个？

print(friends_str,'准备抢红包了！！！')


s=set({}) # 这是做什么？可不可以写成 s={}不可以，这样是创建空字典
money=money*100  # 红包的金额为什么乘以100， 将元转成分  元-->分之间的进率是100，相当于1元钱=100分
#  循环是产生随机金额的
for i in range(num-1):  # 为什么要-1？num表示的是红包的个数，为什么要减1，假设5个红包，随机4个就够了，最后一个不用随机数
                         # 最后一个包不用随机，剩多少都最最后一个
    balance=random.randint(1,money)  # 产生一个1到money的随机数，最少是1分钱，包含不包含money？包含

    s.add(balance) # 集合的添加方法，将产生的红包金额 添加到集合中，为什么不使用列表呢？
                          # 因为如果使用列表，最后一个包可能永远是最大的
    money-=balance   # 假设，5元 500分 ，randint(1,500)，假设第一个随机是120分 第二次randint(1,380)


s.add(money) # 最后剩多个，都不需要随机了，直接添到集合中

# 显示抢包金额
name_lst=[]
for item in range(num):   # num 是红包的个数
    name=random.choice(friends)    # 随机取出好友   ，可能会重复
    # while循环排除重复的情况
    while name in name_lst:            # 如果产生的好友在name_list中存在，就需要重新取好友，  抢红包，每人只允许抢一次
        name = random.choice(friends)
    name_lst.append(name) # 将选出的好友放到列表中

#print(name_lst)
#n,p是变量的名称，自定义的
for n,p in zip(name_lst,s):   # 打包输出  使用到发zip
    print(f'{n}抢了{p/100}元')  # 为什么要除以100， 因为要将  “分”--》转’元‘
    time.sleep(2)   # 每执行一次，休眠2秒
