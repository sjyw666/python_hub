#运算比较符：对变量或表达式的结果进行大小，真假等比较
#(>),(<),(>=),(<=),(!=)
#比较运算符的结果为bool类型    结果只能为True或False(Yes或No)
a,b=10,20
print('a>b吗？',a>b)    #False
print('b>a吗?',b>a)    #True
print('a<b吗？',a<b)    #True
print('a>=b吗？',a>=b)  #False
print('a<=b吗？',a<=b)  #True
print('a=b吗？',a==b)   #False
print('a≠b吗？',a!=b)   #True



print("-------------")


'''一个=称为赋值运算符，两个==称为比较运算符，作用不相同
   一个变量由三部分组成  标识（id），类型，值
   比较的是值
'''


'''比较对象的标识使用是    is  '''
#对象value的比较  (==)
#对象的id的比较      (is),(is not)
a=10
b=10
c=20
print(a==b)       #True     说明a和b的value相同
print(a is b)     #True     说明a和b的id(标识)相同    value（值）相同--》a和b指向的空间相同--》id相同
print(a is c)
#以下代码没学过，后面会讲解
lst1=[11,22,33,44]
lst2=[11,22,33,44]
print(lst1==lst2)        #value      --》True
print(lst1 is lst2)      #id         --》False
print(id(lst1))
print(id(lst2))
#列表的值相同，但是标识不同

#比较对象的id是不相同的吗
print(a is not b )       #False
print(lst1 is not lst2)  #True
