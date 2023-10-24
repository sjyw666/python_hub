#研发者：时间遗忘
#开发时间：2022/11/12 13:40

'''元组的创建方式'''
'''直接使用（）'''
t=('Python','world',98)#先创建一个小括号，再赋值给一个变量
print(t)
print(type(t))

t1='Pyhton','world',98#第一种方式可以省略小括号
print(t1)
print(type(t1))

t2=('Python')            #只包含一个元素的元组需要加上逗号
t5='Python',             #元组不加逗号就会显示原本的数据类型
print(t2)
print("t5:",t5)
print(type(t2))

t3=('Python',)#加了逗号才显示为元组
print(t3)
print(type(t3))


'''使用内置函数tuple()'''
t4=tuple(('Python','world',98))#小括号里面再加上一个小括号代表元组
                               #然后再赋值给一个变量
print(t4)
print('t4-type',type(t4))


'''空（列表、字典、元组）的创建方式'''
a1=[]
a2=list()

b1={}
b2=dict()

#空元组
c1=()
c2=tuple()

print('空列表',a1,a2)
print('空字典',b1,b2)
print('空元组',c1,c2)


print('------复习---------')
s1=('hollo word',6666)
s2='suo','nb',666
s3='nb',
s4=tuple(('nb1',66))
s5=()
s6=tuple()
print(s1,type(s1))
print(s2,type(s2))
print(s3,type(s3))
print(s4,type(s4))
print(s5,type(s5))
print(s6,type(s6))