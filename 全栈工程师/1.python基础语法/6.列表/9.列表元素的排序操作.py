#研发者：时间遗忘
#开发时间：2022/10/6 21:36

'''
常见的两种方式：
调用sort()方法，列表中的所有元素默认按照从小到大的顺序进行排序，可以指定reverse=True，进行降序排序

调用内置函数sorted()，可以指定reverse=True，进行降序排序，原列表不发生改变
'''

lst=[20,40,10,98,54]
print('排序前的列表：',lst,id(lst))

#调用列表对象的sort方法--->直接在原列表进行，默认是升序排序
lst.sort()
print('排序后的列表：',lst,id(lst))#id未发生改变，说明是在原列表的基础上进行的


#通过指定关键字参数，将列表中的元素进行降序排序
lst.sort(reverse=True)
print(lst)
lst.sort(reverse=False)   #reverse=True 是降序，reverse=False是升序
print(lst)


#内置函数sorted()--->对原列表不产生影响
print('----------使用内置函数sorted()对列表进行排序，将产生一个新的列表对象，不对原列表进行更改--------')
lst=[20,40,10,98,54]
print('原列表：',lst,id(lst))

#内置函数，直接使用
new_lst=sorted(lst)
print('排序列表：',new_lst,id(new_lst))


desc_lst=sorted(lst,reverse=True)  #指定关键字参数
print('降序列表：',desc_lst,id(desc_lst))







