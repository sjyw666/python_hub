#研发者：时间遗忘
#开发时间：2022/11/12 8:58

'''字典中元素的获取：
[]   举例：scores['张三']

get()方法   举例：scores.get('张三')
'''

#[]取值与使用get()取值的区别：
#[]如果字典中不存在指定的key,抛出keyError异常
#get()方法取值，如果字典中不存在指定的key，并不会抛出keyError而是返回None（没有），可以通过参数设置默认的value，以便指定的key不存在时返回

scores={'张三':100,'李四':98,'王五':45}
'''第一种方式，使用[]（中括号里面是键，不是索引）'''
print(scores['张三'])
#print(scores['陈六'])   #keyError:'陈六'


'''第二种方式，使用get()方法，索引时建议使用get方法'''
print(scores.get('张三'),'6')
print(scores.get('陈六'))  #None
print(scores.get('麻七',99))  #99是在查找'麻七'所对的value不存在时，提供的一个默认值


print("-------复习----------")
print(scores['张三'])
print(scores.get('张三'))
print(scores.get('陈六','nb'))



if scores.get('陈六','nb')==None:
    print('None')
else:
    print('nb')

print(scores['张三'])

name=scores.get('张三')
name2=scores.get('张四',800)
print(name,name2)

name3=scores['张三']
name4=scores.get('张三',68)
print(name3,name4)