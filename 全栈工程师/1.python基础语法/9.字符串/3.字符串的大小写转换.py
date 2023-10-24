#研发者：时间遗忘
#开发时间：2023/5/21 10:29
'''
upper() 上面的
    把字符串中所有字符都转成大写字母
lower() 下方的
    把字符串中所有字符转成小写字母
swapcase()  转换
    把字符串中所有大写字母转成小写字母，把所有小写字母都转成大写字母
capitalize()    首字母大写
    把第一个字符转换为大写，把其余字符转换为小写
title() 标题
    把每个单词的第一个字符转换为大写，把每个单词的剩余字符转换为小写
'''

'''
字符串是一个不可变序列，修改大小写之后会产生一个新的字符串对象
'''
s='hello,python'
print(s,id(s))
a=s.upper()
print(a,id(a))

b=s.lower()
print(b,id(b))
print(s.lower(),id(s.lower()))
print(b==s) #True  内容相等
print(b is s) #False   地址不相等，没有驻留

s2='hello,Python'
c=s2.swapcase()
print(c,id(c))

d=s.capitalize()
print(d,id(d))

e=s.title()
print(e,id(e))