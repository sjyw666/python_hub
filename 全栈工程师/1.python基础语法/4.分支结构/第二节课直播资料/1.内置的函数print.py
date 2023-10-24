# coding:utf-8
# author:杨淑娟
# 一次输出一个值
print(10)
print('helloworld')
print(98.5) # print输出之后，换行操作，每个值在输出之后，独占一行

# 一次输出多个值，多个值之间使用英文的逗号进行分隔,输出的值与值之间有一个空格，为什么？
# #输出之后的值与值之间的间隔符可以换成别的符号吗？可以
print(10,'helloworld',98.5) # 在一行输出，输出之后换行
#def print(self, *args, sep=' ', end='\n', file=None):
# sep 的默认值是 空格，只需要输出的时候修改sep的值即可
print(10,'helloworld',98.5,sep='+') # 输出之后值与值之间使用 +进行分隔
print(10,'helloworld',98.5,sep='8') # 输出之后值与值之间使用 8进行分隔
# 为什么一个什么都没有的print函数是一个换行呢？
print() # 作用是换行，为什么？可不可以修改，可以，只需要修改end的值

print(10,end='*')
print(20,end='*') # 10*20*
print(end='*')#10*20**    end决定了print函数执行结束之后的操作
print(end='abc+def') # 可以
