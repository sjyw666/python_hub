#研发者：时间遗忘
#开发时间：2023/9/20 10:45
#柱状图
#数据的准备工作
#定义变量名，例如：
import matplotlib.pyplot as plt

movie_name=['名字']
#横坐标
x=range(len(movie_name))
#纵坐标（票房数据）
y = []

#创建画布
plt.Figure(figsize=(20,15),dpi=1080)

#绘制柱状图
plt.bar(x,y,width=0.5,color=['b','r','g','y','c','m','y','k','c','g','b'])

#修改坐标刻度显示
plt.xticks(x,movie_name)

#显示网格
plt.gird(True,linesstylie="--",alpha=0.5)

#添加标题
plt.title('电影票房收入比较')

#图像显示
plt.show()