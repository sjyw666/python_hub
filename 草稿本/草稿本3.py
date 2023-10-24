#研发者：时间遗忘
#开发时间：2023/3/28 20:44
#1-4作业项目
import time

aaa = time.time()
def pb(i):
    if i==1:
        return 1
    if i==2:
        return 1
    else:
        return pb(i-1)+pb(i-2)

ppp=pb(34)

bbb = time.time() - aaa
print(bbb)
print(ppp)

