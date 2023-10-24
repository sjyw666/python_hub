#研发者：时间遗忘
#开发时间：2023/4/26 20:04
t=(i for i in range(10) if i%2==0)
print(t)       #不加tuple，生成乱码    <generator object <genexpr> at 0x00000206C299D3C0>
print(tuple(t))#推导结果需要另行转换