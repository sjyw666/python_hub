#研发者：时间遗忘
#开发时间：2023/9/20 10:57
#柱状图
#数据的准备工作
#定义变量名，例如：
import matplotlib.pyplot as plt

movie_name=['qiangshen']
#横坐标
x=range(len(movie_name))
#纵坐标（票房数据）
y = [32,56,85,79,85,85,81,75,97,68,51]

#创建画布
plt.Figure(figsize=(20,15),dpi=1080)

#绘制柱状图
plt.bar(x,y,width=0.5,color=['b','r','g','y','c','m','y','k','c','g','b'])

#修改坐标刻度显示
plt.xticks(x,movie_name)

#显示网格
plt.grid(True, linestyle="--", alpha=0.5)

#添加标题
plt.title('电影票房收入比较')

#图像显示
plt.show()


'''
#柱状图

#定义变量名，例如：
import matplotlib.pyplot as plt

#数据的准备工作
movie_name=['名字']

first_day=["票房数据"]
first_weekend = ["一周后的票房数据"]

#横坐标
x=range(len(movie_name))

#纵坐标（票房数据）
y = []

#创建画布
plt.Figure(figsize=(20,15),dpi=1080)

#绘制柱状图
plt.bar(x, first_day, width=0.2,label="首日票房",color=['b','r'])
plt.bar([i+0.2,for i in x], first_weekend, width=0.2,label="首周票房",color=['b','r'])

#显示图例
plt.legend()

#修改坐标刻度显示
plt.xticks([i+0.1,for i in x],movie_name)

#显示网格
plt.gird(linesstylie="--",alpha=0.5)

#添加标题
plt.title('电影票房收入比较')

#图像显示
plt.show()
'''