#研发者：时间遗忘
#开发时间：2023/9/2 23:21
'''
二次指数平滑预测法（Double Exponential Smoothing）是一种常用的时间序列预测方法，用于预测具有趋势性的数据。它是对一次指数平滑预测法的改进，通过引入趋势值来更好地捕捉数据的趋势变化。
二次指数平滑预测法使用两个平滑参数来平滑观测值和趋势值。具体来说，它包括以下步骤：

1.初始化：选择初始的预测值、初始趋势值以及两个平滑参数alpha和beta（0 ≤ alpha ≤ 1，0 ≤ beta ≤ 1）。
2.预测值更新：对于每个时刻t，预测值通过以下公式计算：
预测值(t) = alpha * Y(t) + (1 - alpha) * (P(t-1) + T(t-1))
其中，Y(t)表示时刻t的观测值，P(t-1)表示上一时刻的预测值，T(t-1)表示上一时刻的趋势值。
3.趋势值更新：趋势值通过以下公式计算：
趋势值(t) = beta * (P(t) - P(t-1)) + (1 - beta) * T(t-1)
4.重复步骤2和步骤3，直到预测所有时刻的值。

在实际应用中，为了获得更准确的预测结果，需要根据数据的特点和趋势的变化情况来选择合适的平滑参数。
通常情况下，较小的alpha和beta值会使模型对数据的变化更加敏感，适用于波动性较大的数据；较大的alpha和beta值则会使模型对数据的变化反应较慢，适用于波动性较小的数据。
二次指数平滑预测法在实际中有广泛的应用，特别适用于销售趋势、股票价格等时间序列数据的预测。
它能够捕捉到数据的整体趋势，并在一定程度上平滑噪声和异常值的影响，从而提供相对准确的预测结果。
'''

import numpy as np


def double_exponential_smoothing(data, alpha, beta):
    """
    使用二次指数平滑预测法进行时间序列预测

    参数：
    - data: 输入的时间序列数据（一维数组）
    - alpha: 平滑参数alpha（0 ≤ alpha ≤ 1）
    - beta: 平滑参数beta（0 ≤ beta ≤ 1）

    返回：
    - predictions: 预测结果（与输入数据长度相同的一维数组）
    """
    predictions = []
    n = len(data)
    P = data[0]  # 初始预测值
    T = data[1] - data[0]  # 初始趋势值

    for i in range(n):
        if i == 0:
            predictions.append(P)
            continue

        # 更新预测值
        P_last = P
        T_last = T
        P = alpha * data[i] + (1 - alpha) * (P_last + T_last)

        # 更新趋势值
        T = beta * (P - P_last) + (1 - beta) * T_last

        predictions.append(P)

    return predictions


# 示例用法
data = [10, 12, 14, 16, 18,19,30,40]  # 时间序列数据
alpha = 0.2  # 平滑参数alpha
beta = 0.2  # 平滑参数beta

predictions = double_exponential_smoothing(data, alpha, beta)
print("预测结果:", predictions)
