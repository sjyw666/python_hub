#研发者：时间遗忘
#开发时间：2023/9/16 19:55
def fac(n):
    if n==1:
        return 1
    else:
        return n*fac(n-1)

print(fac(6))

def fac2(n):
    if n==1:
        return 1
    else:
        res=n * fac2(n - 1)
        return res

print(fac2(6))