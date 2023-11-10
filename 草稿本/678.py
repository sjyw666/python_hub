# 研发者：时间遗忘
# 开发时间：2023/11/4 16:09
# 特点说明：
'''

'''
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,1.1,0.1)
print(x)
plt.figure(figsize=(28,8),dpi=80)
plt.plot(x,x+2)
plt.show()