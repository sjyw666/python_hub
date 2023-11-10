# 研发者：时间遗忘
# 开发时间：2023/11/5 17:05
# 特点说明：
'''x 

'''
import pandas as pd
detail = pd.read_excel('meal_order_detail.xlsx')
pd.set_option('display.max_columns', None)  # 显示所有列
pd.set_option('display.max_rows', None)  # 显示所有行

# 然后显示整个 DataFrame
print(detail)
