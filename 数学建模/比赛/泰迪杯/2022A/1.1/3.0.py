# 研发者：时间遗忘
# 开发时间：2023/11/2 15:44
# 特点说明：
'''

'''
import os
import zipfile
import patoolib
import shutil
import time

# 记录开始时间
start_time = time.time()

# 指定目录包含子压缩包的路径
source_directory = r"E:\数模\比赛\泰迪杯\近年泰迪杯赛题\2022年泰迪杯赛题\2022年“泰迪杯”A题\A题：竞赛作品的自动评判数据\A题：竞赛作品的自动评判数据\DataA.rar"

# 创建一个目录用于存放解压后的子文件夹
output_directory = r"D:\Python学习\数学建模\比赛\泰迪杯\2022A\批量解压缩压缩包\解压文件夹"
os.makedirs(output_directory, exist_ok=True)

# 创建名为"summary"的子文件夹
summary_folder = "summary"
os.makedirs(summary_folder, exist_ok=True)

# 遍历源目录中的每个子压缩包
for root, dirs, files in os.walk(source_directory):
    for file in files:
        if file.endswith((".zip", ".rar", ".7z")):
            archive_file_path = os.path.join(root, file)
            output_folder = os.path.join(output_directory, os.path.splitext(file)[0])

            # 创建image文件夹
            image_folder = os.path.join(output_folder, "image")
            os.makedirs(image_folder, exist_ok=True)

            # 使用不同的解压工具解压不同类型的文件
            if file.endswith(".zip"):
                with zipfile.ZipFile(archive_file_path, 'r') as zip_ref:
                    zip_ref.extractall(output_folder)
            elif file.endswith(".rar"):
                try:
                    if not os.path.exists(output_folder):
                        patoolib.extract_archive(archive_file_path, outdir=output_folder)
                except patoolib.util.PatoolError as e:
                    print(f"Error: {e}")
                    continue
            elif file.endswith(".7z"):
                try:
                    if not os.path.exists(output_folder):
                        patoolib.extract_archive(archive_file_path, outdir=output_folder)
                except patoolib.util.PatoolError as e:
                    print(f"Error: {e}")
                    continue

            # 复制task2_3.pdf文件到image文件夹
            for root, dirs, files in os.walk(output_folder):
                for file in files:
                    if file == "task2_3.pdf":
                        pdf_file_path = os.path.join(root, file)
                        # 检查源文件和目标文件是否相同，只复制不同的文件
                        if pdf_file_path != os.path.join(image_folder, file):
                            shutil.copy(pdf_file_path, image_folder)

# 记录结束时间
end_time = time.time()

# 计算执行时间
execution_time = end_time - start_time
print(f"执行时间: {execution_time} 秒")

print("子文件夹创建和文件复制完成")
