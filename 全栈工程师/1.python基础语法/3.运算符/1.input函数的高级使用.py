#从键盘中输入两个加数（两个）整数，计算两个整数的和
a=input('请输入一个加数：')
a=int(a)       #将转换之后的结果存储到a中
b=input('请输入另一个加数：')
b=int(b)
print(type(a),type(b))
print(a+b)#由于两个输入为字符串类型，所以+号起到的是连接作用


#或
a=int(input('请输入一个加数：'))
b=int(input('请输入另一个加数：'))
print(type(a),type(b))
print(a+b)


#或？（自己编写）
a=input('请输入一个加数：')
b=input('请输入另一个加数：')
print(type(a),type(b))
print(int(a)+int(b))


print("----------复习---------")
n1=input("请输入一个加数：")
n2=input("请输入另一个加数：")
print(type(n1),type(n2))
print(int(n1)+int(n2))