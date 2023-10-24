#研发者：时间遗忘
#开发时间：2022/11/12 14:54

'''元组是可迭代对象，所以可以使用for in 进行遍历'''
t=(('Python','world',98))
'''元组元素的获取可以使用索引，但是超出索引范围会报错'''
print(t[0])
print(t[1])
print(t[2])

'''使用遍历的方式获取'''
for item in t:
    print(item)

print('-------复习-------')
for i in t:
    print(i)
i2=[i]
print(i2)