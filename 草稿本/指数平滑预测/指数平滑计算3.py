#研发者：时间遗忘
#开发时间：2023/8/31 8:55
import pandas as pd

# 定义指数平滑函数
def exponential_smoothing(data, alpha):
    smoothed_values = [data[0]]  # 初始平滑值等于第一个数据点
    for i in range(1, len(data)):
        smoothed_value = alpha * data[i] + (1 - alpha) * smoothed_values[i-1]
        smoothed_values.append(smoothed_value)
    return smoothed_values

# 导入 Excel 数据文件
data_file = '../最后一周指数平滑数据.xlsx'
df = pd.read_excel(data_file)

# 获取销售量观测值列
sales_data = df['需求量'].tolist()

# 设置平滑系数
alpha = 0.5

# 进行指数平滑处理
smoothed_sales = exponential_smoothing(sales_data, alpha)

# 计算观测值和平滑值之差的均值
difference = [observed - smoothed for observed, smoothed in zip(sales_data, smoothed_sales)]
mean_difference = sum(difference) / len(difference)

# 打印观测值、平滑值和观测值与平滑值之差
print("观测值    平滑值    观测值与平滑值之差")
for i in range(len(sales_data)):
    print(f"{sales_data[i]}    {smoothed_sales[i]}    {difference[i]}")

# 打印观测值和平滑值之差的均值
print("观测值和平滑值之差的均值:", mean_difference)

# 进行后续时间点的预测
num_predictions = eval(input('请输入需要预测的时间点个数:'))  # 需要预测的时间点个数

# 初始化平方误差和（SSE）
sse = 0.0

for i in range(1, num_predictions + 1):
    last_observed_value = sales_data[-1]
    last_alpha = alpha
    next_predicted_value = last_alpha * last_observed_value + (1 - last_alpha) * smoothed_sales[-1]
    sales_data.append(next_predicted_value)
    updated_smoothed_value = last_alpha * next_predicted_value + (1 - last_alpha) * smoothed_sales[-1]
    smoothed_sales.append(updated_smoothed_value)

    # 计算预测值与观测值之间的差距并将其平方，然后累加至平方误差和（SSE）
    prediction_error = next_predicted_value - sales_data[-1]
    sse += prediction_error ** 2

    print(f"预测值{i}: {next_predicted_value}")

# 打印平方误差和（SSE）
print("平方误差和（SSE）:", sse)
