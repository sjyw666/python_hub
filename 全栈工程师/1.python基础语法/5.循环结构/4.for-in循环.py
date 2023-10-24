#研发者：时间遗忘
#开发时间：2022/9/30 10:28

#for-in循环：
#in表达从（字符串、序列等）中依次取值，又称遍历（把里面的东西都拿出来叫做遍历）
#for-in遍历的对象必须是可迭代对象
#for in也叫做次数固定的循环
'''for-in的语法结构：
for 自定义的变量 in 可迭代的对象：
    循环体
'''

for item in 'Python':      #第一次取出来的是P，将P值赋值给item，将item的值输出，依此类推
    print(item)            #item为自定义的名称


#range（）函数：用于生成一个整数序列---->也是一个可迭代对象
for i in range(10):        #range(10)说明是从0到9，0到9执行了10次
    print(i)

#如果循环体内不需要访问自定义变量，可以将自定义变量替代为下划线
for _ in range(5):         #range函数可用做for函数的一个循环次数
    print('人生苦短，我用Python')


print('使用for循环计算1-100之间的偶数和')
sum=0
for item in range(1,101):
    if item%2==0:
       sum+=item
print(sum)

print('使用for循环计算1-100之间的奇数和')
a=1
sum2=0
for i1 in range(1,101):
    if a%2==1:
        sum2+=a
    a+=1
print(sum2)

