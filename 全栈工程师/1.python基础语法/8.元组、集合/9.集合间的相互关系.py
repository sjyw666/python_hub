#研发者：时间遗忘
#开发时间：2022/11/12 16:29

'''判断集合是否相等==  ！='''
'''元素的内容相同，底层的存储数据也相同'''
s={10,20,30,40}
s1={30,40,20,10}
print(s==s1)    #True
print(s!=s1)    #False

'''判断一个集合是否是另一个集合的子集'''
s1={10,20,30,40,50,60}
s2={10,20,30,40}
s3={10,20,90}
#形式：s2/s3是否是s1的子集
print(s2.issubset(s1))  #True   #相等的时候互为子集和超集
print(s3.issubset(s1))  #False


'''判断一个集合是否是另一个集合的超集'''
print(s1.issuperset(s2))  #True
print(s1.issuperset(s3))  #False



'''判断两个集合是否没有交集'''
print(s2.isdisjoint(s3))    #disjoint 不相交的   #False
s4={100,200,300}
print(s2.isdisjoint(s4))    #True



print("---------复习------------")
s5={10,20,30,40}
s6={30,40,20,10}
print(s6==s5)
print(s6!=s5)


print(s6.issubset(s5))
print(s5.issuperset(s6))
print(s5.isdisjoint(s6))