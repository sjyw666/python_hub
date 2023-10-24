#研发者：时间遗忘
#开发时间：2022/10/4 20:36

#获取列表中的多个元素
'''语法格式：
列表名[start:stop:step]
        1.切片的结果---->原列表片段的拷贝

        2.切片的范围---->[start:stop)#不包含stop

切片操作：3.step默认值为1---->简写为[start:stop]

        4.step为正数---->[stop:step]---->切片的第一个元素默认是列表的第一个元素------>从start开始往后计算切片
                   ---->[start:step]---->切片的最后一个元素默认是列表的最后一个元素-->

        5.step为负数---->[stop:step]---->切片的第一个元素默认是列表的最后一个元素------>从start开始往前计算切片
                   ---->[start:step]---->切片的最后一个元素默认是列表的第一个元素-->
'''


lst=[10,20,30,40,50,60,70,80]
print('--------step步长为正数的时候------')
#start=1，stop=6，step=1
#print(lst[1:6:1])#不包括6
print('原列表：',id(lst))
lst2=lst[1:6:1]
print('切的片段：',id(lst2))


print(lst[1:6])#默认步长为1
print(lst[1:6:])#冒号后面不写一样默认为1
#start=1，stop=6，step=2
print(lst[1:6:2])
#stop=6，step=2，start采用默认
print(lst[:6:2])
#start=1，step=2，stop采用默认-
print(lst[1::2])

print('--------step步长为负数的时候------')
print('原列表：',lst)
print('逆序输出：',lst[::-1])#逆序输出
#start=7，stop省略，step=-1
print('start初始值为7：',lst[7::-1])
print('strat初始值为6：',lst[6::-1])
print('strat初始值为5：',lst[5::-1])
#start=6，stop=0，step=-2
print(lst[6:0:-2])

print('尝试逆序start不设值，stop默认为0',lst[:0:-1])


#判断指定元素在列表中是否存在
#元素名  in   列表名
#元素名  not in  列表名
lst3=[10,20,'python','hello']
print(10  in  lst3)
print(100  in  lst3)
print(10  not in  lst3)
print(100  not in  lst3)




#列表元素的遍历
#for  迭代变量   in  列表名：
      #--------操作--------
print('-------列表元素的遍历--------')
for item in lst3:
    print(item)


