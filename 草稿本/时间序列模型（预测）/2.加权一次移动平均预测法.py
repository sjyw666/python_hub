#研发者：时间遗忘
#开发时间：2023/9/2 22:32
'''
加权一次移动平均预测法（Weighted Moving Average）是对简单移动平均预测法的改进，它考虑了过去数据的加权平均值，以便更好地适应不同时期的变化。
在加权一次移动平均预测法中，与简单移动平均预测法不同的是，我们为每个数据点分配一个权重，然后计算加权平均值。
权重可根据对过去数据的重视程度进行设置，例如，我们可以赋予较近期的数据较高的权重，以便更准确地反映最近的趋势。
以下是加权一次移动平均预测法的基本步骤：

1.确定加权窗口大小：首先需要确定用于计算加权移动平均的窗口大小。

2.确定权重：为窗口内的每个时间点分配一个权重，通常权重越大，对应的数据点对预测的贡献越大。
    权重可以按照线性或指数衰减等方式确定。

3.计算加权移动平均值：根据选定的窗口大小和权重，按时间顺序计算每个时间点的加权移动平均值。
    假设第t个时间点的数据为x(t)，对应的权重为w(t)，计算方法为将窗口内每个数据点与对应的权重相乘，再将乘积求和并除以权重之和。
    WMA(t) = (x(t) * w(t) + x(t-1) * w(t-1) + … + x(t-n+1) * w(t-n+1)) / (w(t) + w(t-1) + … + w(t-n+1))
    其中，x(t)表示第t个时间点的数据，w(t)表示第t个时间点对应的权重。

4.进行预测：在计算得到加权移动平均值之后，可以利用这些值进行未来的预测。最简单的方法是使用最新的加权移动平均值作为对未来趋势的预测。

需要注意的是，加权一次移动平均预测法通常需要根据实际情况选择合适的权重设置方法和窗口大小。
可以根据经验或进行实验来调整权重和窗口大小的设置，以获得更准确的预测结果。
'''

import numpy as np

def weighted_moving_average(data, weights):
    moving_averages = []
    n = len(data)

    for i in range(len(weights), n+1):
        window = data[i-len(weights):i]
        average = np.average(window, weights=weights)
        moving_averages.append(average)

    return moving_averages

# 示例数据
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
weights = [0.1, 0.2, 0.3, 0.4]

# 计算加权移动平均值
moving_averages = weighted_moving_average(data, weights)
print("加权移动平均值:", moving_averages)

# 进行预测
last_average = moving_averages[-1]
print("预测值:", last_average)

'''
在上述代码中，我们定义了一个weighted_moving_average函数，它接受一个数据列表和权重列表作为参数，并返回加权移动平均值的列表。
函数中使用了NumPy库中的average函数来计算加权平均值。
我们提供了示例数据data和权重weights，并调用weighted_moving_average函数计算加权移动平均值。
最后，我们使用最后一个加权移动平均值作为预测值。
请注意，示例代码中的权重列表weights需要根据实际情况进行设置。
这里的示例权重是一个简单的线性权重，你可以根据需要使用不同的权重设置方法，如指数衰减权重或自定义权重设置方法。
'''