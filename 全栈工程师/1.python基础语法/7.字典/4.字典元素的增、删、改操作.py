#研发者：时间遗忘
#开发时间：2022/11/12 9:20


scores={'张三':100,'李四':98,'王五':45}
#key的判断：in   not in
print('张三' in scores)
print('张三' not in scores)

#字典元素的删除(方括号中间是键)，删除指定的key-value对，不可以单独删除键或值：
del scores['张三']  #直接使用（del）的叫语句，带括号（pop、clear）的叫方法
print(scores)

scores.pop('李四')
print(scores)

scores.clear()     #清空字典中的元素
print(scores)

#列表元素的新增(字典没有添加方法，直接赋值即可)：
scores['jack']=90
print(scores)

#列表元素的修改：
scores['jack']=100
print(scores)














print("---------复习-------------")
scores2={'nb1':1,'nb2':2,'nb3':3}
print('nb1' in scores2)
print('nb4'  not in scores2)

del scores2['nb2']
scores2['nb5']=666
scores2['nb5']=66
#scores2.clear()
print(scores2)

scores3={'ab':12,'ab2':34,'ab3':56}
print('name' in scores3)
del scores3['ab']
scores3['ab']=66
print(scores3)
scores3['ab']=666
print(scores3)
scores3.clear()
print(scores3)

del scores3['张三']
print(scores3)
scores3['张三']=168
print(scores3)
scores3.clear()
print(scores3)