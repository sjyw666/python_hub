# 研发者：时间遗忘
# 开发时间：2023/10/21 9:20
# 特点说明：读取所有行政区号文件生成随机合理身份证
import random
import pandas as pd
import os


# 读取 Excel 文件
def read_region_codes(file_path):
    df = pd.read_excel(file_path)

    # 将 '行政区号' 列转换为数值并排除非整数值
    region_codes = pd.to_numeric(df["行政区号"], errors="coerce")
    region_codes = region_codes.dropna().astype(int).tolist()

    return region_codes

# 生成身份证号
def generate_sfzh(region_codes, num_to_generate):
    sfzh_list = []

    for _ in range(num_to_generate):
        region_code = random.choice(region_codes)

        year = random.randint(1950, 2003)
        month = random.randint(1, 12)
        days_in_month = 31 if month != 2 else 29 if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else 28
        day = random.randint(1, days_in_month)
        birthday_code = f"{year:04d}{month:02d}{day:02d}"

        sequence_code = f"{random.randint(1, 999):03d}"

        sfzh_1_17 = f"{region_code}{birthday_code}{sequence_code}"

        def calculate_check_code(s1):
            multiplier = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
            total = sum(int(digit) * multiplier[i] for i, digit in enumerate(s1))
            remainder = ["1", "0", "X", "9", "8", "7", "6", "5", "4", "3", "2"]
            return remainder[total % 11]

        sfzh_18 = calculate_check_code(sfzh_1_17)

        sfzh = f"{sfzh_1_17}{sfzh_18}"
        sfzh_list.append(sfzh)

    return sfzh_list


# 获取当前目录
current_directory = os.path.dirname(__file__) if "__file__" in locals() else os.getcwd()

# 指定生成的 Excel 文件的绝对路径
file_path = os.path.join(current_directory, "行政区号生成数据.xlsx")  # 从当前目录下读取

# 读取行政区号
region_codes = read_region_codes(file_path)

# 指定生成的身份证数量
num_to_generate = 10  # 替换为你需要的数量

# 生成身份证号
sfzh_list = generate_sfzh(region_codes, num_to_generate)

# 打印生成的身份证号
for i, sfzh in enumerate(sfzh_list, 1):
    print(f"{i}. 生成的身份证号为: {sfzh}")

