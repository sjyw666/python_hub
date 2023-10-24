#研发者：时间遗忘
#开发时间：2023/7/9 9:57
for i in range(1,1001):#外部循环1000次
    for j in range(1,1001):
        if i-1<=j and j<=i+1:
            if j==i:
                z = f'4*X_{j}'
            else:
                z = f'X_{j}'
        else:
            continue
        print(z, end='+')
    print(f'\b={i};')