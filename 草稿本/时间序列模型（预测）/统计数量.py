#研发者：时间遗忘
#开发时间：2023/9/10 0:31
import pandas as pd

# 读取包含数据的Excel文件
df = pd.read_excel("附件1统计性分析.xlsx")

# 设置日期列
df["Date"] = pd.to_datetime(df[["年", "月", "日"]])

# 计算每天的观测时间点数量
df["观测时间点数量"] = df.groupby("Date")["时间"].transform("count")

# 选择仅包含相关列的DataFrame
result_df = df[["年", "月", "日", "观测时间点数量"]]

# 保存结果到一个新的Excel文件
result_df.to_excel("result_file.xlsx", index=False)
