#研发者：时间遗忘
#开发时间：2023/8/22 11:09
import numpy as np

#生成（0，1）之间的随机数组，包含0不包含1的数组（[0,1））
n1=np.random.rand(5)            #产生一维数组
n11=np.random.rand(2,4)         #生成两行四列的数组
print(n1)
print(n11)


#随机生成满足正态分布的数组
n2=np.random.randn(3)
n21=np.random.randn(3,4)        #如何判断生成数据是否满足正态分布
print(n2)
print(n21)


#生成一定范围内的随机数组，（含头不含尾）
#(start,stop,num)   起始、停止、生成数量
n3=np.random.randint(1,6,10)
n31=np.random.randint(1,6,size=(2,3))       #生成两行三列的随机数数组
print(n3)
print(n31)

#生成正态分布的随机数组
'''[
正态分布的均值（正态分布的对称轴），
正态分布的标准差（正态分布的形状，越大越矮胖，越小越瘦高），
表示产生数组的维数
]'''
n4=np.random.normal(0,0.1,10)           #生成元素数为10的数组
n41=np.random.normal(0,0.1,(2,3))       #生成二维数组
print(n4)
print(n41)






