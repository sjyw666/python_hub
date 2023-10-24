# 研发者：时间遗忘
# 开发时间：2023/10/17 23:44
import difflib

def compare_files(file1, file2, encoding='utf-8'):
    with open(file1, 'r', encoding=encoding) as f1, open(file2, 'r', encoding=encoding) as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()

    # 创建差异比较器
    d = difflib.Differ()
    diff = list(d.compare(lines1, lines2))

    added = []
    missing = []

    line_number = 0  # 用于计算行号

    for line in diff:
        line_number += 1  # 增加行号
        if line.startswith('+ '):
            added.append((line_number, line[2:]))
        elif line.startswith('- '):
            missing.append((line_number, line[2:]))

    return added, missing

if __name__ == '__main__':
    file1 = '新.txt'  # 请将文件名替换为您要比较的第一个文件
    file2 = '旧.txt'  # 请将文件名替换为您要比较的第二个文件

    added, missing = compare_files(file1, file2)

    print("缺失的部分：")
    for line_number, line in missing:
        print(f"行号 {line_number}: {line}", end='')

    print("\n\n新增的部分：")
    for line_number, line in added:
        print(f"行号 {line_number}: {line}", end='')
