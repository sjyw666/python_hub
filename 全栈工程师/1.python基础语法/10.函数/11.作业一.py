# 研发者：时间遗忘
# 开发时间：2023/10/11 10:18
import random
import time

# 输入红包金额
rp_money = float(input("请输入红包金额："))

# 输入红包个数
rp_amount = int(input("请输入红包个数："))

# 输入祝福语
greeting_input = input("请输入祝福语：")

greeting_list = ['金榜题名', '马到成功', '一帆风顺', '步步高升', '飞黄腾达']

# 没有输入祝福语自动选择
if not greeting_input:
    greeting = random.choice(greeting_list)
else:
    greeting = greeting_input

print(greeting)

# 自动@每个人，同时后面接一句“准备抢红包了！！”
personnel_list = ['韩跳跳', '李白白', '亚连连', '戈娅娅', '上官官']
for i in personnel_list:
    print('@' + i + ' ', end='')
print('准备抢红包了！！!')

# 使用二倍均值法分配红包金额
def distribute_red_packets(total_amount, num_packets):
    result = []
    remaining_amount = total_amount
    remaining_packets = num_packets

    for i in range(num_packets - 1):
        # 计算均值
        average = remaining_amount / remaining_packets
        # 随机生成比例因子，范围为0.5到1.5
        rand_factor = random.uniform(0.5, 1.5)
        amount = round(average * rand_factor, 2)#round表示四舍五入函数，后面的数字参数表示需要保留的小数位数
        result.append(amount)
        remaining_amount -= amount
        remaining_packets -= 1

    result.append(round(remaining_amount, 2))
    random.shuffle(result)  # 打乱红包顺序
    return result

random_amounts = distribute_red_packets(rp_money, rp_amount)

# 随机选人，人数为红包个数
for i in range(rp_amount):
    person_name = random.choice(personnel_list)
    personnel_list.remove(person_name)
    time.sleep(1)
    print(f'{person_name} 抢到 {random_amounts[i]} 元')
