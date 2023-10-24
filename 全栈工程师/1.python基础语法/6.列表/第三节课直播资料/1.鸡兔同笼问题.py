#研发者：时间遗忘
#开发时间：2022/10/7 10:27

#鸡兔同笼：鸡+兔=35头   94只脚  鸡（2）  兔（4）
#可以使用循环来解决：while ， for in都可以

#while循环
x=0 #鸡
y=0 #兔
while x<=35:
    y=35-x   #鸡为x只，兔为35-x只
    if 2*x+4*y==94 and x+y==35:
        print('鸡：',x)  #23+12=35  23*2=46  12*4=48  46+48=94
        print('兔：',y)
    x+=1  #鸡的个数要每次加1

#自己写的while循环
a=0
while a<35:
    b=35-a
    while 2*a+4*b==94:
        print("鸡有",a,"只，兔有",b,"只")
        break
    a+=1



#for in循环
count=0
for x in range(1,36):
    count+=1   #进入循环加一次
    y=35-x
    if x*2+y*4==94 and x+y==35:
        print('鸡的数量：',x)
        print('兔的数量：',y)
        break
    #count+=1   放在这最后一次就来不及累加
print('循环的次数:',count)

#自己写的for循环
for a in range(1,35):
    b=35-a
    if 2*a+4*b==94:
        print("鸡有",a,"只，兔有",b,"只")



print("----------复习--------")
#鸡兔同笼：鸡+兔=35头   94只脚  鸡（2）  兔（4）
a=0
b=0
while a<=35:
    b=35-a
    if 2*a+4*b==94:
        print("鸡的数量为：",a)
        print("兔的数量为：",b)
    a+=1


for a in range(1,35):#应改成（35）或（1，36）
    b=35-a
    if 2*a+4*b==94:
        print("鸡的数量为：", a,"兔的数量为：", b)
