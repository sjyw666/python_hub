#研发者：时间遗忘
#开发时间：2023/9/9 17:53
import pandas as pd
import matplotlib.pyplot as plt

# 读取Excel文件，假设日期保存在"Date"列，流量保存在"Flow"列
df = pd.read_excel('插值数据每天.xlsx')

# 将日期列转换为日期类型
df['Date'] = pd.to_datetime(df['日期'])

# 设置日期列为索引
df.set_index('Date', inplace=True)

# 按每三个月进行重采样，并计算每三个月的流量总和
resampled_data = df['日总流量'].resample('3M').sum()

# 生成折线图
plt.plot(resampled_data.index, resampled_data.values)
plt.xlabel('Date')
plt.ylabel('Total Flow')
plt.title('Total Flow Every Three Months')
plt.show()
