# coding:utf-8
# author:杨淑娟
#d={[123,456]:'helloworld'} # 这个字典可以吗？不可以，因为list是可变数据类型

#print(d)

# 可变数据类型是不可以作为key,那些数据类型可以作为字典的键呢？str,int,float,bool,元组
d={(123,456):'helloworld'} # 正常，因为元组是不可变数据类型
print(d)
# 字典是可变数据类型，字典如何添加元素？如何删除元素？如何修改元素?
d['hello']='world' # 字典没有添加方法，直接赋值即可
print(d)
d.pop('hello') # 叫删除
print(d)
del d[(123,456)] # 删除语句
print(d)
d1={1:'a',2:'b',3:'c',4:'d'} # 重新创建一个字典
# 获取字典的元素
print(d1[1]) # 因为1是键  ,获据key获取值
#print(d1[5]) # 键是5，但是这个键 在字典中是否存在？不存在 KeyError: 5
# 建议： 字典取值时使用get()方法
# get(key,default值)
print(d1.get(5,'不存在')) # 不存在
# 字典元素的遍历
for key in d1:  # item是字典中的所有key
    print(key,'-->',d1.get(key))
print('_'*40)

for key in d1.keys(): # 问题 是d1.keys()是什么类型？
    print(key,'-->',d1.get(key))
print('_'*40)
print(d1.keys()) # dict_keys
print(tuple(d1.keys())) # (1, 2, 3, 4)
print('_'*40)
# 遍历值
for value in d1.values():
    print(value)

# 还可以怎么遍历
for k,v in d1.items():
    print(k,v)
print('_'*40)
# 遍历的时候， items()是是一对一对的元组
for item in d1.items():
    print(item) # 这个结果是什么？元组

# 通过映射创建字典
lst1=[1,2,3,4,5]
lst2=['hello','world','python']
zip=zip(lst1,lst2)  # 打包之后的结果什么？打包之后，包里的每一个元素就是一个元组
#print(tuple(zip)) # 打包之后的结果不是字典，打包之后的结果是一对一对的元组
# 一对一对的元素，可以创建字典
print(dict(zip))
t=(('a','apple'),('b','banana'),('c','cat')) # 这是元组吧
# 这个元可以创建字典吗? 可以
print(dict(t))

# 列表推导式
lst=[i for i in range(10) if i%2==0] # 得到一个全都最偶数的字典
print(lst)

# 有没有元组推导式呢？
t=(i for i in range(10) if i%2==0)
print(tuple(t)) # 这里是否会报错？不会报错，会得到一个对象，如果想看到这个对象中的内容，手动转

# 字典推导式
d={i: 'hello'*i for i in range(10) }  #只有偶数会放到字典中
print(d)