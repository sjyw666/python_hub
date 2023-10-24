# coding:utf-8
# author:杨淑娟
#1.从键盘录入一个整数，使用循环计算该整数的二进制数并输出。
num=eval(input('请输入一个整数:'))
lst=[]
while num!=0:
    lst.insert(0,num%2)
    num=num//2


for i in lst:
    print(i,end='')


print("--------------自己写的------------")
'''十进制数转换二进制
规律：不断除以2，保留余数，商为0时不再除以2，将所有余数倒叙排列，商为小数的时候商为0，余数为1
商为1时，继续除下去，余数为1
商为0时，余数为1
从商为0的余数开始算二进制
'''
import_number=eval(input("请输入一个数，我会将它转化为二进制数"))
lst=[]
while import_number!=0:
    lst.insert(0,import_number%2)
    import_number=import_number//2

for i in lst:
    print(i,end="")