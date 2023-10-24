#研发者：时间遗忘
#开发时间：2022/9/21 9:11
#Python一切皆对象，所有对象都有一个布尔值
#获取对象的布尔值：使用内置函数bool（）


print('----------以下对象的布尔值都是False---------')
#False
print("False：",bool(False))           #False

#数字0
print("数字0：",bool(0))               #False
print("数字0.0：",bool(0.0))


#None     英文为“没有”的意思
print("英文None：",bool(None))            #False

#空字符串：长度为0的字符串对象
#空字符串和空格字符串不一样
print("空字符串：",bool(''))              #False
print(bool(""))
print("空格字符串",bool(" "))             #True
#空列表:[]和list（）都表示列表
print(bool([]))              #False
print(bool(list()))

#空元组：（）和tuple都表示元组
print(bool(()))              #False
print(bool(tuple()))

#空字典：{}和dict（）都是字典
print(bool({}))
print(bool(dict()))

#空集合:set()是集合
print(bool(set()))

print('------------------剩下的布尔值均为True------------')
print(bool(18))
print(bool(True))
print(bool('holloworld'))
print(bool())