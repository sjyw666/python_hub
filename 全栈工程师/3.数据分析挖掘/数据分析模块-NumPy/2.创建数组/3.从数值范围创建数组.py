#研发者：时间遗忘
#开发时间：2023/8/19 22:02
import numpy as np
'''
从数值范围创建数组
'''
#通过数值范围创建数组
#np.arange(start,stop,step,dtype=None)
#arange的生成值是一个列表，参数含头不含尾
n1=np.arange(1,11,2,dtype=None)
print(n1)


#使用linspace函数创建等差数列(等差数列：从第二项开始，每一个的数据都与前一个数据有着相同的差值)
#linspace(start,stop,num=50,endpoint=True,restep=False,dtype=None)
#num表示要生成的等步长的标本数量，不改定默认生成50个
#endpoint表示数列是否包含step(终点值)
#restep表示生成的数组当中是否会出现间距问题，默认值为False
#dtype表示数据类型
n2=np.linspace(7500,10000,6)
#等价于
n21=np.linspace(7500,10000,num=10,endpoint=True,dtype=int)      #加入 restep=False 会导致 _linspace_dispatcher()获得了一个意外的关键字参数'restep'
print('n2:',n2,type(n2))
print('n21:',n21,type(n21))             #生成的是一个数组，只不过里面的值为等差数列




#使用logspace函数创建等比数列(等比数列：从第二项开始，每一个的数据都与前一个数据有着相同的比值)
#logspace(start,stop,num=50,endpoint=True,base=10.0,dtype=None)
#base表示对数的底数
'''int类型是32位的，数据范围是从负的2147483648到正的2147483648，
超出了指定范围时需修改生成的数据类型，将int（32位）类型修改为'uint64'（无符号整数，但是需要加引号，否则会报错，uint64未定义）'''
n3=np.logspace(0,63,64,base=2,dtype='uint64')       #正常元素过长表达方式
n31=np.logspace(0,63,64,base=2,dtype=int)           #默认int表达方式
n32=np.logspace(2,100,4,endpoint=True,base=10,dtype=int)
print(n3)
print(n31)
print(n32)




