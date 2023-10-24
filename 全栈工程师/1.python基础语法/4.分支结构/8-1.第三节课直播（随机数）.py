#研发者：时间遗忘
#开发时间：2022/9/27 11:08

import random
train_number=random.randint(1,8)                                 #产生1-8的随机数，包括1，也包括8
print('车厢号为：0'+str(train_number))
seat_number=random.randint(1,200)
if len(str(seat_number))==1:                                     #len是求字符串长度（len（字符串）），判断长度表示是否要加零
    print(f'您的座位号为：0{train_number}车00{seat_number}B')       #B为自己选择
elif len(str(seat_number))==2:                                   #随机数为2位数时
    print(f'您的座位号为：0{train_number}车0{seat_number}B')
elif len(str(seat_number))==3:                                   #随机数为3位数时
    print(f'您的座位号为：0{train_number}车{seat_number}B')




#随机生成26个英文字母
'''char=[]
for i in range(1,27):
    chars.append(chr(i))
chars'''


#用upper()来转化大小写
import numpy as np
a1=np.arange(97,123)
b1=[chr(i) for  i in a1]
print(b1)