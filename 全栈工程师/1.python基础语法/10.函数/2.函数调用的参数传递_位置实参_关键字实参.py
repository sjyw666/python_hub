#研发者：时间遗忘
#开发时间：2023/9/16 19:52
def jia(a,b):   #a,b为形式参数，简称形参，在函数的定义处
    c=a+b
    return c

shu=jia(10,20)  #10，20为实际参数，简称实参，在函数的调用处
print(shu)


#位置传参（正常传参）根据形参对应的位置进行实参传递
def c1(a,b):
    c=a+b
    return c

p1=c1(10,20)
print(p1)


#关键字传参（可不按位置赋值）根据形参名称进行实参传递
def c2(a,b):
    c=a+b
    return c

p2=c2(b=10,a=20)        #形参名称=形参值
print(p2)



