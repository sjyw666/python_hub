#研发者：时间遗忘
#开发时间：2022/11/12 15:51
'''集合元素的判断操作'''
s={10,20,30,40}
print(10 in s)
print(10 not in s)

'''集合元素的增添操作'''
s.add(80)   #一次添加一个元素
print(s)

#s.add([10,20,30])   不可以，因为添加的是可变数据类型


s.update({100,200,300})   #字典  #一次最少添加一个元素
print(s)
s.update([300,566])       #列表
s.update((78,76,9))       #元组
print(s)

'''集合元素的删除操作'''
s.remove(100)    #一次删一个，要求删的时候元素要存在，否则抛异常KeyError
print(s)
s.discard(500)      #同样是一次删一个，但是删除元素不存在时不会抛异常
s.discard(300)
print(s)
s.pop()     #一次只删除一个任意元素
s.pop()
#s.pop(400)    pop()方法不能添加参数
s.clear()
print(s)     #列表的清空操作


print('---------复习-------')
s1={10,20,30,40}
print(10 in s1)
print(1000 not in s1)

s1.add(100)
l1=[100,200,3003,3030]
s1.update(l1)
print(s1)
s1.update({100:"字典"})
s1.update((1010,10,120,3030,30))
print(s1)

s1.remove(100)
#s1.remove(500)
s1.discard(1000)
s1.pop()
print(s1)
s1.clear()
print(s1)
