import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

mpl.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

# 绘制折线图，以sin函数为例
x = np.linspace(start=0, stop=30, num=300)
y = np.sin(x)
plt.plot(x, y)
plt.title("这是折线图")
plt.xlabel("x轴标签")
plt.ylabel("y轴标签")
plt.show()
