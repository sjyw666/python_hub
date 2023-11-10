# 研发者：时间遗忘
# 开发时间：2023/11/2 15:52
# 特点说明：
'''

'''
import os
import patoolib

# 指定压缩文件路径
compress_file_path = r"E:\数模\比赛\泰迪杯\近年泰迪杯赛题\2022年泰迪杯赛题\2022年“泰迪杯”A题\A题：竞赛作品的自动评判数据\A题：竞赛作品的自动评判数据\DataA.rar"

# 解压到当前目录
output_directory = os.path.splitext(compress_file_path)[0]

# 创建同名子文件夹
os.makedirs(output_directory, exist_ok=True)

# 使用patoolib来解压文件
patoolib.extract_archive(compress_file_path, outdir=output_directory)

# 创建"summary"子文件夹
summary_folder = os.path.join(output_directory, "summary")
os.makedirs(summary_folder, exist_ok=True)

# 遍历每个作品文件夹
for root, dirs, files in os.walk(output_directory):
    for dir in dirs:
        work_folder = os.path.join(root, dir)
        image_folder = os.path.join(work_folder, "image")
        os.makedirs(image_folder, exist_ok=True)

        # 解压作品文件夹中的子文件
        subfolder_compress_files = [f for f in os.listdir(work_folder) if f.endswith((".zip", ".rar", ".7z")]

        for subfolder_file in subfolder_compress_files:
            subfolder_file_path = os.path.join(work_folder, subfolder_file)
            subfolder_output_folder = os.path.join(work_folder, os.path.splitext(subfolder_file)[0])
            os.makedirs(subfolder_output_folder, exist_ok=True)
            patoolib.extract_archive(subfolder_file_path, outdir=subfolder_output_folder)

print("解压和文件夹创建完成")
