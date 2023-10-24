#input内置函数是进行键盘输入
name=input('请输入您的姓名：')#小括号里面是文本提示，这个文本提示，可写可不写，但是建议写上
            #否则客户不知道要做什么
#输入的值需要存储到变量当中            变量（使用）=对输入的值进行储存



#从键盘输入（录入）的任何数据，都是字符串类型
#可使用内置函数type()查看数据的类型
age=input('请输入您的年龄：')
score=input('请输入您的成绩:')
print(name,'的数据类型是：',type(name))
print(age,'的数据类型是：',type(age))
print(score,'的数据类型是：',type(score))


#内置函数eval()可以改变数据字符，通常与input一起使用，将字符串转成实际的数据类型
age1=eval(input('请再次输入您的年龄：'))
print(age1,'的数据类型为：',type(age1))
print(score,'的数据类型为：',type(eval(score)))#将数字串转换成了int或float类型的数字串


age2=eval(input('输入实验'))
print(age2,'的数据类型：',type(age2))

