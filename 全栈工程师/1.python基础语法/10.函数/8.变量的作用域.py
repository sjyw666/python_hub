#研发者：时间遗忘
#开发时间：2023/9/16 19:55
def fun():      #函数内部定义的变量是局部变量，局部变量用global声明，这个变量就变成了全局变量
    global age
    age=20
    #global abc =30     不能直接用这种写法，需先声明再进行赋值
    print(age)

fun()
print(age)