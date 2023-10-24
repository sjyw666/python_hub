#研发者：时间遗忘
#开发时间：2022/12/10 21:20

'''集合的数学操作'''
#交集：求两个集合当中共同的元素就是交集操作
s1={10,20,30,40}
s2={20,30,40,50,60}
print(s1.intersection(s2))
print(s1 & s2)   #intersection 和 & 等价，都是交集操作


#并集操作
print(s1.union(s2))
print(s1 | s2)    #union 和 | 等价，都是并集操作

print(s1)
print(s2) #交集和并集之后s1和s2都没有发生改变


#差集操作
print(s1.difference(s2))  #结果为{10}   (前面的)减去相同的部分之后剩下来的
print(s1-s2)   #ditterence 和 - 等价

print(s1)
print(s2)  #差集之后s1和s2都没有发生改变

#对称差集
print(s1.symmetric_difference(s2))   #用并集减交集所剩的部分
print(s1^s2)  #symmetric_difference 和 ^ 等价


print("--------复习--------")
s3={10,20,30,40}
s4={20,30,40,50,60}
print(s3.intersection(s4))
print(s3 & s4)

print(s3.untion(s4))
print(s3 | s4)

print(s3.difference(s4))
print(s3-s4)

print(s3.symmetric_difference(s4))
print(s3^s4)

