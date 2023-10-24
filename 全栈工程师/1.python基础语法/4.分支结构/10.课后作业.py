#研发者：时间遗忘
#开发时间：2022/9/28 9:10

print('--------------车次信息--------------')
print('车次：G103    出发站：北京南    到达站：上海虹桥     出发时间：06:20     到达时间：11:50    历时：05:38（当日到达）')
print('座位等级：1.商务座/特等座   2.一等座    3.二等座/二等包座')
print('座位数：\t\t\t13\t\t\t有\t\t\t有')
print('价格：\t\t1873.0\t\t930.0\t\t\t553.0')

#选择座位等级
seat=eval(input('-----请选择座位等级：1.商务座/特等座   2.一等座    3.二等座/二等包座-----'))
if type(seat)==int:
    if seat<1 or seat>3:
        seat='二等座/二等包座'
        seat_money = 553
        print('输入错误，已默认选择二等座/二等包座')
    if seat == 1:
        seat = '商务座/特等座'
        seat_money=1873
        print('已选择商务座/特等座')
    elif seat == 2:
        seat = '一等座'
        seat_money=930
        print('已选择一等座')
    elif seat == 3:
        seat = '二等座/二等包座'
        seat_money=553
        print('二等座/二等包座')
    else:
        seat = '二等座/二等包座'
        seat_money = 553
        print('输入错误，已默认选择二等座/二等包座')
else:
    seat = '二等座/二等包座'
    seat_money = 553
    print('输入错误，已默认选择二等座/二等包座')


#选择乘车人
passengers=eval(input('-----请选择乘车人：1杨淑娟    2.吴俊英-----'))
if type(passengers)==int:
    if passengers<1 or passengers>2:
        passengers = '杨淑娟'
        print('输入错误，已默认选择杨淑娟')
    if passengers == 1:
        passengers='杨淑娟'
        print('已选择杨淑娟')
    elif passengers == 2:
        passengers='吴俊英'
        print('已选择吴俊英')
    else:
        passengers = '杨淑娟'
        print('输入错误，已默认选择杨淑娟')
else:
    passengers = '杨淑娟'
    print('输入错误，已默认选择杨淑娟')


#选择票种
ticket_type=eval(input('-----请选择票种：1.成人票   2.儿童票-----'))
if type(ticket_type)==int:
    if ticket_type<1 or ticket_type>2:
        ticket='成人票'
        ticket_type=1
        print('输入错误，已默认选择成人票')
    elif ticket_type==1:
        ticket = '成人票'
        ticket_type = 1
        print('已选择成人票')
    elif ticket_type==2:
        ticket = '儿童票'
        ticket_type = 0.5
        print('已选择儿童票，儿童票半价')
    else:
        ticket = '成人票'
        ticket_type = 1
        print('输入错误，已默认选择成人票')
else:
    ticket = '成人票'
    ticket_type = 1
    print('输入错误，已默认选择成人票')


#选择座位
import random
print('-----窗\tA\tB\tC\t过道\t\tD\tF\t窗-----')
seat_number=eval(input('请选择座位：1.A   2.B   3.C  4.D  5.F  6.随机'))
if type(seat_number)==int:
    if seat_number<1 or seat_number>6:
        seat_number=random.randint(A,G)
        print('输入错误，已默认选择随机')
    elif seat_number==1:
        seat_number='A座位'
        print('已选择A号座位')
    elif seat_number==2:
        seat_number='B座位'
        print('已选择B号座位')
    elif seat_number==3:
        seat_number='C座位'
        print('已选择C号座位')
    elif seat_number==4:
        seat_number='D座位'
        print('已选择D号座位')
    elif seat_number==5:
        seat_number='E座位'
        print('已选择E号座位')
    elif seat_number==6:
        seat_number='随机'
        print('座位已选择随机')
        seat_number = random.randint(A, G)
else:
    seat_number = random.randint(A, G)
    print('输入错误，已默认选择随机')


#车厢随机选择
import random
random_carriage=random.randint(1,11)
if len(str(random_carriage))==1:
    random_1='0'+str(random_carriage)
else:
    random_1 = random_carriage
random_seat=random.randint(1,21)
if len(str(random_seat))==1:
    random_2='0'+str(random_seat)
else:
    random_2=random_seat


#打印车票
print('-------------您的车票信息为：-----------')
print('车次：G103    出发站：北京南    到达站：上海虹桥     出发时间：06:20     到达时间：11:50    历时：05:38（当日到达）')
print(f'乘车人：{passengers}\t\t座位等级：{seat}\t\t{random_1}车{random_2}排{seat_number}号\t\t\t{ticket}{seat_money*ticket_type}元')
payment=eval(input('是否确认支付：1.取消支付   2.确认支付'))
if type(payment)==int:
    if payment<1 or payment>2:
        print('输入错误，已取消支付')
    elif payment==1:
        print('已确认取消支付')
    elif payment==2:
        answer = input('确认支付？Yes/No')
        if answer == 'Yes':
            pay_way = eval(input('请选择支付方式：1.支付宝  2.微信  3.银行卡  4.亲友代付'))
            if type(pay_way) == int:
                if pay_way == 1:
                    print(f'已选择支付宝支付,支付宝优惠10元，已支付{ seat_money*ticket_type- 100}元')
                elif pay_way == 2:
                    print(f'已选择微信支付,已支付{seat_money*ticket_type}元')
                elif pay_way == 3:
                    print(f'已选择银行卡支付,已支付{seat_money*ticket_type}元')
                elif pay_way == 4:
                    print(f'已选择亲友代付,已支付{seat_money*ticket_type}元')
                else:
                    print('输入错误，已默认选择支付宝支付')
            else:
                print('输入错误，已默认选择支付宝支付')

        else:
            print('输入错误，已默认选择支付宝支付')
    else:
        print('输入错误，已取消支付')
else:
    print('输入错误，已取消支付')

