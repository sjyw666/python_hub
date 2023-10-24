#研发者：时间遗忘
#开发时间：2023/8/16 20:53



import pandas as pd

# 读取第一个 Excel 文件
fj4sp_id = pd.read_excel('附件4删除重复数据.xlsx')       #df1 = pd.read_excel('附件')
#print(fj4sp_id.head())#可以查看数据的前几行：

# 读取第一列的数据并转换为列表
first_column_data = fj4sp_id['sku_id'].tolist()#代码中的 '列名' 替换为您实际的第一列列名。这将使用 tolist() 方法将数据转换为 Python 的列表，然后将其存储在名为 first_column_data 的变量中。

# 打印列表
#print(first_column_data)

'''fj4sp_id=[          #附件4中的商品id
    66,
    78,
    4432,
    42
]'''

fj1sp_id=[          #附件1中的商品id
    66,
    78,
    4432,
    44,
    4432,
    68
]

fj1sp_xx=[          #附件1中商品信息
    ['10-1',708,666,996,568,654],
    ['10-2',708,666,996,568,654],
    ['10-3',708,666,996,568,654],
    ['10-4',708,666,996,568,654],
    ['10-3',708,666,996,568,654],
    ['10-6',708,666,996,568,654],
]


for i in range(0,len(fj1sp_id)):        #遍历次数为附件1商品的次数
    scores2={
        fj1sp_id[i]:fj1sp_xx[i]
    }


    for item in fj4sp_id:                    #遍历列表元素(附件4商品id)
        for item2 in scores2:                #遍历字典的值(附件1商品id)
            if item == item2:                #如果相等


                print(item2, '-->', scores2.get(item2))              #输出字典对应的value(商品信息)




