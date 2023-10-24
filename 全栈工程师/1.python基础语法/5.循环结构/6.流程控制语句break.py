#研发者：时间遗忘
#开发时间：2022/9/30 16:07

#break语句：用于结束循环结构，通常与分支结构if一起使用
#break只能跟循环一起使用
'''
for ... in ...:               while （条件）：
    ...                         ...
    if ...:                     if ...:
       break--->跳出循环             break--->跳出循环
'''


'''从键盘录入密码，最多录入三次，如果正确就结束循环'''
for item in range(3):
    password=input('请输入您的密码；')
    if password=='8888':
        print('密码正确')
        break              #退出for循环，不再执行
    else:
        print('密码错误')



a=0
while a<3:              #0是一次，1是一次，2是一次
    '''条件执行体（循环体）'''
    password=input('请输入密码：')
    if password=='8888':
        print('密码正确')
        break
    else:
        print('密码不正确')
    '''改变变量'''
    a+=1



print("---复习--------")
for _ in range(3):
    psd=input("请输入您的密码：")
    if psd=="123":
        print("密码正确")
        break
    else:
        print("密码错误")

a=0
while a<3:
    psd=input("再再再次输入您的密码：")
    if psd=="666":
        print("密码正确")
        break
    else:
        print("密码错误")
        a+=1