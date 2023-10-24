#研发者：时间遗忘
#开发时间：2023/8/22 13:19
import numpy as np

'''从已有的数组中创建数组'''
#与array函数类似
#asarray(a,dtype=None,order=None)
n1=np.asarray([1,2,3])
print(n1,type(n1))
#通过列表的元组创建数组
n12=np.asarray([(1,2,3),(4,5,6)])    #列表中包含元组元素
print(n12)
#通过元组创建元组
n13=np.asarray((1,2,3))
print(n13)
#通过元组的元组创建数组
n14=np.asarray(((1,2,3),(4,5,6)))    #元组中包含元组
print(n14)
#通过元组的列表
n15=np.asarray(([1,2,3],[4,5,6]))
print(n15)


#动态数组
#formbuffer(buffer,dtype=float,conunt=-1,offset=0)
n2=np.frombuffer(b'juanzijie',dtype='S1')         #buffer参数在前面加上b，参数写中文前需会提示编码不对，需将中文换成英文
print(n2)              #输出结果前面都会带个b
                       #python3版本默认是unicode？类型，需转成facts二进制类型（在前面加b）
                       #S1表示单个字符串是一个字符


#从迭代对象中建立数组对象
#fromiter(iterable,dtype,count=-1)
#iterable是迭代器
iter=(i for i in range(5))      #创捷可迭代对象
n3=np.fromiter(iter,dtype='int')
print(n3)



#empty_like函数
#numpy.empty_like(protype,dtype=None,order='k',subok=True)
#创建一个指定模板的数组，该函数会根据指定数组模板进行创建
n4=np.empty_like([[1,2],[3,4]])         #创建2行2列的数组
print(n4)

n41=np.zeros_like([[1,2],[3,4]])         #创建以0填充的2行2列的数组
print(n41)

n42=np.ones_like([[1,2],[3,4]])         #创建以1填充的2行2列的数组
print(n42)

n43=np.empty_like([[1,2],[3,4]])         #创建指定数字填充的2行2列的数组
print(n43)








