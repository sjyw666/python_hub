#研发者：时间遗忘
#开发时间：2023/9/9 9:09
import numpy as np
import matplotlib.pyplot as plt

from scipy.interpolate import interp1d, CubicSpline

# 示例数据
x = np.array([1, 2, 3, 4, 5])
y = np.array([1, 4, 9, 16, 25])

# 插值方法
methods = ['linear', 'polynomial', 'cubic spline']

# 生成插值函数
linear_interp = interp1d(x, y, kind='linear')
polynomial_interp = interp1d(x, y, kind='quadratic')
cubic_spline_interp = CubicSpline(x, y)

# 生成插值点
x_new = np.linspace(1, 5, 200)

# 计算插值结果
y_linear = linear_interp(x_new)
y_polynomial = polynomial_interp(x_new)
y_cubic_spline = cubic_spline_interp(x_new)

# 绘制原始数据和插值后的折线图
plt.plot(x, y, 'bo', label='原始数据')
plt.plot(x_new, y_linear, label='线性插值')
plt.plot(x_new, y_polynomial, label='多项式插值')
plt.plot(x_new, y_cubic_spline, label='三次样条插值')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('原始数据和插值后的折线图')
plt.grid(True)
plt.show()
