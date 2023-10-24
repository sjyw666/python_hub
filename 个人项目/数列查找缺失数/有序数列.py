#研发者：时间遗忘
#开发时间：2023/10/8 11:41
'''将列表的数字求和，和正常开始到结束的数列做差，差值就是缺失值'''
def find_missing_number(arr, start, end):
    expected_sum = sum(range(start, end + 1))
    actual_sum = sum(arr)
    return expected_sum - actual_sum

arr = [10, 11, 12, 13, 14, 15, 17, 18, 19, 20]
start = 10
end = 20

missing_number = find_missing_number(arr, start, end)
print(f"缺失的数字是：{missing_number}")
