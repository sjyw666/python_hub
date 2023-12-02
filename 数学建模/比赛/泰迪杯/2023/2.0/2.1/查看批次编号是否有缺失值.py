# 研发者：时间遗忘
# 开发时间：2023/11/11 9:04
# 特点说明：
'''

'''
import pandas as pd

# 读取 Excel 文件
df = pd.read_excel('批次编号数据.xlsx', header=None, names=['Column_Name'])

# 检查是否有缺失值
missing_values = df['Column_Name'].isnull().any()

if missing_values:
    # 找到缺失的值
    missing_numbers = df[df['Column_Name'].isnull()]['Column_Name']
    print("缺失的值是：", missing_numbers)
else:
    print("没有缺失值")
