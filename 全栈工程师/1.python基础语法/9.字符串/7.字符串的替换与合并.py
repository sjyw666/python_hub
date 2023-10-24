#研发者：时间遗忘
#开发时间：2023/5/29 9:47
'''
字符串替换replace()
    第1个参数指定被替换的子串，第2个参数指定替换子串的字符串，该方法返回替换后得到的字符串，
    替换前的字符串不发生变化，调用该方法时可以通过第3个参数指定替换最大替换次数
字符串的合并join()
    将列表或元组中的字符串合并成一个字符串
'''

s='hello,Python'
print(s.replace('Python','Java'))
s1='hello,Python,Python,Python'
print(s1.replace('Python','Java',2))

lst=['hello','Java','Python']
print('|'.join(lst))   #使用join前面的字符将列表或元组中的字符连接到一起
print(''.join(lst))

t=('hello','Java','Python')
print(''.join(t))

print('*'.join('Python'))

