# 研发者：时间遗忘
# 开发时间：2023/10/18 20:56
'''计算两个非负整数p和q的最大公约数；
若q是0，则最大公约数为p，
否则，将p除以q得到余数r、p和q的最大公约数即为q和r的最大公约数'''

def gys(p,q):
    if q==0:
        return p
    r=p%q
    return gys(q,r)

a=int(input("请输入第一个整数："))
b=int(input("请输入第二个整数："))

print('最大公约数为；',gys(a,b))