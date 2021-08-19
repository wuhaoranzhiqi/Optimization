import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

mpl.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

# 绘制散点图
x = np.random.randint(low=2, high=10, size=10)
y = np.random.randint(low=2, high=10, size=10)
plt.scatter(x, y)  # 绘制散点图
plt.title("这是散点图")
plt.xlabel("x轴标签")
plt.ylabel("y轴标签")
plt.show()
