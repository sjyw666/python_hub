#研发者：时间遗忘
#开发时间：2022/10/6 20:50

#列表元素的删除操作，方法是带括号的，剩下的叫语句
'''
          一次删除一个元素
remove()  重复元素只删除第一个
          元素不存在抛出ValueError

        删除一个指定索引位置上的元素
pop()   指定索引不存在抛出IndexError
        不指定索引，删除列表中最后一个元素

切片   一次至少删除一个元素

clear()  清空列表

del  删除列表（del  语句）

'''
lst=[10,20,30,40,50,60,30]
lst.remove(30)#从列表中移除一个元素，如果有重复元素只移除第一个元素
print('remove:',lst)
#lst.remove(100)    ValueError: list.remove(x): x not in list

#pop()  根据索引去移除元素
lst.pop(1)      #1指的是索引
print('pop:',lst)
#lst.pop(5)     IndexError: pop index out of range   如果指定的索引位置不存在，将抛出异常
lst.pop()
print('pop不指定索引：',lst)#如果不指定索引，将删除列表中的最后一个元素

print('--------切片操作，一次至少删除一个元素，但是将会产生一个新的列表对象-------')
new_lst=lst[1:3]#不包括3   选取的元素截取出来
print('原列表：',lst,'id：',id(lst))
print('切片输出之后的列表：',new_lst,'id:',id(new_lst))

'''不产生新的列表对象，而是产生删除原列表中的内容'''
lst[1:3]=[]#想删除就得拿一个空列表去替代
print(lst)

'''清除列表中的所有元素'''
lst.clear()
print(lst)

'''del语句将列表删除'''
lst2=[10,20,30,40]
#del lst[2]  #将指定索引删除
del lst   #直接将语句删除
#print(lst)  #NameError: name 'lst' is not defined   列表未定义，所以程序报错



print('------复习---------------')
lst4=[121,4234,2324,23423,324]
lst4.remove(121)
if lst4==[4234,2324,23423,324]:
    print(lst4)
    lst4.pop(1)
    if lst4==[4234,23423,324]:
        print(lst4)
        lst4=lst4[1:3]
        '''if lst4==[23423,324]:
            print(lst4)
            lst4.clear()
            print(lst4)
            del(lst4)
            if print(lst4)==True:
                print(True)
            elif(NameError):
                print(False)'''
else:
    pass

