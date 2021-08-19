import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

mpl.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

# 绘制柱状图
x = ['a', 'b', 'c', 'd']
y = [3, 5, 7, 9]
plt.bar(x, y, width=0.5)
plt.title("这是柱状图")
plt.xlabel("x轴标签")
plt.ylabel("y轴标签")
plt.show()
