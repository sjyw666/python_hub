#研发者：时间遗忘
#开发时间：2023/8/30 19:25
import pandas as pd
import numpy as np

def adaptive_exponential_smoothing(series, alpha):
    smoothed = [series[0]]
    errors = []
    for i in range(1, len(series)):
        predicted = alpha * series[i] + (1 - alpha) * smoothed[i-1]
        smoothed.append(predicted)
        errors.append(series[i] - predicted)
        alpha = calculate_alpha(series[i], smoothed[i-1], alpha)
    return smoothed, errors

def calculate_alpha(observed, predicted, previous_alpha):
    error = observed - predicted
    delta_alpha = 0.1 * np.abs(error)
    new_alpha = previous_alpha + delta_alpha
    new_alpha = max(0, min(1, new_alpha))
    return new_alpha

# 导入Excel数据
data = pd.read_excel('最后一周指数平滑数据.xlsx')

# 获取数据列（假设数据在"Value"列中）
series = data['需求量'].tolist()

# 设置初始alpha值
alpha = 0.5

# 进行指数平滑并获取平滑值和差值
smoothed_series, errors = adaptive_exponential_smoothing(series, alpha)

# 打印观测值、平滑值和差值
print("观测值:", series)
print("平滑值:", smoothed_series)
print("差值:", errors)
print("差值的均值:", np.mean(errors))
