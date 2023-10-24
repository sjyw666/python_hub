#研发者：时间遗忘
#开发时间：2022/9/30 16:37

#continue语句：用于结束当前循环，进入下一次循环，通常与分支结构if一起使用
#不管后面有多少代码，直接从头再来
'''
for ... in ...:               while （条件）：
    ...                         ...
    if ...:                     if ...:
       continue                    continue
    ...                         ...
'''

'''要求输出1-50之间所有5的倍数    5、10、15...
5的倍数共同点：   和5的余数为0的数都是5的倍数
什么样的数不为5的倍数：   和5的余数不为0的数都不是5的倍数
要求使用continue实现
'''

for item in range(1,51):
    if item%5==0:
        print(item)

print('----------使用continue--------')
for item in range(1,51):
    if item%5!=0:
        continue
    print(item)