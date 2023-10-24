import random
money=eval(input('请输入红包金额'))
num=eval(input('请输入红包个数:'))

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


print("随机分配的红包金额：")
for amount in s:
    print(f"{amount / 100:.2f}元")  # 将分转换成元并打印
