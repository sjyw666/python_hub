#研发者：时间遗忘
#开发时间：2023/8/17 22:01

#基本运算（多重赋值）
a,b,c=2,3,4
#相当于
'''
a=2  b=3  c=4
'''

#字符串操作
s=' I like python'
s+=' very much'          #将s与' very much'拼接得到，得到' I like python very much'
print(s)

s.split(' ')            #将s以空格分割，得到列表['I','like','python']???
print(s,type(s))

for i in s:
    print(i)

if a==1:
    print(a)
else:
        print('a不等于1')

#函数
'''
Python用def来自定义函数
'''
def add1(x):
    return x+2
print(add1(2))      #输出结果为4,输入一个参数，由程序去判断输出结果


def add2(x=0,y=0):  #定义函数，同时
    return (x+2,y+2)
def add3(x,y):
    return x+3,y+3
a,b=add3(1,2)           #
print(a,b)





