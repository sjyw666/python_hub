#研发者：时间遗忘
#开发时间：2023/9/8 19:06
'''下面是一个使用Python读取Excel文件，指定因变量和自变量，并建立包含一次项和交互项的多元线性回归模型的示例代码：'''
import pandas as pd
import numpy as np
import statsmodels.api as sm

# 读取Excel文件，指定因变量和自变量的列名
df = pd.read_excel('2018年.xlsx')
y_column = '含沙量'  # 指定因变量列名
x_columns = ['水位', '流量']  # 指定自变量列名

# 构建自变量矩阵 X 和因变量向量 y
X = df[x_columns]
X = sm.add_constant(X)  # 添加常数列，代表截距
y = df[y_column]

# 添加交互项
interaction_terms = ['X1:X2', 'X1:X3']  # 指定交互项列名
X_with_interaction = X.copy()
for term in interaction_terms:
    terms = term.split(':')
    interaction = X[terms[0]] * X[terms[1]]
    X_with_interaction[term] = interaction

# 建立多元线性回归模型
model = sm.OLS(y, X_with_interaction)
results = model.fit()

# 打印回归结果
print(results.summary())

'''请注意，你需要将 "your_file.xlsx" 替换为你的Excel文件的路径，并使用实际的因变量和自变量列名替换 "Y"、"X1"、"X2"、"X3"。如果你需要添加更多的交互项，可以修改 interaction_terms 列表。
该代码使用 pandas 库读取Excel文件，并使用 statsmodels.api 库建立多元线性回归模型。首先，通过 pd.read_excel() 函数读取Excel文件。然后，将自变量列存储在 X 矩阵中，并通过 sm.add_constant() 函数添加常数列，代表截距项。因变量则存储在向量 y 中。
接下来，通过遍历指定的交互项列表，计算出交互项并添加到自变量矩阵 X_with_interaction 中。
最后，使用 sm.OLS() 函数建立多元线性回归模型，传入因变量向量和包含自变量和交互项的矩阵。通过 model.fit() 进行拟合得到回归结果，并使用 results.summary() 打印回归结果摘要信息。
请确保已安装需要的库（pandas、numpy、statsmodels）以及在代码中正确引用了它们。同时，根据你的数据的实际情况进行适当的替换和调整。'''