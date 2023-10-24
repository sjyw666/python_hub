#研发者：时间遗忘
#开发时间：2023/8/27 20:19
geshu=input('请输入想要的裴波那契数列个数：')

#定义初值
n1=0
n2=1
pbnqsl=[]
for geshu in range(eval(geshu)):#控制累加次数
    n3=n1+n2
    n4=n3+n2

    print('')