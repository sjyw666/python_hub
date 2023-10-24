#研发者：时间遗忘
#开发时间：2023/8/30 20:49
import numpy as np
import pandas as pd
from statsmodels.tsa.api import SimpleExpSmoothing
from statsmodels.tsa.arima_model import ARIMA
from graypy import GM

# 导入Excel数据
excel_file = 'sales_data.xlsx'  # 替换为你的Excel文件路径
data_frame = pd.read_excel(excel_file)
sales_data = data_frame['Sales'].tolist()


# 指数平滑
def exponential_smoothing(data, alpha):
    model = SimpleExpSmoothing(data)
    model_fit = model.fit(smoothing_level=alpha, optimized=False)
    forecast = model_fit.forecast(steps=1)
    return forecast[0]


alpha = 0.2
exp_forecast = exponential_smoothing(sales_data, alpha)
exp_sse = (sales_data[-1] - exp_forecast) ** 2


# ARIMA
def arima_forecast(data, order):
    model = ARIMA(data, order=order)
    model_fit = model.fit(disp=False)
    forecast = model_fit.forecast(steps=1)
    return forecast[0]


arima_order = (1, 1, 1)  # Example ARIMA order
arima_forecast_value = arima_forecast(sales_data, arima_order)
arima_sse = (sales_data[-1] - arima_forecast_value) ** 2


# 灰色预测
def gray_forecast(data):
    model = GM(1, 1)
    model.fit(data)
    forecast = model.predict(steps=1)
    return forecast[0]


gray_forecast_value = gray_forecast(sales_data)
gray_sse = (sales_data[-1] - gray_forecast_value) ** 2


# 神经网络预测（使用简单的Numpy实现）
def neural_network_forecast(data):
    # Define network weights and biases
    input_weight = np.array([0.5])
    hidden_weight = np.array([0.3, 0.2])
    hidden_bias = 0.1
    output_weight = np.array([0.4])
    output_bias = 0.2

    # Calculate hidden layer output
    hidden_output = np.dot(data[-1], input_weight) + hidden_bias
    hidden_output = 1 / (1 + np.exp(-hidden_output))

    # Calculate final output
    final_output = np.dot(hidden_output, output_weight) + output_bias
    return final_output


nn_forecast_value = neural_network_forecast(sales_data)
nn_sse = (sales_data[-1] - nn_forecast_value) ** 2

print("Exponential Smoothing Forecast:", exp_forecast)
print("Exponential Smoothing SSE:", exp_sse)
print("\nARIMA Forecast:", arima_forecast_value)
print("ARIMA SSE:", arima_sse)
print("\nGray Forecast:", gray_forecast_value)
print("Gray SSE:", gray_sse)
print("\nNeural Network Forecast:", nn_forecast_value)
print("Neural Network SSE:", nn_sse)
