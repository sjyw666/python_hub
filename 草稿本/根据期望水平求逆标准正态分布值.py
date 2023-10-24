#研发者：时间遗忘
#开发时间：2023/9/1 8:44
from scipy.stats import norm

probability = 0.90
inverse_std_normal_dist = norm.ppf(probability)

print("逆标准正态分布值为:", inverse_std_normal_dist)
