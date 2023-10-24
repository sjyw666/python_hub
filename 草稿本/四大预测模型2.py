#研发者：时间遗忘
#开发时间：2023/8/30 21:13
import numpy as np

# 创建示例时间序列数据
np.random.seed(0)
time = np.arange(1, 101)
data = 10 * np.sin(0.2 * time) + np.random.normal(size=100)

# 分割数据为训练集和测试集
train_data = data[:80]
test_data = data[80:]

from statsmodels.tsa.holtwinters import ExponentialSmoothing

# 创建指数平滑模型
exp_smooth_model = ExponentialSmoothing(train_data, seasonal='add', seasonal_periods=12)
exp_smooth_fit = exp_smooth_model.fit()

# 进行预测
exp_smooth_forecast = exp_smooth_fit.forecast(steps=len(test_data))

# 计算SSE
exp_smooth_sse = np.sum((exp_smooth_forecast - test_data)**2)
print("Exponential Smoothing SSE:", exp_smooth_sse)

from statsmodels.tsa.arima_model import ARIMA

# 创建ARIMA模型
arima_model = ARIMA(train_data, order=(2, 1, 1))
arima_fit = arima_model.fit(disp=False)

# 进行预测
arima_forecast = arima_fit.forecast(steps=len(test_data))

# 计算SSE
arima_sse = np.sum((arima_forecast - test_data)**2)
print("ARIMA SSE:", arima_sse)

from graypy import GM11

# 创建灰色预测模型
gray_model = GM11(train_data)
gray_fit = gray_model.fit()

# 进行预测
gray_forecast = gray_fit.predict(steps=len(test_data))

# 计算SSE
gray_sse = np.sum((gray_forecast - test_data)**2)
print("Gray Forecast SSE:", gray_sse)

import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler

# 数据预处理
scaler = MinMaxScaler()
scaled_train_data = scaler.fit_transform(train_data.reshape(-1, 1))
scaled_test_data = scaler.transform(test_data.reshape(-1, 1))

# 创建神经网络模型
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(1,)),
    tf.keras.layers.Dense(1)
])
model.compile(optimizer='adam', loss='mean_squared_error')

# 训练模型
model.fit(scaled_train_data, scaled_train_data, epochs=50, batch_size=1, verbose=0)

# 进行预测
nn_forecast_scaled = model.predict(scaled_test_data)
nn_forecast = scaler.inverse_transform(nn_forecast_scaled)

# 计算SSE
nn_sse = np.sum((nn_forecast - test_data)**2)
print("Neural Network SSE:", nn_sse)
