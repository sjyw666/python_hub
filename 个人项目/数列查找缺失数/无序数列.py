#研发者：时间遗忘
#开发时间：2023/10/8 11:41
'''将列表转换为字典，通过列表元素遍历字典，在字典中查找'''
def find_missing_number_unsorted(arr, start, end):
    num_set = set(arr)

    for i in range(start, end + 1):
        if i not in num_set:
            return i

    return -1  # 如果没有缺失的数字，可以返回一个特殊值，如 -1


arr = [11, 13, 14, 16, 17, 18, 20]
start = 10
end = 20

missing_number = find_missing_number_unsorted(arr, start, end)
print(f"缺失的数字是：{missing_number}")
