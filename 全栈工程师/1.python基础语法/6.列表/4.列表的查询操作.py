#研发者：时间遗忘
#开发时间：2022/10/4 16:38

#获取列表中指定元素的索引：
'''
index()  如查列表中存在N个相同元素，只返回相同元素中的第一个元素的索引
         如果查询的元素在列表当中不存在，则会抛出ValueError
         还可以在指定的start和stop之间进行查找
'''
lst=['hello','world',98,'hello']
print(lst.index('hello'))#0，如查列表中存在N个相同元素，只返回相同元素中的第一个元素的索引
#print(lst.index('Python'))    #ValueError: 'Python' is not in list
#print(lst.index('hello',1,3))     #索引为3，但是不包括3  #ValueError: 'hello' is not in list


print(lst.index('hello',1,4))   #3




#获取列表中的单个元素
'''
正向索引从0到N-1   举例：lst[0]
逆向索引从-N到-1   举例：lst[-N]
指定索引不存，抛出indexError
'''
lst2=['hello','world',98,'hello','world',234]
#获取索引为2的元素
print(lst2[2])
#获取索引为-3的元素
print(lst2[-3])

#获取索引为10的元素
#print(lst2[10])  #IndexError: list index out of range  #获取索引不在指定范围内

#使用enumerate方法,可以查看对应的序列和对应选项的遍历
for item in enumerate(lst):
    print(item)

for item in lst:
    print(item)

for i in enumerate(lst):
    print(i,'66')












































