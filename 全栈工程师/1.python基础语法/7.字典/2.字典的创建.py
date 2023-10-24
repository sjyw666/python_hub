#研发者：时间遗忘
#开发时间：2022/11/12 8:29

'''字典的创建；
最常用的方法：使用花括号
scores={'张三':100,'李四':98,'王五'：45}

使用内置函数dict()
dict(name='jack',age=20)

采用等号赋值的形式，所以等号左侧是不加引号的
右侧加不加引号取决于值的数据类型
字符串加，整数类型不加

当字典的key为可变数据类型（str int float ）时，将可变数据类型转换为元组
例：列表类型转换为元组类型
'''

'''最常用的方法：使用花括号'''
scores={'张三':100,'李四':98,'王五':45}
print(scores)
print(type(scores))

liebiao={(123,456):"holloworld"}
print(liebiao)


'''第二种创建dict（）'''
student=dict(name='jack',age=20)
print(student)



'''第三种通过映射创建字典'''
lst1=[1,2,3,4,5]
lst2=['hello','world','python']
'''
zip=zip(lst1,lst2)
print(zip)                 #不加tuple出现乱码（<zip object at 0x0000019B90377E80>）
print(tuple(zip))          #打包之后的结果是一对对的元组，但一对对的元组可以创建字典
print(dict(tuple(zip)))    #但是无法根据这种方式去创建压缩字典
print(dict(zip))
'''



lst3=[1,2,3,4,5]
lst4=['hello','world','python']
zip2=zip(lst3,lst4)     #zip压缩无法同时使用
                        #pythonzip()函数
print(zip2)             #不加tuple出现乱码（<zip object at 0x0000019B90377E80>）
print(dict(zip2))       #使用这种方式创建lst3:lst4的压缩字典


t=(('a','apple'),('b','banana'),('c','cat'))#利用元组也可以创建字典，只有两个元素的元组才可以分别当作键和值创建字典
print(dict(t))


s={'apple','banana','pear','grape','orange'}
#输出结果{'grape', 'apple', 'pear', 'banana', 'orange'}随机！！！
print(s)
#用集合中的元素作为字典中的键，不会按照原来的顺序，而是会按照输出结果的顺序进行创建,每次输出的结果都不相同
#原因是Python解释器的版本问题，Python3.5以下字典的输出结果都最无序的，但是3.5以上输出结果都与定义顺序相同
#Python解释器的版本更新很快，但是第三方库不支持，就无法使用一些功能
#定义顺序相同，但是也不能说是有序的
lst5=[10,2,3,4,5]
zidian={k:y for k,y in zip(s,lst5)}
zidian4={k4:y4 for k4,y4 in zip(lst5,s)}
print(zidian)



'''空字典'''
d={}
print(d)


print("--------复习-----------")
zidian={'张三':10,'李四':30}
print(zidian)

zidian2=dict(张三=10,李四=100,name='姓名')
print(zidian2)

zidian3={}
print(zidian3)

ss={'ww':66,'ss':77,'bb':88 }
print(ss,type(ss))

ss1=dict(na=66,nb='nba')
print(ss1)

ss2={}
print(ss2)



zidian2={'张三':122,'李四':134}
print(zidian2)
zidian4=dict(李四=122,王五=134)
print(zidian4)
zidian5={}
print(zidian5)