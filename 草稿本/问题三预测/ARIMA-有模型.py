import numpy as np
import pandas as pd
import tensorflow as tf1
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import time

# 记录程序开始时间
start_time = time.time()

# 读取数据
data = pd.read_excel('每天水流量排沙量数据.xlsx')
data['日期'] = pd.to_datetime(data['日期'])
time_series = data['日流量'].values.astype(float)

# 数据标准化
scaler = MinMaxScaler()
time_series = scaler.fit_transform(time_series.reshape(-1, 1))

# 准备数据集
def create_dataset(time_series, look_back=1):
    X, Y = [], []
    for i in range(len(time_series) - look_back):
        X.append(time_series[i:(i + look_back), 0])
        Y.append(time_series[i + look_back, 0])
    return np.array(X), np.array(Y)

look_back = 7  # 使用前30天的数据来预测第31天
X, Y = create_dataset(time_series, look_back)

# 构建神经网络模型
model = Sequential()
model.add(LSTM(100, input_shape=(look_back, 1)))  # 增加LSTM神经元数量
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer='adam')

# 模型训练
model.fit(X, Y, epochs=10000, batch_size=64, verbose=2)

# 预测未来两年的数据
num_days = 2 * 365
future_predictions = []

# 使用模型逐步预测未来数据点
for i in range(num_days):
    last_data_points = time_series[-look_back:].reshape(1, look_back, 1)
    future_prediction = model.predict(last_data_points)[0][0]

    # 将负数预测值转为0
    if future_prediction < 0:
        future_prediction = 0

    future_predictions.append(future_prediction)

    # 将预测结果添加到时间序列中以供下一次预测使用
    time_series = np.append(time_series, [[future_prediction]], axis=0)

# 反标准化未来预测数据
future_predictions = scaler.inverse_transform(np.array(future_predictions).reshape(-1, 1))

# 创建日期范围，包括未来两年的日期
last_date = data['日期'].iloc[-1]
future_date_range = pd.date_range(last_date, periods=num_days + 1)[1:]

# 记录程序结束时间
end_time = time.time()

# 计算运行时间
running_time = end_time - start_time
print(f"程序运行时间：{running_time:.2f} 秒")

# 绘制历史数据和未来预测数据
plt.figure(figsize=(12, 6))
plt.plot(data['日期'], scaler.inverse_transform(time_series)[:len(data)], label='Historical Data', color='blue')
plt.plot(future_date_range, future_predictions, label='Future Predictions', color='green')
plt.xlabel('Date')
plt.ylabel('Flow')
plt.title('Historical Data vs. Future Predictions')
plt.legend()
plt.xticks(rotation=45)
plt.show()

# 将日期范围转换为日期字符串的列表
future_date_strings = [str(date) for date in future_date_range]

# 创建一个包含日期和预测值的DataFrame
future_predictions_df = pd.DataFrame({'日期': future_date_strings, '预测值': future_predictions.ravel()})

# 保存DataFrame到Excel文件
future_predictions_df.to_excel('未来两年水流量预测结果.xlsx', index=False)

print("预测结果已保存到 '未来两年水流量预测结果.xlsx' 文件中。")

# 模型性能评估
historical_data = data['日流量'][-num_days:]
mse = mean_squared_error(historical_data, future_predictions)
rmse = np.sqrt(mse)
mae = mean_absolute_error(historical_data, future_predictions)
r2 = r2_score(historical_data, future_predictions)

print(f'MSE: {mse:.2f}')
print(f'RMSE: {rmse:.2f}')
print(f'MAE: {mae:.2f}')
print(f'R^2: {r2:.2f}')
