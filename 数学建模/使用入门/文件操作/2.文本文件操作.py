#研发者：时间遗忘
#开发时间：2023/8/11 11:30
with open('1.txt') as fp:
    L1=[]
    L2=[]
    for line in fp:
        L1.append(len(line))
        L2.append(len(line.strip()))    #去掉换行符
    data=[str(num)+'\t'for num in L2]   #转换为字符串
    print(L1)
    print(L2)
    with open('data2_42.txt','w') as fp2:
        fp2.writelines(data)