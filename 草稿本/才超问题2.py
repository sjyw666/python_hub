#研发者：时间遗忘
#开发时间：2023/9/20 11:00
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

# 创建一个示例时间序列数据
data = pd.Series([23, 27, 30, 33, 35, 38, 42, 45, 47, 50, 52])

# 对时间序列数据进行指数平滑
alpha = 0.2 # 平滑系数
model = sm.tsa.ExponentialSmoothing(data, trend='add', damped=False, seasonal=None, initialization_method="estimated")
result = model.fit(smoothing_level=alpha, optimized=False)

# 预测未来的值
forecast = result.forecast(steps=3) # 预测未来3个时间步长的值

# 打印预测结果
print("预测结果:")
print(forecast)

# 绘制原始数据和平滑后的数据
plt.figure(figsize=(10, 6))
plt.plot(data, label='原始数据', marker='o')
plt.plot(result.fittedvalues, label='平滑数据', color='red')
plt.plot(pd.concat([data, forecast]), label='原始数据+预测', linestyle='dashed', color='green')
plt.legend()
plt.title('指数平滑示例')
plt.show()