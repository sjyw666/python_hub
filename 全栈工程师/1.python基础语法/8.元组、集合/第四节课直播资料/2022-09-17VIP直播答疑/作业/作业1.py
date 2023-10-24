# coding:utf-8
# author:杨淑娟
import time
englist=['counter','stall','shelf','price tag','discount','change','bank','shop']
chn=['柜台','售货摊','货架','标价签','打折扣','零钱','银行','商店']
# 转成字典
dic=dict(zip(englist,chn))
print('百折词')
times=eval(input('请设置每个单词停留时间(1-10秒):'))
for key in dic:
    print(key,'_________')
    time.sleep(times)

for value in dic.values():
    print(value,'_________')
    time.sleep(times)