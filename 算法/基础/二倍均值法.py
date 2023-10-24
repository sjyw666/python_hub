# 研发者：时间遗忘
# 开发时间：2023/10/20 17:14
'''二倍均值法是一种常用的红包分发算法，可以确保每个红包都有一定的价值，并且最后一个红包不会太小。它的基本思想是：将总金额均匀地分配给每个红包，每次分配的金额都是前一个红包的两倍均值。

以下是一个简单的示例，使用二倍均值法来分发10元的红包给5个人：

1.
初始化总金额为10元，总人数为5人。
2.
首先，计算出第一个红包的金额，它等于总金额除以总人数，即
10
元 / 5
人 = 2
元。
3.
随机生成一个比例因子（0.5
到1
.5
之间的随机数），将第一个红包的金额乘以这个比例因子，得到第一个人的红包金额，例如
2
元 * 1.2 = 2.4
元。
4.
更新总金额为总金额减去第一个人的红包金额，即
10
元 - 2.4
元 = 7.6
元。
5.
再次计算出第二个红包的金额，它等于剩余金额除以剩余人数，即
7.6
元 / 4
人 = 1.9
元。
6.
随机生成比例因子，计算第二人的红包金额。
7.
重复上述步骤，直到所有人都分配到红包为止。

下面是一个简化的Python示例代码，用于演示二倍均值法'''


import random


def distribute_red_packets(total_amount, num_people):
    result = []
    remaining_amount = total_amount * 100  # 将金额转换为分
    remaining_people = num_people

    for i in range(num_people):
        if remaining_people == 1:
            amount = remaining_amount
        else:
            # 计算均值
            average = remaining_amount / remaining_people
            # 随机生成比例因子，范围为0.5到1.5
            rand_factor = random.uniform(0.5, 1.5)
            amount = int(average * rand_factor)

        result.append(amount / 100)  # 将分转换为元
        remaining_amount -= amount
        remaining_people -= 1

    return result


total_amount = 10  # 总金额为10元
num_people = 5  # 分给5个人
red_packets = distribute_red_packets(total_amount, num_people)

print("随机分配的红包金额：")
for amount in red_packets:
    print(f"{amount:.2f}元")

'''这段代码模拟了使用二倍均值法分发10元给5个人的情况，确保每个红包都有一定的价值，同时最后一个红包不会太小'''