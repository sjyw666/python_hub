#研发者：时间遗忘
#开发时间：2022/10/2 16:56

#else语句：
#与else语句搭配的三种情况：
'''else的搭配：
if...:                              while...:     for...:
  ...                                    ...         ...
else:--->if条件表达式不成立时执行else   else:         else:---->没有碰到break时执行else
  ...                                    ...         ...
'''

for item in range(3):
    password=input('请输入您的密码：')
    if password=='8888':
        print('密码正确')
        break
    else:
        print('密码不正确')
else:
    print('三次密码均输入错误')


'''for循环和while循环执行路径上不出现break，执行完循环执行else'''

a=0
while a<3:
    password=input('请输入您的密码：')
    if password=='8888':
        print('密码正确')
        break
    else:
        print('密码不正确')
    a+=1
else:
    print('三次密码均输入错误')