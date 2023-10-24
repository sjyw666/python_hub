#可以使用连接符‘+’连接多个字符串类型
print('hello'+'world')
print('hello'+str(123))     #使用加号两边必须是同种类型
#print('hello'+123)   不加单/双引号无法用+连接


#str()   将其他数据类型转换成字符串
#也可以引号转换
name='张三'
age=20
print(type(name),type(age))#说明name和age的数据类型不相同
#print('我叫'+name+'，今年'+age+'岁')       #+号是链接符，但这种情况会报错，需要进行类型转换
print('我叫'+name+'，今年'+str(age)+'岁')
print('我叫'+name+'，今年'+str(age)+'岁了')    #先转换，再链接
print("我叫"+name+"，今年"+str(age)+"岁了")



a=10
b=198.8
c=False
print(type(a),type(b),type(c),)
print(str(a),str(b),str(c),type(str(a)),type(str(b)),type(str(c)))


print("----------------复习------------")
a1=56
b1=69.4
c1=True
print(type(a1),type(b1),type(c1))
print(type(str(a1)),type(str(b1)),type(str(c1)))


#str（）可以将所有的数据类型转换成str类型
a={'aa':100}
print(a,'的数据类型为：',type(a))
s=str(a)#将a转成了字符串类型
print(s,'的数据类型为：',type(s))


#int()    将其他数据类型(必须是数字串)转成整数
#文字类和小数类字符串，无法转化成整数
#浮点数转化成整数，抹零取整
print('-------int()将其他类型转换成int类型-------')
s1='128'
f1=98.7
s2='76.77'
ff=True
s3='hello'
print(type(s1),type(f1),type(s2),type(ff),type(s3))
print(int(s1),type(int(s1)))    #str类型转成int类型，字符串为  数字串
print(int(f1),type(int(f1)))    #folat转成int类型，截取整数部分，舍掉小数部分
#print(int(s2),type(int(s2)))   #str类型转成int类型，报错，因为字符串为小数串
print(int(ff),type(int(ff)))    #bool类型转int类型的时候按照True和False对应的1和0进行转换
#print(int(s3),type(int(s3)))   #str类型转成int类型时，字符串必须为数字串（整数），非数字串是不允许转换的

print(int('98')+int('2'))       #将字符串类型转换成int类型，之后进行加法运算
print(int(98.9))                #将float类型转换成int类型
#这种情况不能转
#print(int('98.9'))   字符串为小数串


#float()     将其他数据类型转换为浮点数
#文字类无法转成整数
#整数转成浮点数，末尾为.0
print('------float()将其他类型转换成folat类型-----')
s1='128.98'
s2='76'
ff=True
s3='hello'
i=98
print(type(s1),type(s2),type(ff),type(s3),type(i))
print(float(s1),type(float(s1)))
print(float(s2),type(float(s2)))
print(float(ff),type(float(ff)))
#print(float(s3),type(float(s3)))     #字符串中的数据如果非数字串的话，则不允许转换
print(float(i),type(float(i)))


#eval()将字符串类型转换成真实的数据类型
x=eval('{"a":100}')#将str类型转换成实际的数据类型
print(x,'的数据类型为：',type(x))