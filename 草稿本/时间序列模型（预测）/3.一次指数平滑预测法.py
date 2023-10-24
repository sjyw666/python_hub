#研发者：时间遗忘
#开发时间：2023/9/2 22:36
'''
一次指数平滑预测法（Single Exponential Smoothing）是基于指数平滑方法的一种时间序列预测技术。
它适用于平稳或趋势稳定的数据，并用于生成未来时期的预测。
一次指数平滑预测法的基本概念是对历史观测值进行加权平均，其中较新的观测值具有较高的权重。
该方法假设未来的观测值与过去的加权平均值有关，且权重以指数形式递减。
一次指数平滑预测法的公式如下：
P(t) = α * Y(t) + (1 - α) * P(t-1)
其中，P(t)表示时刻t的预测值，Y(t)为时刻t的观测值，P(t-1)为时刻t-1的预测值，α为平滑系数（0 ≤ α ≤ 1）。
在该公式中，时刻t的预测值是当前观测值与上一次预测值的加权平均。
平滑系数α决定了历史观测值对预测值的相对权重，较大的α值对应较快的适应性，但也会较快地忽略过去观测值的影响。
预测过程的初始阶段需要指定初始预测值。
通常，初始预测值可以设定为时间序列的第一个观测值。
一次指数平滑预测法的优点是简单且易于实现，但不适用于数据具有较强的趋势或季节性的情况。
对于这些情况，可以使用二次指数平滑或季节性指数平滑等更复杂的方法。
总之，一次指数平滑预测法是一种常用且简单的时间序列预测技术，适用于平稳或趋势稳定的数据，但在使用时需要注意选择合适的平滑系数。
'''


def single_exponential_smoothing(data, alpha):
    predictions = []
    n = len(data)
    prev_prediction = data[0]  # 初始预测值

    for i in range(n):
        current_data = data[i]
        prediction = alpha * current_data + (1 - alpha) * prev_prediction
        predictions.append(prediction)
        prev_prediction = prediction

    return predictions


# 示例数据
data = [10, 12, 15, 16, 18, 20, 22]
alpha = 0.2  # 平滑系数

# 进行预测
predictions = single_exponential_smoothing(data, alpha)
print("预测值:", predictions)



'''
在上述代码中，我们定义了一个single_exponential_smoothing函数，它接受一个数据列表和平滑系数作为参数，并返回预测值的列表。
函数中使用一次指数平滑预测法的公式进行预测。
我们提供了示例数据data和平滑系数alpha，并调用single_exponential_smoothing函数进行预测。
最后，我们得到了预测值的列表。
需要注意的是，平滑系数alpha的选择对于预测结果的影响很大。
较小的alpha值会使模型更加稳定，但可能较慢地响应数据的变化。
较大的alpha值会使模型更快地适应数据的变化，但可能会过度拟合噪声或异常值。
因此，在实际应用中，需要根据具体情况选择合适的平滑系数。
'''