#输出不会加引号



#可以输出数字
print(520)
print(98.5)

#可以输出字符串
print('holloworld')
print("holloworld")#单、双、三引号告诉计算机不用去理解，直接打印输出就可以了

#可以输出含有（操作数   运算符    一起叫做表达式）的结果
print(3+1)



#一次输出一个值
print(10)
print('holloword')
print(98.5)#print输出后，换行操作，每个值在输出之后，独占一行

#一次输出多个值，多个值之间使用英文的逗号隔开
print(10,'holloword',98.5)#在一行输出，输出之后换行


#输出之后值与值之间有一个间隔符，间隔符可更换
#将鼠标放到print上，按Ctrl键可以进入到函数的定义处
#print(value, ..., sep（间隔符）=' ', end（结尾）=' ', file=sys.stdout, flush=False)
#sep的默认值是   空格，只需要输出的时候修改sep的值就行
print(10,'holloword',98.5,sep='+')

print()#作用是换行，可以修改，只需要修改end的值
print(10,end='*')
print(20,end='*')#10*20*
print(end='*')#10*20**     end决定了print函数执行结束之后的操作



print("------复习------------")
n1=100
n2=200
#print(end=n1+n2)   无法代入函数，结尾必须是None或字符串，而不是int

'''print()函数可以将内容输出在显示器或文件'''
#将数据输出文件中，注意点，1，所指定的盘符在存在，2，使用file=
fp=open('D:/text.txt','a+')#a+以读写的方式进行追加，如果文件不存在就创建，存在就在文件内容的后面继续追加
print('holloworld',file=fp)#file为文件的意思，fp为变量名
fp.close()#close 关闭的意思

#不进行换行输出（输出内容在同一行中，用逗号隔开）
print('hollo','world','print')

#在开头加入f，可以直接在字符串当中引用变量
print(f'{n1}\t{n2}')

#round()内置函数，保留一位小数/int直接取整？
print(f'{n1}\t{round(n2)}')
