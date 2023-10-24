# 研发者：时间遗忘
# 开发时间：2023/10/20 20:21
# 说明：生成随机合理的身份证号
import random
import pandas as pd

# 指定生成的 Excel 文件的绝对路径
file_path = "D:\Python学习\个人项目\生成合理随机的身份证号\行政区号生成数据.xlsx"  # 替换为实际的绝对路径

# 读取 Excel 文件
df = pd.read_excel(file_path)

# 从数据框中提取行政区号并存储在列表中
region_codes = df["行政区号"].tolist()

# 现在 region_codes 列表中包含了所有的行政区号
# 将身份证号的前六位从列表中随机抽取
sfzh_1_6 = int(random.choice(region_codes))




def generate_birthday_code():
    # 生成随机的年份（范围可根据需要自行调整）
    year = random.randint(1950, 2003)

    # 生成随机的月份（1到12之间）
    month = random.randint(1, 12)

    # 根据月份确定每月的天数，假设一个月最多有31天
    days_in_month = 31

    # 对于2月，根据闰年和平年确定天数
    if month == 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            days_in_month = 29
        else:
            days_in_month = 28

    # 生成随机的日（1到月份对应的天数之间）
    day = random.randint(1, days_in_month)

    # 格式化成六位的生日码，如19800101
    birthday_code = f"{year:04d}{month:02d}{day:02d}"

    return birthday_code


# 生成生日码
sfzh_7_14 = generate_birthday_code()


'''
birthday_code = f"{year:04d}{month:02d}{day:02d}" 是一种使用 f-string 格式化字符串的方式，用于将年份、月份和日期合并成一个六位的生日码。

这行代码的工作方式如下：

{year:04d}: 这部分将年份 year 格式化为四位数字，不足四位的年份将在前面用零填充，确保输出的年份是四位数字。例如，年份 1990 会被格式化为 "1990"。
{month:02d}: 这部分将月份 month 格式化为两位数字，不足两位的月份将在前面用零填充，确保输出的月份是两位数字。例如，月份 5 会被格式化为 "05"。
{day:02d}: 同样的方式，这部分将日期 day 格式化为两位数字，不足两位的日期将在前面用零填充
'''

'''
在 f-string 中，格式化选项 `d` 用于格式化整数。具体来说，`d` 表示以十进制格式输出整数，通常用于确保整数的输出是十进制数值而不包含小数部分。

以下是使用 `d` 格式化选项的示例：

number = 42
formatted = f"The answer is {number:d}."
# 输出：The answer is 42.


在这个示例中，`{number:d}` 将整数 `number` 格式化为十进制整数，结果是字符串 "42"。

需要注意的是，`d` 格式化选项通常用于整数类型的数据，如果应用于浮点数，会将其转换为整数并去掉小数部分。如果你需要保留小数部分，应使用其他格式化选项，如 `f` 用于浮点数。
'''
#生成顺序码
def sequence_codes():
    a=random.randint(1,999)
    return f'{a:03d}'

sfzh_15_17 =  sequence_codes()

def check_code(s1,s2,s3):
    a = str(s1)
    b = str(s2)
    c = str(s3)
    lianjieshu =f'{a}{b}{c}'
    multiplier = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    acount = 0  #次数
    total = 0   #乘积总数
    for i in lianjieshu:
        acount += 1
        zhuan = int(i)
        product = zhuan * multiplier[acount-1]
        total += product

    remainder = ["1","0","X","9","8","7","6","5","4","3","2"]
    for i in range(11):
        if 0<=total % 11<=10:
            d = remainder[i]
            return d
        else:
            continue





sfzh_1_17 = f'{sfzh_1_6}{sfzh_7_14}{sfzh_15_17}'
print("身份证前17位为：",sfzh_1_17)
sfzh_18 = check_code(sfzh_1_6,sfzh_7_14,sfzh_15_17)
print("效验码为：",sfzh_18)
sfzh = f'{sfzh_1_17}{sfzh_18}'
print("身份证为：",sfzh)

print("年份为:",sfzh[6:10:1])    # 指定步长为1，不指定也可以，默认为1

print("月份为:",sfzh[10:12])

print("日期为:",sfzh[12:14])
