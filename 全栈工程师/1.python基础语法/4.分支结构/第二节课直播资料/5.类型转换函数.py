# coding:utf-8
# author:杨淑娟
# int()转成int类型
print(int('98')+int('2')) # 将字符串转成int类型,之后进行加法运算
print(int(98.9)) #将float类型转成int类型
# 这种情况不能转
#print(int('98.5')) # ValueError: invalid literal for int() with base 10: '98.5'

# float()函数
print(float(98)+float('98.2'))

# str()将任何类型转成字符串类型
a={'aa:':100}
print(a,'的数据类型是:',type(a))
s=str(a) # 将a转成了字符串类型
print(s,'的数据类型是:',type(s))
# eval()将字符串转成真实的数据类型
x=eval('{"a":100}') # 将str转成了实际的数据类型
print(x,'的数据类型是:',type(x))
