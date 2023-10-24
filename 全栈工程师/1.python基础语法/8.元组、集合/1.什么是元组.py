#研发者：时间遗忘
#开发时间：2022/11/12 13:21

#元组：Python内置的数据结构之一，是一个不可变序列
t=('Python','hello',90)   #元组和列表只相差在括号上，元组为小括号，列表为中括号



'''可变序列：可以对序列执行增、删、改的操作，对象地址不发生更改（列表、字典）'''
lst=[10,20,45]
print(id(lst))
lst.append(300)
print(id(lst))

'''不可变序列：没有增、删、改的操作（字符串、元组）'''
s='hello'
print(id(s),type(s))
s+='world'
print(id(s),type(s))
print(s)


print("----------复习----------")
s1=(100,"zhao",666)
print(id(s1))
#s1+="444"
print(type(s1))