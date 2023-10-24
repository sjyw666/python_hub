#研发者：时间遗忘
#开发时间：2023/5/13 17:05

#字符串：在Python中字符串是基本数据类型，是一个不可变的字符序列

'''
字符串驻留机制：
仅保留一份相同且不可变字符串的方法，不同的值被存放在字符串的驻留池中，
Python的驻留机制对相同的字符串只保留一份拷贝，后续创建相同字符串时，不会开辟新的空间，
而是把该字符串的地址赋给新创建的变量
因为PyCharm对字符串进行了优化（强制）处理，对内容进行了驻留，所以用终端进行才能看出驻留机制
'''



'''
字符串驻留机制的优缺点
·当需要值相同的字符串时，可以直接从字符串池里拿来使用，避免频繁的创建和销毁，提升效率和节约内存，
（Python一切皆对象，创建和销毁都需要时间）
因此拼接字符串和修改字符串是比较影响性能的。
·
在需要进行字符串拼接时建议使用str类型的join方法、而非+，
因为join（）方法是先计算所有字符串中的长度，
然后拷贝，只new一次对象，效率要比“+”效率高
'''


a='Python'
b="Python"
c='''Python'''
print(a,id(a))     #发现有相同字符串就不会创建新的内存地址去存储
print(b,id(b))
print(c,id(c))


'''
驻留机制的几种情况（交互模式）
·字符串的长度为0或1时
·符合标识符的字符串
·字符串只在编译时进行驻留，而非运行时
·[-5,256]之间的整数数字
'''

#·字符串的长度为0或1时
s1=''
s2=''
s1 is s2 #True
print(s1 is s2 )#True


s1='%'
s2='%'
print(s1 is s2 )#True


#·符合标识符的字符串
s1='abc%'
s2='abc%'
print(s1 is s2 )#False
print(s1==s2 )#True

print(id(s1))  #不同
print(id(s2))


s1='abcx'
s2='abcx'
print(s1 is s2 )#False
print(s1==s2 )#True

print(id(s1))  #不同
print(id(s2))

a='abc'
b='ab'+'c'
c=''.join(['ab','c'])
a is b
#True

a is c
#False
print(c)
'abc'
print(type(c))
#<class 'str'>
print(a)
'abc'
print(type(a))
#<class 'str'>


a=-5
b=-5
a is b   #True


a=-6
b=-6
a is b   #False


import sys
a='abc%'
b='abc%'
a is b #False

a=sys.intern(b)
a is b #强制驻留
#True


#sys中的intern方法强制2个字符串指向同一个对象


