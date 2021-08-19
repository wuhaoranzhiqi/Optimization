import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns

sns.set_style("whitegrid")
mpl.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

# 固定随机数种子
np.random.seed(1234)

# 一些参数
city_num = 10  # 城市的数量
iter_num = 1000  # 算法最大迭代次数

# 随机生成city_num个城市的坐标，注意是不放回抽样
X = np.random.choice(list(range(1, 100)), size=city_num, replace=False)
Y = np.random.choice(list(range(1, 100)), size=city_num, replace=False)

plt.scatter(X, Y, color='r')
plt.title('城市坐标图')
