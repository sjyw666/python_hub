#研发者：时间遗忘
#开发时间：2023/8/7 15:10
import numpy as np
import pandas as pd
a=pd.read_csv('E:\数模\题目\第四次模拟_0804\21级老队员第四次模拟练习题目_0804\附件1PM2.5数据.txt',header=None)



b=a.values

mu=np.mean(b,axis=1)#求均值

fc=np.var(b,axis=1,ddof=1)#求方差

print(mu,fc)