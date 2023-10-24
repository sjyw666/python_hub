#变量的命名必须要规范，用小写，多个单词的时候用下划线连接
#定义名称
Cat_litter='猫砂'
the_skating_shoes='溜冰鞋'
Walnut_milk='核桃牛奶'


#定义单价
Cat_litter_Unit_Price=18.9
the_skating_shoes_Unit_Price=218
Walnut_milk_Unit_Price=49.8


#定义数量
Cat_litter_quantity=2
the_skating_shoes_quantity=1
Walnut_milk_quantity=1

#打印小计
print('名称\t\t单价\t\t数量\t\t小计')
print(f'{Cat_litter}\t\t{Cat_litter_Unit_Price}\t{Cat_litter_quantity}\t\t{Cat_litter_Unit_Price*Cat_litter_quantity}')
print(f'{the_skating_shoes}\t{the_skating_shoes_Unit_Price}\t\t{the_skating_shoes_quantity}\t\t{the_skating_shoes_Unit_Price*the_skating_shoes_quantity}')
print(f'{Walnut_milk}\t{Walnut_milk_Unit_Price}\t{Walnut_milk_quantity}\t\t{Walnut_milk_Unit_Price*Walnut_milk_quantity}')
print(''*20,'共记：',f'{Cat_litter_Unit_Price*Cat_litter_quantity+the_skating_shoes_Unit_Price*the_skating_shoes_quantity+Walnut_milk_Unit_Price*Walnut_milk_quantity}')
#\t不用占用单独的字符串，与前面的内容直接连接就行

'''Python字符串格式化的方式有三种（Python常见100问中第15问）：   
1  %的形式
2  字符串的format方法
3  f-string形式，在字符串之前加个f，那么字符串中就可以使用{变量}的形式
'''