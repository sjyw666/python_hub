#研发者：时间遗忘
#开发时间：2023/8/13 13:29
'''
最初在进行Lasso回归时，一般会通过sklearn库进行实现。但是，了解其内部的Python实现对于掌握Lasso回归建模和算法的原理和特性非常有帮助。下面给出了一个Python实现的Lasso回归建模过程。
'''
#步骤一：加载数据
import numpy as np

def load_data():
    # 加载数据集
    data = np.loadtxt("data.txt", delimiter=",")

    # 将数据拆分为特征和标签
    X = data[:, :-1] # 特征
    y = data[:, -1] # 标签
    return X, y

#步骤二：搭建模型
class LassoRegressor:
    def __init__(self, alpha=1, l1_ratio=0.5, max_iter=1000, tol=1e-3):
        self.alpha = alpha # l1正则化系数
        self.l1_ratio = l1_ratio # L1/L2正则化比率
        self.max_iter = max_iter # 最大迭代次数
        self.tol = tol # 损失函数变化量的阈值

    def _soft_threshold(self, x, lambda_):
        if x > 0 and lambda_ < abs(x):
            return x - lambda_
        elif x < 0 and lambda_ < abs(x):
            return x + lambda_
        else:
            return 0

    def fit(self, X, y):
        self.n_samples, self.n_features = X.shape

        # 初始化theta
        self.theta = np.zeros(self.n_features)

        # 初始化损失函数二范数
        self.cost_his = []

        for i in range(self.max_iter):
            # 计算预测结果并计算残差
            y_pred = X.dot(self.theta)
            residuals = y - y_pred

            # 更新theta
            for j in range(self.n_features):
                X_j = X[:, j]
                soft_threshold = self._soft_threshold(X_j.T.dot(residuals), self.alpha*self.l1_ratio)
                self.theta[j] = soft_threshold / (1 + self.alpha*(1-self.l1_ratio))

            # 计算损失函数
            cost = np.sum((y_pred - y)**2) + self.alpha*np.sum(np.abs(self.theta))
            self.cost_his.append(cost)

            # 判断损失函数是否收敛
            if len(self.cost_his) > 1:
                if abs(self.cost_his[-1] - self.cost_his[-2]) < self.tol:
                    break

        return self

    def predict(self, X):
        return X.dot(self.theta)

'''
代码中，我们定义了一个 LassoRegressor 类，包含了以下几个方法：
– __init__(self, alpha, l1_ratio, max_iter, tol): 初始化方法，包括正则化系数、L1/L2比例、最大迭代次数和损失函数变化门限。
– _soft_threshold(self, x, lambda_): 辅助计算函数，主要用于计算软阈值。
– fit(self, X, y): 训练方法，拟合数据集，通过更新参数theta来减少损失函数。
– predict(self, X): 预测方法，通过theta和特征集X来预测标签。
'''

#步骤三：测试模型
'''通过下面这段代码来测试上面的模型：'''
from sklearn.datasets import make_regression
from sklearn.linear_model import Lasso
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# 生成样本数据
X, y = make_regression(n_samples=100, n_features=10, random_state=0, noise=0.5)

# 划分数据集
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

# 建立sklearn的Lasso模型并拟合
lasso_sklearn = Lasso(alpha=1.0)
lasso_sklearn.fit(X_train, y_train)
y_pred_sklearn = lasso_sklearn.predict(X_test)

# 建立自己的Lasso模型并拟合
lasso_self = LassoRegressor(alpha=1.0)
lasso_self.fit(X_train, y_train)
y_pred_self = lasso_self.predict(X_test)

# 对比两者效果
print("sklearn mean squared error: ", mean_squared_error(y_test, y_pred_sklearn))
print("self mean squared error: ", mean_squared_error(y_test, y_pred_self))

# 绘制损失函数曲线
plt.plot(range(len(lasso_self.cost_his)), lasso_self.cost_his)
plt.title("Lasso Regression Cost History")
plt.xlabel("Number of Iterations")
plt.ylabel("Cost")
plt.show()

'''
上述代码中，我们首先生成了一个包含100个样本数据和10个特征的人工数据集，然后将其分为训练集和测试集。接着，我们评估了最终的预测结果，并且输出了其均方误差。最后，我们绘制损失函数的历史曲线以及与sklearn库结果进行对比，以验证我们上述模型的准确性和可信度。
'''