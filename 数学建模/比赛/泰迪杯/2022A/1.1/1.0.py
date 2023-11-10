# 研发者：时间遗忘
# 开发时间：2023/11/2 15:31
# 特点说明：
'''
将DataA2.rar文件进行解压，但是解压后并没有解压子文件
'''
import os
import patoolib
import time

start_time = time.time()
# 指定压缩文件路径
compress_file_path = r"E:\数模\比赛\泰迪杯\近年泰迪杯赛题\2022年泰迪杯赛题\2022年“泰迪杯”A题\A题：竞赛作品的自动评判数据\A题：竞赛作品的自动评判数据\DataA.rar"

# 解压到当前目录
output_directory = os.path.splitext(compress_file_path)[0]

# 创建同名子文件夹
os.makedirs(output_directory, exist_ok=True)

# 使用patoolib来解压文件
patoolib.extract_archive(compress_file_path, outdir=output_directory)

end_time = time.time()

yx_time = start_time - end_time

print(yx_time)