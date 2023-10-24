#研发者：时间遗忘
#开发时间：2023/9/8 18:31
'''以下是一个使用Python进行三次样条插值、绘制预测图和实际值曲线对比的示例代码。这个示例假设你使用的Excel文件有一列数据，你可以指定要读取的列进行插值和对比。'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# 读取Excel文件，指定要读取的列
df = pd.read_excel("附件", usecols=["Column_name"])
data = df["含沙量(kg/m3) "]

# 创建插值函数
x = np.arange(len(data))
cs = CubicSpline(x, data)

# 预测值
x_pred = np.linspace(0, len(data) - 1, 100)  # 预测值的 x 范围
y_pred = cs(x_pred)  # 通过插值函数获得预测的 y 值

# 绘制预测图和实际值曲线对比
plt.plot(x, data, 'o', label='Actual')  # 实际值曲线
plt.plot(x_pred, y_pred, label='Predicted')  # 预测值曲线
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

'''在代码中，你需要替换 "yourfile.xlsx" 为你的Excel文件的路径，并将 "Columnname" 替换为你要读取的具体列名。
这段代码将通过CubicSpline函数创建三次样条插值函数，并使用linspace函数生成预测值的范围。然后，使用插值函数 cs 对预测值范围进行插值操作，得到预测的y值，最后使用plt.plot()函数绘制实际值曲线和预测值曲线。
请注意，这只是一个示例代码，并且需要安装 pandas、matplotlib 和 scipy 库来运行这段代码。你可以使用 pip 或者 conda 来安装这些库。同时，为了适应你的具体情况，你可能需要根据实际需求进行一些修改和调整。'''