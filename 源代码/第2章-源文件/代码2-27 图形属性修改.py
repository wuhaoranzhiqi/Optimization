import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

mpl.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

# 绘制正弦曲线，并修改图形属性
x = np.linspace(start=0, stop=30, num=300)
y = np.sin(x)
plt.plot(x, y, color='r', marker='d', linestyle='--', linewidth=2, alpha=0.8)
plt.title('颜色：红，标记：棱形，线性：虚线，线宽：2，透明度：0.8')
plt.show()
