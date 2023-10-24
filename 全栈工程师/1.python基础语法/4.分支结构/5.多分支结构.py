#研发者：时间遗忘
#开发时间：2022/9/21 16:28

#多分支结构：...是...吗？不是
#          ...是...吗？不是
#          ...是...吗？不是
#          ...是...吗？不是
#          ...是...吗？是（多选一执行）
#通常用来解决区间段的问题
#第一个条件为True，后面的均不做判断；第一个条件为False，再去判断第二个条件...

'''语法结构：if 条件表达式1：
              条件执行体1
           elif 条件表达式2:
                条件执行体2
           elif 条件表达式N：
                条件执行体N
           【else】：#放在方括号中，说明是可写可不写的，在多分支结构中是可以省略的
                条件执行体N+1
'''


'''从键盘录入一个整数
90-100 A
80-89  B
70-79  C
60-69  D
0-59   E
小于0大于100  为非法数据 （不是成绩的有效范围）
'''

score=int(input('请输入您的成绩：'))
if score>=90 and score<=100:
    print('您的评价为  A')
elif score>=80 and score<89:
    print('您的评价为  B')
elif score>=70 and score<=79:
    print('您的评价为  C')
elif score>=60 and score<=69:
    print('您的评价为  D')
elif score>=0 and score<=59:
    print('您的评价为  不及格')
else:
    print('成绩无效')


#Python当中有独特的写法
score=int(input('请输入您的成绩：'))
if 90<=score<=100:
    print('A级')
elif 80<=score<=89:
    print('B级')
elif 70<=score<=79:
    print('C级')
elif 60<=score<=69:
    print('D级')
elif 0<=score<=59:
    print('E级')
else:
    print('成绩无效')
