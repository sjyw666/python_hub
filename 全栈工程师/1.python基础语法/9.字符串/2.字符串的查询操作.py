#研发者：时间遗忘
#开发时间：2023/5/16 11:10
'''
index()
    查找子串substr第一次出现的位置，如果查找的子串不存在时，则抛出ValseError
rindex()
    查找子串substr最后一次出现的位置，如果查找的子串不存在时，则抛出ValueError
find()
    查找子串substr第一次出现的位置，如果查找的子串不存在时，则返回-1
rfind()
    查找子串substr最后一次出现的位置，如果查找 的子串不存在时，则返回-1
'''

s='hello,hello'
print(s.index('lo'))  #3
print(s.find('lo'))
print(s.rindex('lo'))  #9
print(s.rfind('lo'))

#print(s.index('k'))    ValueError: substring not found   字符串不存在
#print(s.rindex('k'))
print(s.find('k'))   #-1
print(s.rfind('k'))