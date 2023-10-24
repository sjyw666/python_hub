#研发者：时间遗忘
#开发时间：2023/9/8 19:30
import pandas as pd
import statsmodels.api as sm
from sklearn.preprocessing import PolynomialFeatures

data = pd.read_excel('2018年.xlsx')  # 替换为你的文件路径

print(data.columns.tolist())

# 定义因变量和自变量
y_column_name = '含沙量'  # 替换为你的因变量列名
x_column_names = ['水位', '含沙量']  # 替换为你的自变量列名

y = data[y_column_name]
X = data[x_column_names]

poly = PolynomialFeatures(interaction_only=True, include_bias=False)
X_poly = poly.fit_transform(X)

X_with_intercept = sm.add_constant(X_poly)

model = sm.OLS(y, X_with_intercept)
results = model.fit()

print(results.summary())