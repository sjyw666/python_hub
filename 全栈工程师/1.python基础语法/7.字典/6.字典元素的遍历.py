#研发者：时间遗忘
#开发时间：2022/11/12 10:05

scores={'张三':100,'李四':98,'王五':45}
for item in scores:
    print(item)     #遍历的是scores的key
    print(item,scores[item],scores.get(item))   #用列表元素的获取方式结合遍历可输出value的值
                                                #放在循环中遍历的键索引都是存在的，不会出现报错的情况

'''根据键取值的遍历'''
print("方法一----------------------------------------")
for key in scores:
    print(key,'-->',scores.get(key))    #用get方法求字典的值
    print(key,'-->',scores.values())
    #根据values得到的是全部的value（dict_values([100, 98, 45])），无法单独打印


print("方法二-------------------------------------------")
#遍历的时候，items()是一对对的元组
for k,v in scores.items():              #将键值分开存放
    print(k,v)

for items in scores.items():            #用这种方式创建出来的结果类型是元组
    print(items)

print("方法三----------------------------------------------")
for key1 in scores.keys():
    print(key1,'-->',scores.get(key1))


print(scores.keys())                    #直接使用会带一个dict_keys
print(tuple(scores.keys()))



print('------------复习-----------')
scores1={'张三':100,'李四':98,'王五':45}
for i2 in scores1:
    print(i2,scores1[i2],scores1.get(i2))

print('------------')
for i3 in scores1:
    print(i3,scores1[item],scores1.get(i3))