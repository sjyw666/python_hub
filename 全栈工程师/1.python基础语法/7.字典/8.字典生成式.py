#研发者：时间遗忘
#开发时间：2022/11/12 10:37

'''字典生成式：
使用内置函数zip()
用于将可迭代的对象作为参数，将对象中的对应的元素打包成一个元组，然后返回由这些元组组成的的列表
'''

#两个字典的列表：
items=['Fruits','Books','Others']
prices=[96,78,85]

d={item:price for item,price in zip(items,prices)}#首先使用for in循环遍历压缩包zip（）
                                                  #再放到自定义的item,price中
                                                  #输入字典的格式item:price
                                                  #最后再将字典赋值给d
print(d)


#大写输出
e={item.upper():price for item,price in zip(items,prices)}#在key后面添加upper（）
                                                          #输出的key就都变成了大写
print(e)


#字典元素不相同的情况下：
items=['Fruits','Books','Others']
prices=[96,78,85,100,120]
f={item:price for item,price in zip(items,prices)}  #当字典中元素个数不一样时，zip()会进行压缩，最后输出的结果按照顺序进行
print(f)      #{'Fruits': 96, 'Books': 78, 'Others': 85}


#字典推导式
t={i:i*2 for i in range(10) if i%2==0}#推导的目的是快捷创建，值为所有数据类型都行
print(t)
t1={i:"hello" for i in range(10) if i%2==0}
print(t1)




print('----------复习-----------')
lst1=['nb1','nb2','nb3']
lst2=[111,222,333]
lst3=[12,324,523,5346,643,63]
zidian={i:i2 for i,i2 in zip(lst1,lst2)}
zidianshitu=zidian.items()
print(dict(zidianshitu))

zidian2={i3.upper():i4 for i3,i4 in zip(lst1,lst2)}
print(zidian2)

zidian3={i5.upper():i6 for i5,i6 in zip(lst1,lst3)}
print(zidian3)
