# coding:utf-8
# author:杨淑娟
# input内置函数是进行键盘输入
name=input('请输入您的姓名:') # 小括号中的是文本提示，这个文本提示，可写可不写，但是建议大家是要写上，因为不写不够友好
                 # 提示文本不写，不够友好，因为客户不知道要做什么

# 从键盘中输入的 任何数据都是字符串类型
# 可以使用内置函数type()查看数据的类型
age=input('请输入您的年龄:')
score=input('请输入您的成绩:')
print(name,'的数据类型是:',type(name))
print(age,'的数据类型是:',type(age))
print(score,'的数据类型是:',type(score))
# 内置函数eval()改变数据字符，通常与input一起使用，将字符串转成实际的数据类型
age2=eval(input('请再次输入您的年龄：'))
print(age2,'的数据类型:',type(age2))
print(score,'的数据类型:',type(eval(score))) #将数字串98.5转成了float 类型的98.5