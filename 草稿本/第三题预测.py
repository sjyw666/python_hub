import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.statespace.sarimax import SARIMAX
from datetime import timedelta
import time

# 记录开始时间
start_time = time.time()

# 从Excel文件中读取数据
data = pd.read_excel('周需求量统计.xlsx')  # 替换成你的文件路径

# 将时间作为索引，并按照时间排序
data['周起始日期'] = pd.to_datetime(data['周起始日期'])
data.set_index('周起始日期', inplace=True)
data.sort_index(inplace=True)

# 创建时间序列对象
time_series = data['需求量总和']

# SARIMA模型的参数
order = (1, 1, 2)
seasonal_order = (1, 1, 1, 52)

# 创建SARIMA模型
model = SARIMAX(time_series, order=order, seasonal_order=seasonal_order)
model_fit = model.fit(disp=False)

# 预测未来70周的需求量
forecast_steps = 80
forecast_values = []

for _ in range(forecast_steps):
    # 预测下一周的需求量
    forecast = model_fit.get_forecast(steps=1)
    forecast_values.append(forecast.predicted_mean.iloc[0])

    # 将预测值添加到历史数据中，并重新训练模型
    time_series = pd.concat([time_series, pd.Series([forecast.predicted_mean.iloc[0]],
                                                    index=[time_series.index[-1] + timedelta(weeks=1)])])
    model_fit = SARIMAX(time_series, order=order, seasonal_order=seasonal_order).fit(disp=False)

# 记录结束时间
end_time = time.time()

# 输出训练和预测时长
total_time = end_time - start_time
print("Total running time:", total_time, "seconds")

# 输出预测结果
forecast_index = pd.date_range(start=time_series.index[-forecast_steps], periods=forecast_steps, freq='W-MON')
forecast_series = pd.Series(forecast_values, index=forecast_index)

# 绘制预测结果
plt.figure(figsize=(12, 6))
plt.plot(time_series.index, time_series.values, label='Actual Data')
plt.plot(forecast_series.index, forecast_series.values, color='red', label='Forecast')
plt.xlabel('Time')
plt.ylabel('Demand')
plt.title('Demand Forecast using Iterative SARIMA')
plt.legend()
plt.show()

print("Demand Forecast for the next", forecast_steps, "weeks:")
print(forecast_series)
forecast_file = 'forecast_results.xlsx'  # Replace with your desired file name and path
forecast_series.to_excel(forecast_file)