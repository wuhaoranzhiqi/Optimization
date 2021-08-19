import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

mpl.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

# 直方图
x = np.random.normal(loc=0, scale=1, size=1000)
plt.hist(x=x, bins=50)
plt.title("这是直方图")
plt.xlabel("x轴标签")
plt.ylabel("y轴标签")
plt.show()
