# 研发者：时间遗忘
# 开发时间：2023/11/11 9:34
# 特点说明：
'''
计算并绘制每天不同工序完成案卷数量，通过程序生成xlsx数据
'''
import pandas as pd
import matplotlib.pyplot as plt

# 读取数据
df = pd.read_excel('data2.xlsx')

# 将日期字符串转换为日期类型
df['工序开始时间'] = pd.to_datetime(df['工序开始时间']).dt.date

# 筛选出工序状态为2或5的数据
completed_cases = df[df['工序状态'].isin([2, 5])]

# 根据工序开始时间和工作节点名称分组，并计算每组的数量
grouped_data = completed_cases.groupby(['工序开始时间', '工作节点名称']).size().reset_index(name='完成案卷数量')

# 将数据透视为以日期为行，工作节点名称为列的形式
pivot_data = pd.pivot_table(grouped_data, values='完成案卷数量', index='工序开始时间', columns='工作节点名称', fill_value=0)

# 打印生成的透视数据
print(pivot_data)

# 绘制图表
pivot_data.plot(kind='bar', stacked=True)
plt.title('每天不同工序完成案卷数量')
plt.xlabel('日期')
plt.ylabel('完成案卷数量')
plt.show()

# 将透视数据保存为新的Excel文件
pivot_data.to_excel('processed_data.xlsx')
