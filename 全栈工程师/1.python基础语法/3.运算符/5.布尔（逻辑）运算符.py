#布尔运算符    和(and),或者(or),不(not),在里面(in),不在里面(not in)
#作用：连接比较运算符的
a,b=1,2
#两个运算数都为True时，运算结果才为True
print('---------------and  并且-------------')
print(a==1 and b==2)     #True       True and True-->True
print(a==1 and b<2)      #False      True and False-->False
print(a!=1 and b==2)     #False      True and False-->False
print(a!=1 and b<2)      #False      False and False-->False


#只要有一个运算数为True，运算结果就为True
print('------------------or  或者---------------')
print(a==1 or b==2)      #True       True or True-->True
print(a==1 or b<2)       #True       True or True-->True
print(a!=1 or b==2)      #True       False or True-->True
print(a!=1 or b<2)       #False      False or False-->False


#只有一个运算数，not取反之后为相反的结果（对bool类型操作数进行取反）
#不是什么的结果
print('-----------------not  取反--------------------')
f=True
f2=False
print(not f)
print(not f2)


#在不在什么里面
print('------------------in 与not in ---------------------')
s='holloward'
print('w' in s)
print('k' in s)
print('w' not in s)
print('k' not in s)

s2=123
#print(1 in s2)          报错，类型int的参数不可迭代
#print("1" in s2)

s3="123"
print('1' in s3)     #将需要确认的int类型输入成str类型才能进行运算






