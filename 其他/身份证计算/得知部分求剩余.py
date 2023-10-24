#研发者：时间遗忘
#开发时间：2023/5/18 11:49

#前六位
ID_Top_6={"武汉市":420100,"黄石市":420200,"十堰市":420300,
          "宜昌市":420500,"襄阳市":420600,"鄂州市":420700,
          "荆门市":420800,"孝感市":420900,"荆州市":421000,
          "黄冈市":421100,"咸宁市":421200,"随州市":421300,
          "恩施州":422800,"仙桃市":429004,"潜江市":429005,
          "天门市":429006,"神农架林区":429021}

i=0
ID_Top_6_valse=list(ID_Top_6.values())
for qian6wei in ID_Top_6_valse:
       # 年份
       ID_78 = 19
       for ID_9_10 in range(1, 51):
              time=int(f'{ID_78}{ID_9_10}')
              if time%100==0:
                     if time % 400 == 0:
                            time_type = 0  # 闰年
                     else:
                            time_type = 1  # 平年
              else:
                     if time % 4 == 0:
                            time_type = 0  # 闰年
                     else:
                            time_type = 1  # 平年
              # 月份
              for month_number in range(1,13):
                     if month_number == 1 or month_number == 3 or month_number == 5 or month_number == 7 or month_number == 8 or month_number == 10 or month_number == 12:
                            day_number = 31
                     elif month_number == 4 or month_number == 6 or month_number == 9 or month_number == 11:
                            day_number = 30
                     elif month_number == 2:
                            if time_type==1:
                                   day_number=28
                            elif time_type==0:
                                   day_number=29

                     if len(str(month_number))==1:    # len是求字符串长度（len（字符串）），判断长度表示是否要加零
                            ID_11_12=int(f'0{month_number}')
                     elif len(str(month_number))==2:  # 随机数为2位数时
                            ID_11_12=month_number


                     # 日期
                     for date_number in range(1, int(day_number)):
                            if time_type==0:
                                   pass
                            elif time_type==1:
                                   pass

                            if len(str(date_number)) == 1:  # len是求字符串长度（len（字符串）），判断长度表示是否要加零
                                   ID_13_14 = int(f'0{date_number}')
                            elif len(str(date_number)) == 2:  # 随机数为2位数时
                                   ID_13_14 = date_number

                            month_and_date_number = int(f'{ID_11_12}{ID_13_14}')


                            for ID_15 in range(0, 10):# 第15位随机码
                                   # 最后固定3位
                                   ID_16_18 = 513
                                   ID=f'{qian6wei}{time}{month_and_date_number}{ID_15}{ID_16_18}'
                                   print(ID)
                                   i+=1


print(i)















