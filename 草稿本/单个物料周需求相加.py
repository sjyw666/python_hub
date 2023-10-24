#研发者：时间遗忘
#开发时间：2023/8/31 13:45
import pandas as pd

# 读取Excel文件
data_file = '6个物料的所有订单数据.xlsx'
xls = pd.ExcelFile(data_file)

# 循环读取每个子表格并处理
output_file = '6个物料的周订单数据.xlsx'

with pd.ExcelWriter(output_file) as writer:
    for sheet_name in xls.sheet_names:
        df = pd.read_excel(data_file, sheet_name=sheet_name)

        # 将日期列转换为日期类型
        df['日期'] = pd.to_datetime(df['日期'])

        # 按周进行分组并累加需求量
        df_weekly = df.groupby(pd.Grouper(key='日期', freq='W-MON')).agg({'需求量': 'sum'}).reset_index()

        # 将结果写入新的子表格中
        df_weekly.to_excel(writer, sheet_name=sheet_name, index=False)

print("已生成新的Excel文件:", output_file)
