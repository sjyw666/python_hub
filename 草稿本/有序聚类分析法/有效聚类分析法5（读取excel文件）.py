#研发者：时间遗忘
#开发时间：2023/9/9 10:21
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams['font.family'] = 'SimHei'

def ordered_cluster_analysis(data):
    n = len(data)
    best_split_point = None
    min_total_variance = float('inf')

    for split_point in range(1, n):
        data_before = data[:split_point]
        data_after = data[split_point:]
        mean_before = np.mean(data_before)
        mean_after = np.mean(data_after)
        variance_before = np.sum((data_before - mean_before) ** 2)
        variance_after = np.sum((data_after - mean_after) ** 2)
        total_variance = variance_before + variance_after

        if total_variance < min_total_variance:
            min_total_variance = total_variance
            best_split_point = split_point

    return best_split_point

# 从Excel文件中读取数据
data = pd.read_excel('插值数据2021.xlsx')
water_level = data['水位'].values
flow_rate = data['流量'].values
sediment_concentration = data['含沙量'].values

# 对水位序列进行有序聚类分析
best_split_point_water = ordered_cluster_analysis(water_level)

# 对流量序列进行有序聚类分析
best_split_point_flow = ordered_cluster_analysis(flow_rate)

# 对含沙量序列进行有序聚类分析
best_split_point_sediment = ordered_cluster_analysis(sediment_concentration)

# 打印最优分割点
print("Best split point for water level:", best_split_point_water)
print("Best split point for flow rate:", best_split_point_flow)
print("Best split point for sediment concentration:", best_split_point_sediment)

# 绘制效果图
plt.figure(figsize=(12, 8))

# 水位效果图
plt.subplot(3, 1, 1)
plt.plot(water_level[:best_split_point_water], 'b')
plt.plot(water_level[best_split_point_water:], 'r')
plt.axvline(x=best_split_point_water, color='k', linestyle='--')
plt.xlabel('时间')
plt.ylabel('水位')
plt.title('有序聚类 - 水位')#Ordered Clustering 有序聚类

# 流量效果图
plt.subplot(3, 1, 2)
plt.plot(flow_rate[:best_split_point_flow], 'b')
plt.plot(flow_rate[best_split_point_flow:], 'r')
plt.axvline(x=best_split_point_flow, color='k', linestyle='--')
plt.xlabel('时间')
plt.ylabel('流量')
plt.title('有序聚类 - 流量')

# 含沙量效果图
plt.subplot(3, 1, 3)
plt.plot(sediment_concentration[:best_split_point_sediment], 'b')
plt.plot(sediment_concentration[best_split_point_sediment:], 'r')
plt.axvline(x=best_split_point_sediment, color='k', linestyle='--')
plt.xlabel('时间')
plt.ylabel('含沙量')
plt.title('有序聚类 - 含沙量')

plt.tight_layout()
plt.show()
