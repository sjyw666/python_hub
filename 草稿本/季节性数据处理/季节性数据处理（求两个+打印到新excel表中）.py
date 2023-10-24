#研发者：时间遗忘
#开发时间：2023/9/9 18:00
import pandas as pd
import matplotlib.pyplot as plt

# 读取 Excel 文件，假设日期保存在 "Date" 列，流量保存在 "Flow" 列，排沙量保存在 "Sediment" 列
df = pd.read_excel('插值数据每天.xlsx')

# 将日期列转换为日期类型
df['Date'] = pd.to_datetime(df['日期'])

# 设置日期列为索引
df.set_index('Date', inplace=True)

# 根据每三个月进行重采样，并对流量和排沙量求和
resampled_data = df.resample('3M').sum()

# 绘制折线图
resampled_data['日总流量'].plot(label='Flow')
resampled_data['日总排沙量'].plot(label='Sediment')
plt.xlabel('Date')
plt.ylabel('Sum')
plt.title('Three-Month Sum (Flow and Sediment)')
plt.legend()
plt.show()

# 打印每三个月的流量总和和排沙量总和
print("Three-Month Flow Sum:")
print(resampled_data['Flow'])
print("Three-Month Sediment Sum:")
print(resampled_data['Sediment'])

# 将求和后的数据保存到新的 Excel 文件中
resampled_data.to_excel('季节划分后数据.xlsx')
