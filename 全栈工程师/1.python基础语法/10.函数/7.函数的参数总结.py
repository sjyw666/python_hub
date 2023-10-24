#研发者：时间遗忘
#开发时间：2023/9/16 19:54
def fun(a,b,c):     #a,b,c在函数的定义处，所以是形式参数
    print('a=',a)
    print('b=',b)
    print('c=',c)

fun(10,20,30)
lst=[11,22,33]
fun(*lst)   #在函数调用时，将（列表/字典）中的（每个元素/键值对）都转化为（位置/关键字）实参传入，不加*号会报错，只传入了一个（参数/关键字）

dic={'a':111,'b':222,'c':333}
fun(**dic)

def fun2(a,b=20):   #有默认值
    pass

def fun3(*args):    #个数可变的（位置/关键字）形参
    pass

def fun4(**args):
    pass


fun3(10,20,30)
fun4(a=10,b=20,c=30)
'''???'''
fun3(10,20,c=20,d=30)

'''几种方式均可'''
def fun5(a,b,*,c,d):    #在*号之后的参数在函数调用时，只能采用关键字参数进行传递
    print(a,b,c,d)

def fun6(a,b,c,d,*args):
    pass

def fun7(*args,**args2):
    pass

def fun8(a,b=10,*args,**args2):
    pass






