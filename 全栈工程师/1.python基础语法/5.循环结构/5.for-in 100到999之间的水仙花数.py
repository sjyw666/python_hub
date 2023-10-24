#研发者：时间遗忘
#开发时间：2022/9/30 11:15

'''输出100到999之间的水仙花数
   举例
   153=3*3*3+5*5*5+1*1*1    个位数的三次方加十位数上的三次方再加上百位数上的三次方的和相等的数为水仙花数
'''


for item in range(100,1000):
    ge=item%10                    #个位上的数
    shi=item//10%10               #十位上的数
    bai=item//100                 #百位上的数
    #print(ge,shi,bai)            用于查看打印输出的数
    if ge**3+shi**3+bai**3==item:
       print(item)                #注意判断print的位置

print("100-999之间的水仙花数有")
for i in range(100,999):
    ge1=i%10%10
    shi1=i//10%10
    bai1=i//100
    if i==ge1**3+shi1**3+bai1**3:
        print(i)
