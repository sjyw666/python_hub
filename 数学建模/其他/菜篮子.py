#研发者：时间遗忘
#开发时间：2023/3/28 20:44


for i in range(1,19):                           #外部循环打印19行
    for n in range(1,21-i):                     #内部20-i个式子，range循环（0，20）是20次，（1，21）也是20次
        for j in range(1,20):
            '''加数每次加一'''
            z = n + j
            assembly =f' X{n} + X{z} = {n + z}'
            print(assembly)

            A1 = 12000
            A4 = 12000
            A9 = 12000
            A13 = 12000
            A17 = 12000
            A20 = 12000

            A2 = 14000
            A3 = 14000
            A5 = 14000
            A8 = 14000
            A11 = 14000
            A14 = 14000
            A19 = 14000

            A6 = 15000
            A7 = 15000
            A10 = 15000
            A12 = 15000
            A15 = 15000
            A16 = 15000
            A18 = 15000

            '''acount1 = T1 * A1 + T2 * A2 + T3 * A3 + T4 * A4 + T5 * A5 + T6 * A6 + T7 * A7 + T8 * A8 + T9 * A9 + T10 * A10 + T11 * A11 + T12 * A12 + T13 * A13 + T14 * A14 + T15 * A15 + T16 * A16 + T17 * A17 + T18 * A18 + T19 * A19 + T20 * A20
            acount2 = T1 * A1 + T2 * A2 + T3 * A3 + T4 * A4 + T5 * A5 + T6 * A6 + T7 * A7 + T8 * A8 + T9 * A9 + T10 * A10 + T11 * A11 + T12 * A12 + T13 * A13 + T14 * A14 + T15 * A15 + T16 * A16 + T17 * A17 + T18 * A18 + T19 * A19 + T20 * A20

            if assembly==:
                print(assembly,acount1,acount2)
            print(f'{n}+{z}={n+z}',end='\t')    #打印输出各数与之和
            if z==20:
                break                           #限制加数最大不超过20
        print()                                 #换行
    break                                       #控制所有式子打印一次后退出循环





#T1==1 or 0'''




