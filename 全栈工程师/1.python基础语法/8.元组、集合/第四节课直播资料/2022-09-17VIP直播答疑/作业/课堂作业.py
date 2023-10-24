#student:李氏小生
#任务1：
lst_name=['《长津湖》57.44亿','《战狼2》56.95亿','《你好，李焕英》54亿','《哪吒之魔童降世》50.36亿','《流浪地球》46.91亿']
#计算总票房：
lst_boxoffice=[56.95,56.95,54,50.36,46.91] # 这个总的计算结果好像有点问题？少了差不多一个亿啊？第一个值应该是57.44
sum=0
for i in lst_boxoffice:
    sum +=i
print('-'*10,'方法1','-'*10)
for i in lst_name:
    print(i)
print('票房总收入为：',round(sum,2),'亿') # 计算结果保留2位小数

print('-'*10,'方法2','-'*10)
for i in range(len(lst_name)):
    print(lst_name[i])
print('票房总收入为：',round(sum,2),'亿')

print('-'*10,'方法3','-'*10)
for index,item in enumerate(lst_name,start=1000):
    print(index,'-->',item)
print('票房总收入为：', round(sum, 2), '亿','\n\n')

#任务2：
lst_name_a=['   猫砂\t  ',' 儿童滑冰鞋','蒙牛核桃牛奶']
lst_number=[2,1,1]
lst_price=[18.90,218.00,49.80]
#这就是我能想到的遍历方法了，能解决问题但可能不太恰当
times=0
print('  商品名','  单价','  数量',' 小计',sep='\t  ')
while times<=2:
    print(lst_name_a[times],'￥'+str(lst_price[times]),lst_number[times],'￥'+str(lst_price[times]*lst_number[times]),sep='   ')
    times+=1
#调试这个间距挺麻烦的，请问老师有什么好的办法吗？
