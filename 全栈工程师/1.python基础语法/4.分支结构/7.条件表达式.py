#研发者：时间遗忘
#开发时间：2022/9/21 20:31

#条件表达式:条件表达式是if...else的简写
#简便代码行数，用于print当中

'''语法结构：
× if  判断条件  else  y
判断条件的结果为True，结果往左
       结果为False，结果往右
'''


#运算规则：如果判断条件的布尔值为True，条件表达式的计算结果为×，否则条件表达值的计算结果为False

#要求从键盘录入两个整数，比较两个整数的大小
num_1=int(input('请输入第一个整数：'))
num_2=int(input('请输入第二个整数：'))
#比较大小
'''（正常解法）
if num_1>=num_2:
    print(num_1,'大于等于',num_2)
else:
    print(num_1,'小于',num_2)
'''
print('使用条件表达式进行比较')
print(       (num_1),'大于等于',(num_2)        if num_1>=num_2 else       (num_1),'小于',(num_2)      )#不加括号以及连接符表达出来的效果不一致
print(       num_1,'大于等于',num_2        if num_1>=num_2 else       num_1,'小于',num_2      )
#或使用连接符进行连接
print(        str(num_1)+'大于等于'+str(num_2)            if num_1>=num_2 else              str(num_1)+'小于'+str(num_2)                  )
#if和else前后的可更改