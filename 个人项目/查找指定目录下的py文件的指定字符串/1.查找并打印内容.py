#研发者：时间遗忘
#开发时间：2023/10/8 9:39
import os

# 指定目录和要查找的字符串
directory = "D:\Python学习\全栈工程师\python语法"
search_string = "向后"

# 遍历目录下的文件
for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith(".py"):  # 仅处理Python文件
            file_path = os.path.join(root, file)
            with open(file_path, "r", encoding="utf-8") as f:
                contents = f.read()
                if search_string in contents:
                    print(f"文件名：{file_path}")
                    print("文件内容：")
                    print(contents)
                    print("=" * 50)
                    # 如果需要，你可以在这里添加其他操作，比如打开文件

# 如果你想在找到指定字符串后自动打开文件，可以使用以下代码
# import subprocess
# subprocess.Popen(["notepad.exe", file_path])  # 用你喜欢的文本编辑器替换notepad.exe
