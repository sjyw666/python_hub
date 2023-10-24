#研发者：时间遗忘
#开发时间：2023/5/29 10:10
'''
运算符：>,>=,<,<=,==,!=

比较规则：首先比较两个字符串中的第一个字符，如果相等则继续比较下一个字符，
依次比较下去，直到两个字符串中的字符不相等时，其比较结果就是两个字符串的比较结果，
两个字符串中的所有后续字符串将不再被比较

比较原理：两上字符串进行比较时，比较的是其ordinal value(原始值),
调用内置函数ord可以得到指定字符的ordinal value
与内置函数ord对应的是内置函数chr，调用内置函数chr时指定ordinal value可以得到其对应的字符
'''

print('apple'>'app')    #True
print('apple'>'banana') #False

print(ord('a'),ord('b'))    #a为97，b为98，结果相当于对比97和98的大小
print(chr(97),chr(98))      #在字符编码的时候unicode前128项是阿斯玛值

print(ord('赵'))
print(chr(36213))


'''
==与id的区别
  ==比较的是value
  id比较的是id（字符串的内存地址）是否相等
'''
a=b='Python'
c='Python'
print(a==b)     #True
print(b==c)     #True

print(a is b)   #True   指向的内存地址相同
print(a is c)   #True
print(id(a))
print(id(b))
print(id(c))




