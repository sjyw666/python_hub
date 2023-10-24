# coding:utf-8
# author:杨淑娟
# 使用到了一个二维列表
goods=[
    ['成幼猫砂猫咪用品豆腐猫砂',37.80,2],
    ['全套装闪光男童女童可调节旱冰鞋',218.00,1],
    ['蒙牛核桃牛奶190ml*16袋整箱纸袋装',49.80,1]
]

# 二维列表，在进行遍历的时候，需要使用二重循环  （循环套循环）
total=0
# 第一种遍历方式
for item in goods:   # item的数据类型是什么？列表
    for i in item:    # 遍历列表  ，i 的数据类型是什么？str,float,int
        print(i,end='\t') #这里的\t是什么意思？不换行
    total+=item[1] *item[2]  #  为什么是item[1]   ,item[0]是商品名称， item[1]是商品的价格，  item[2]是商品的个数
    print() # 这个空的print()表示一个商品全部输出完毕之后换行
print(round(total,2))   #输出结果取两位
print('*'*70)


total=0
# 第二种遍历方使用，使用索引
for i in range(len(goods)):   # 商品列有的长度是多少   ，因为有三个商品  range(3)  0,1,2 三个整数，
    for j in range(len(goods[i])):  # 小列表的长度 ，小列表是每种商品
        print(goods[i][j],end='\t')
        # 这里的i和j分别代表什么？索引,i 是外层循环的索引，j是内层循环的索引
        #i和j都是索引，元素需要根据索引获取
    total+=goods[i][1]*goods[i][2]  # 为什么是goods[i][1]   i的值从0变到2， 所以goods[0],goods[1] ,goods[2]
    print()

print(round(total,2))
total=0
print('*'*70)
# 第三种方式  ，有点牵强 ，但是为了学习一下语法
for index,item in enumerate(goods):
    print(index,end='\t')
    for i ,j in enumerate(item):
        print(j,end='\t')
    print()
    total+=item[1]*item[2]
print(round(total,2))