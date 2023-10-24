#研发者：时间遗忘
#开发时间：2022/10/7 11:09

'''
1.基本数据类型和组合数据类型
  基本数据类型存储数据时只能存储单个值
  组合数据类型存储多个值（多个值的数据类型可以不相同）

2.可变数据类型和不可变数据类型
  可变数据类型：值改变，id不变  （list列表）
  不可变数据类型：值改变，id就变    （int,float,str,bool...）  一个值对应一个id
'''

lst=[10,20,30,'helloworld',True]#这是组合数据类型，可以存储多个值，多个值的数据类型可以不相同
print(lst,'的内存地址为：',id(lst))
#列表最基本的操作，是根据索引取值，索引为正向递增0，1，2，3，4和逆向递减（-1，-2，-3，-4，-5）
#如果希望获取列表中的  True
print(lst[4])
print(lst[-1])




#切片操作不会改变原列表，但是会产生新的列表对象
lst2=lst[0:4:2]  #就是把列表里面的对象提取出来（不包含索引为4的）
print(lst2)

lst3=lst[-1:-4:-1]   #-1就是逆着数，每走一步减1，-1，-2，-3，-4
print(lst3)




#列表元素的判断in 或not in
print(10 in lst)
print(100 not in lst)
print('p' in 'python')#字符串的判断也可以
print('k' not in 'python')




'''列表元素的遍历（重点！！！！）'''
print("-------------列表元素的遍历（重点！！！！）-------------")
#1.直接遍历列表中的元素(最基本的遍历方式) 
for item in lst:
    print(item)

#2.通过索引遍历---->range(),len()    用于控制循环次数
for i in range(len(lst)):#使用len()去计算列表的长度
    print(lst[i])  #根据索引取值
    print("-----不加索引lst[]----")
    print(i)       #不加索引lst就会打印序列数

#3.使用enumerate函数     enumerate  列举、枚举
for idenx,item in enumerate(lst):  #idenx为序列数，默认为0,之后依次递增
    print(idenx,'-->',item)        #item表示的是lst列表的值
#enumerate函数的定义：    del__init__(self,interable,start=0):
'''
一共有三个参数
1.self,不用管，因为没学，面向对象中的内容
2.interable,可迭代对象，就是要遍历的内容
3.start=0,输出序号默认从0开始
'''
print('-------start修改为11后--------')
for index,item in enumerate(lst,start=11):
    print(index,'-->',item)



