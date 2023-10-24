# coding:utf-8
# author:杨淑娟
a=10
print(a,id(a)) # 输出内存地址

a=20  # 将a的值发生更改,那么内存地址也发生了更改
print(a,id(a))

# 字符串的定义
s='helloworld'
s="helloworld"

s='''
   hello
    world
'''

s="""
  hello
  world
"""
# Python中单行注释使用  #  ,对一行代码进行解释说明
# Python中没有明确的多行注释 ，所以可以使用三引号代 表注释
# 25到29行，是多行注释
'''
 下面这是两个输出语句
 一句输出10
 另一句也输出10
'''
print(10)
print(10)

# 可以 使用+连接多个字符串
print('hello'+'world')
#print('hello'+123) # TypeError: can only concatenate str (not "int") to str

# 转义字符 ：\n,\t 常用的转义字符
# 原字符串（r/R）：使转义字符串失效
print('hello\nworld')  # \n换行
print(r'hello\nworld') # \n就失效，r可大写也可小字