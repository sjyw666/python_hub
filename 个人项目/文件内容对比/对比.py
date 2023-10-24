# 研发者：时间遗忘
# 开发时间：2023/10/11 14:40
import difflib

def compare_files(file1, file2,encoding='utf-8'):
    with open(file1, 'r', encoding=encoding) as f1, open(file2, 'r', encoding=encoding) as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()

    # 创建差异比较器
    d = difflib.Differ()
    diff = list(d.compare(lines1, lines2))

    added = []
    missing = []

    for line in diff:
        if line.startswith('+ '):
            added.append(line[2:])
        elif line.startswith('- '):
            missing.append(line[2:])

    return added, missing

if __name__ == '__main__':
    file1 = '新.txt'  # 请将文件名替换为您要比较的第一个文件
    file2 = '旧.txt'  # 请将文件名替换为您要比较的第二个文件

    added, missing = compare_files(file1, file2)

    print("缺失的部分：")
    for line in added:
        print(line, end='')

    print("\n\n新增的部分：")
    for line in missing:
        print(line, end='')
