#研发者：时间遗忘
#开发时间：2023/7/10 21:25
import time

aaa = time.time()
b=1000
a = b-2
i1=1
i2=1
for n in range(a):
    i3 = i1 + i2
    i1 = i2
    i2 = i3
bbb = time.time() - aaa
print(bbb)
print(i3)
