#研发者：时间遗忘
#开发时间：2023/9/9 10:15
import numpy as np
import matplotlib.pyplot as plt

# 输入数据
water_level = np.array([42.79, 42.97, 42.81, 42.79, 43.03, 42.5, 42.57, 42.62, 42.37, 42.34, 42.26, 42.09, 42.02, 41.94, 42.1, 42.15, 42.58, 42.5, 42.72, 42.77, 42.85, 42.95, 42.92, 43.04, 43.37, 43.33, 43.56, 43.23, 43.02, 42.96, 42.85, 42.89, 42.89, 42.88, 42.79, 42.75])
flow_rate = np.array([497, 584, 506, 497, 614, 382, 407, 426, 342, 335, 314, 265, 248, 232, 325, 355, 705, 592, 761, 802, 870, 959, 931, 1140, 1490, 1450, 1660, 1130, 951, 914, 852, 873, 906, 899, 844, 820])
sediment_concentration = np.array([1.37, 0.952, 0.996, 0.977, 1.42, 2.01, 2.25, 1.36, 1.02, 0.796, 0.634, 0.674, 0.284, 0.318, 0.324, 0.958, 2.57, 1.21, 2.6, 3.74, 3.93, 3.39, 3.08, 4.95, 7.71, 7.74, 9.22, 4.57, 2.13, 2.61, 1.96, 2.5, 2.58, 3.29, 2.12, 2.81])

# 有序聚类分析结果
best_split_point_water = 30
best_split_point_flow = 20
best_split_point_sediment = 28

# 绘制效果图
plt.figure(figsize=(12, 8))

# 水位效果图
plt.subplot(3, 1, 1)
plt.plot(water_level[:best_split_point_water], 'b')
plt.plot(water_level[best_split_point_water:], 'r')
plt.axvline(x=best_split_point_water, color='k', linestyle='--')
plt.xlabel('Time')
plt.ylabel('Water Level')
plt.title('Ordered Clustering - Water Level')

# 流量效果图
plt.subplot(3, 1, 2)
plt.plot(flow_rate[:best_split_point_flow], 'b')
plt.plot(flow_rate[best_split_point_flow:], 'r')
plt.axvline(x=best_split_point_flow, color='k', linestyle='--')
plt.xlabel('Time')
plt.ylabel('Flow Rate')
plt.title('Ordered Clustering - Flow Rate')

# 含沙量效果图
plt.subplot(3, 1, 3)
plt.plot(sediment_concentration[:best_split_point_sediment], 'b')
plt.plot(sediment_concentration[best_split_point_sediment:], 'r')
plt.axvline(x=best_split_point_sediment, color='k', linestyle='--')
plt.xlabel('Time')
plt.ylabel('Sediment Concentration')
plt.title('Ordered Clustering - Sediment Concentration')

plt.tight_layout()
plt.show()
