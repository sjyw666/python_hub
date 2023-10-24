#变量的定义
#定义蔬菜名称
#建议变量的定义要见名知义，不建议使用拼音
carrot='新鲜红萝卜'
potato='新鲜土豆'
#如果一个变量由多个英文单词组成，单词与单词之间用_（英文的下划线）连接
Green_bean='新鲜青皮豆'
eggplant='新鲜茄子'

#定义蔬菜数量
carrot_number=220
potato_number=300
Green_bean_number=26
eggplant_number=30

#定义单价
carrot_price=2.5
potato_price=2.6
Green_bean_price=6.8
eggplant_price=4.2

#不需要定义金额。因为   单价*数量=金额
print('名称\t\t\t数量\t\t单价\t\t金额')#不好看可以多加几个\t，让打印出来的数据对齐
#可以使用字符串的格式化输出（format   格式化字符串，将变量‘掺杂’到字符串中）
#（f）就跟放在字符串当中一起了
        #大括号是一种语法规则，与f一起使用
print(f'{carrot}\t{carrot_number}\t\t{carrot_price}\t\t{carrot_number*carrot_price}')
print(f'{potato}\t\t{potato_number}\t\t{potato_price}\t\t{potato_number*potato_price}')
                                                                    #round()内置函数，（四舍五入）保留一位小数
print(f'{Green_bean}\t{Green_bean_number}\t\t{Green_bean_price}\t\t{round(Green_bean_number*Green_bean_price,1)}')
print(f'{eggplant}\t\t{eggplant_number}\t\t{eggplant_price}\t\t{eggplant_number*eggplant_price}')
      #''号里面加空格说明将空格当字符串，*号代表运算符号乘，后面接数量
print(''*20,f'共计币:{carrot_number*carrot_price+potato_number*potato_price+Green_bean_number*Green_bean_price+eggplant_number*eggplant_price}')
print(''*20,'陈文超')