#研发者：时间遗忘
#开发时间：2022/11/12 9:34

'''获取字典视图：
keys()     获取字典中的所有key
values()                value
items()                 key,value对
'''

#获取所有的key
scores={'张三':100,'李四':98,'王五':45}
keys=scores.keys()  #存储到一个变量(keys)中
print(keys)
print(type(keys))
print(list(keys))   #将所有的key组成的视图转换成列表

#获取所有的value
values=scores.values()
print(values)
print(type(values))
print(list(values))

#获取所有的key-value对
items=scores.items()
print(items)
print(type(items))
print(list(items))   #转换之后的元素是由元组组成的


print('---------------复习-------------')
scores1={'张三':100,'李四':98,'王五':45}
keys1=scores1.keys()
print(keys1)
print(type(keys1))
keys2=list(keys1)
print(keys2)


values1=scores1.values()
print(values1)
print(type(values1))
print(list(values1))


items1=scores1.items()
print(items1)
print(type(items1))
print(list(items1))
print(type(list(items1)))


