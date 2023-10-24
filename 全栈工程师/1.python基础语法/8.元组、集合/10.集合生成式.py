#研发者：时间遗忘
#开发时间：2022/12/10 21:51

'''集合生成式'''
'''{  i*i  for  i  in  range(1,10)}'''
'''表示集合     自定义    可迭代对象
元素的表达式     变量
'''
#将{}修改为[]就是列表生成式
#没有元组生成式，因为元组是我们学过的数据类型当中的唯一一个不可变的数据类型

#列表生成式
lst=[  i*i  for  i  in  range(1,10)] #range是产生0-5之间的整数
print(lst)

#字典生成式
items=['Fruits','Books','Others']
prices=[96,78,85]
d={item:price for item,price in zip(items,prices)}
print(d)

#集合生成式
s={  i*i  for  i  in  range(1,10)}  #数字过大的时候跟列表对比的时候发现是无序的，因为集合的特点就是无序的
print(s)


print("-------复习------------")
s1={ (s*s)-1  for s in range(20,30)}
print(s1)