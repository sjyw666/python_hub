#研发者：时间遗忘
#开发时间：2023/8/19 17:17
'''
数组的分类
    一维数组（axis为0，按照行（上下）去操作）
        根Python列表的形状一样，区别在于数组的切片是针对于原始数组
    二维数组（axis为1，按照列（左右）去操作）
        以数组作为数组元素，二维数组包括行和列，类似于表格，又称为矩阵
    三维数组（axis为2）
        为数为三的数组元素，也称矩阵列表
轴的概念
    轴是NumPy模块里的axis,指定某个axis就是沿着axis做相关操作
'''

#创建简单数组
#语法
import numpy
import numpy as np
numpy.array(object,dtype=None,copy=True,ndmin=0)
#object,创建的这个数组对象
n1=np.array([1,2,3])        #array数组
print(n1)

n2=np.array([0.1,0.2,0.3])  #数组元素可为小数
print(n2)

n3=np.array([[1,2],[3,4]])    #使用列表嵌套的方式创建二维数组
print(n3)


#dtype,创建数组时指定数据类型
list1=[1,2,3]
n4=np.array(list1,dtype=float)    #浮点型在小数位为0的情况，不显示小数位
print(n4)
print('n4数据类型：',n4.dtype)
print('n4type类型：',type(n4))
print('n4指定元素的类型：',type(n4[0]))#通过数组的索引（下标）进行指定的查找



#copy,当运算和处理数据的时候为了不影响原数组，对复制后的数组进行修改操作
n5=np.array([1,2,3])
n6=np.array(n5,copy=True)
n6[0]=100
n6[2]=200
print(n5)
print(n6)


#ndmin，控制数组当中最小维数，根据最小维数创建指定维数的一个数组
list2=[1,2,3]
print(list2,"原类型：",type(list2))
n7=np.array(list2,ndmin=3)      #最小维数为3，创建三维数组
print(n7,'现类型；',type(n7))



