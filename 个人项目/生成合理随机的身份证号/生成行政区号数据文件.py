# 研发者：时间遗忘
# 开发时间：2023/10/20 20:35
import os
import pandas as pd

# 获取当前文件的路径
current_directory = os.path.dirname(os.path.abspath(__file__ or 0))

# 构建新文件的完整路径
new_file_path = os.path.join(current_directory, "行政区号生成数据.xlsx")

# 读取原始 Excel 文件
file_path = "行政区号源数据.xlsx"  # 将文件路径替换为实际的文件路径
df = pd.read_excel(file_path, header=None, names=["data"])

# 使用空格分割数据并创建新的 DataFrame
df[["行政区名", "行政区号"]] = df["data"].str.extract(r'(\S+)\s(\d+)')

# 删除原始数据列
df.drop("data", axis=1, inplace=True)

# 保存新的 Excel 文件
df.to_excel(new_file_path, index=False)

print(f"新的 Excel 文件已保存到 {new_file_path}")
