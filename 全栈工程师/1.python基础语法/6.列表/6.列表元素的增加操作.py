#研发者：时间遗忘
#开发时间：2022/10/5 11:23

#增加操作：
'''
append()  在列表的末尾添加一个元素
extend()  在列表的末尾至少添加一个元素
insert()  在列表的任意位置添加一个元素
切片       在列表的任意位置添加至少一个元素
'''
lst=[10,20,30]
print('添加元素之前：',lst,id(lst))#id没变，说明没有新列表出现
lst.append(100)#追加100
print('添加元素之后：',lst,id(lst))
lst2=['hello','world']
#lst.append(lst2)      [10, 20, 30, 100, ['hello', 'world']]，将lst2作为一个元素添加到列表的末尾
lst.extend(lst2)       #[10, 20, 30, 100, 'hello', 'world']，把lst2里面的每一个元素在列表的尾部拓展了
print(lst)
#在任意位置上添加一个元素
#insert(索引，添加对象)
lst.insert(1,90)#在索引为1的位置上添加一个90,原本1索引的元素向后推为2，后面索引全向后推1位
lst.insert(1,[100,200])
print(lst)


print('-----------')
#在任意位置上添加N多个元素
lst3=[True,False,'hello']
lst[1:]=lst3#从1开始切，没有说什么时候结束，就把切掉的部分用新的列表去替换
#lst[1:4]=lst3#不包括4
#lst[1:1]=lst3#数字相同就可以不替换添加进指定位置，原位置的全部向后移一位
print(lst)








































print("-------------")
lst4=[121,4234,2324,23423,324]
lst4.append(233)
lst5=[565,675]
lst4.extend(lst5)
lst4.insert(2,2)
print('-----原列表---',lst4,id(lst4))
lst6=["sb",'DVD']
lst4[1:1]=lst6
print('---新列表---',lst4,id(lst4))