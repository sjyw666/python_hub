#研发者：时间遗忘
#开发时间：2023/9/16 19:53
#函数返回多个值时，结果为元组
def iff(a):
    f1=[]   #存奇数
    f2=[]   #存偶数

    for i in a:         #遍历列表中的元素
        if i%2:         #每个对象都有一个布尔值，1：True 0：False
            f1.append(i)
        else:
            f2.append(i)
    return f1,f2

s=[10,3,60,78,66]
b=iff(s)
print(b)

'''
函数在定义时，是否需要返回值，视情况而定
'''
#如果函数没有返回值【函数执行完毕之后，不需要给调用处提供数据】return可以省略不写
def fun1():
    print("hello")

fun1()


#函数的返回值，如果是1个，直接返回类型
def fun2():
    return "helloo"
a2=fun2()
print(a2)


#函数的返回值，如果是多个，返回的结果为元组
def fun3():
    return 'hello','helloo'
print(fun3())
