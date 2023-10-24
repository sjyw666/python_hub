#研发者：时间遗忘
#开发时间：2023/9/9 9:51
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# 读取 Excel 文件
df = pd.read_excel('2021年-n.xlsx')

# 指定要使用的特征列数据
features = df[['水位', '含沙量']].values

# 应用有序聚类分析法
k = 3  # 聚类簇数
kmeans = KMeans(n_clusters=k)
clusters = kmeans.fit_predict(features)

# 可视化聚类结果
plt.figure(figsize=(8, 6))

# 绘制每个数据点的折线图
for i in range(k):
    cluster_points = features[clusters == i]
    x = cluster_points[:, 0]
    y = cluster_points[:, 1]
    plt.plot(x, y, marker='o', linestyle='-', label=f'Cluster {i+1}')

plt.xlabel('x')
plt.ylabel('y')
plt.title('有序聚类分析结果')
plt.legend()
plt.grid(True)
plt.show()
