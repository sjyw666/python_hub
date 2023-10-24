# coding:utf-8
# author:杨淑娟
import random
target=random.randint(1,100) # 产生1-100之间的随机数
count=0 # 用于统计次数
while True:
    guess=eval(input('请输入一个猜测的整数(1-100):'))
    count=count+1
    if guess>target:
        print('猜大了')
    elif guess<target:
        print('猜小了')
    else:
        print('猜对了')
        break
print('此轮的猜测次数是:',count)

print("--------复习----------")
import random
count=0
random_number=random.randint(1,100)
for i in range(10):#用for循环出现错误，总共就跑了10次，哪怕错了也是10次就结束
    number = eval(input("请输入一个猜测的参数(1~100)"))
    count+=1
    if number>i:
        print("猜大了")
        continue
    elif number<i:
        print("猜小了")
        continue
    else:
        print("猜对了")
        break
print("此轮的猜测次数是：",count)