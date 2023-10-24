#研发者：时间遗忘
#开发时间：2023/9/2 22:27
'''
简单一次移动平均预测法（Simple Moving Average, SMA）是一种基本的时间序列预测方法，用于平滑数据并预测未来趋势。
SMA方法的基本思想是，在预测时利用过去一定时期内的数据的平均值来估计未来的趋势。具体步骤如下：

1.确定移动窗口大小：首先需要确定用于计算移动平均的窗口大小。这个窗口可以视数据的周期性和预测的时间跨度而定。
    较短的窗口可以更敏感地反映近期变化，但可能会忽略长期趋势；较长的窗口则可以平滑噪声，但反应变化相对较慢。

2.计算移动平均值：根据选定的窗口大小，按照时间顺序计算每个时间点的移动平均值。
    假设窗口大小为n，在第t个时间点，计算方法为将前n个时间点的数据相加，再除以n，得到第t个时间点的移动平均值。
    SMA(t) = (x(t) + x(t-1) + … + x(t-n+1)) / n
    其中，x(t)表示第t个时间点的数据。

3.进行预测：在计算得到移动平均值之后，可以利用这些平均值进行未来的预测。最简单的方法是使用最新的移动平均值作为对未来趋势的预测。
    例如，如果我们计算了最后10个时间点的移动平均值，那么可以将最新的移动平均值作为未来一个时间点的预测值。
    预测值 = SMA(t)

需要注意的是，SMA方法在预测时只考虑了移动平均值，并未考虑其他因素的影响，例如趋势的加速或减速、季节性变化等。
因此，在实际应用中，SMA通常被视为更复杂的时间序列预测方法的基础，可以作为其他模型的基准或辅助方法来使用。
'''

import numpy as np


def simple_moving_average(data, window_size):
    moving_averages = []
    n = len(data)

    for i in range(window_size, n + 1):
        window = data[i - window_size:i]
        average = np.mean(window)
        moving_averages.append(average)

    return moving_averages


# 示例数据
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
window_size = 3

# 计算移动平均值
moving_averages = simple_moving_average(data, window_size)
print("移动平均值:", moving_averages)

# 进行预测
last_average = moving_averages[-1]
print("预测值:", last_average)


'''
上述代码首先定义了一个simple_moving_average函数，它接受一个数据列表和窗口大小作为参数，并返回移动平均值的列表。
然后，我们提供了示例数据data和窗口大小window_size，并调用simple_moving_average函数计算移动平均值。
最后，我们可以使用最后一个移动平均值作为预测值。
请注意，示例代码中使用了NumPy库中的mean函数来计算窗口内数据的均值。
你可以通过安装NumPy来使用该代码，例如通过pip install numpy命令安装。
'''