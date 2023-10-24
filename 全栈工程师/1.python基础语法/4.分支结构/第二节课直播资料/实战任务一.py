# coding:utf-8
# author:杨淑娟
# 变是的定义
# 定义蔬菜名称
# 建议变量的定义要见名知意
carrot='新鲜红萝卜'
potato='新鲜土豆'
# 如果一个变量由多个英文单词组成，单词与单词之间使用 _ 连接
green_bean='青皮豆'
eggplant='新鲜茄子'
# 定义蔬菜数量
carrot_num=220
potato_num=300
green_bean_num=26
eggplant_num=30

# 单价
carrot_price=2.5
potato_price=2.6
green_bean_price=6.8
eggplant_price=4.2

# 需不需要定义金额变量？单价*数量 等于金额
print('名称\t\t\t数量\t\t单价\t\t金额')
# 可以使用字符串的格式化输出                               单价*数量
print(f'{carrot}\t{carrot_num}\t\t{carrot_price}\t\t{carrot_num*carrot_price}')
print(f'{potato}\t\t{potato_num}\t\t{potato_price}\t\t{potato_num*potato_price}')
                                                                    #round()内置函数，保留一位小数
print(f'{green_bean}\t\t{green_bean_num}\t\t{green_bean_price}\t\t{round(green_bean_num*green_bean_price,1)}')
print(f'{eggplant}\t\t{eggplant_num}\t\t{eggplant_price}\t\t{eggplant_num*eggplant_price}')
print(' '*15,f'共计币:{carrot_price*carrot_num+potato_price*potato_num+green_bean_price*green_bean_num+eggplant_num*eggplant_price}')
print(' '*20,'陈文超')

# f-->format的缩写，格式化字符串，将变量 “掺杂”到字符串中
# ' '*15  输出15个空格
# ' '*20 输出20个空格

