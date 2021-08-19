import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False

# 绘制正弦曲线，并修改图形属性
x1 = np.linspace(start=0, stop=30, num=300)
y1 = np.sin(x1)
x2 = np.random.randint(low=0, high=10, size=10)
y2 = np.random.randint(low=0, high=10, size=10) / 10

# 先绘制折线图，用蓝色
plt.plot(x1, y1, color='b', label='line plot')
# 再绘制散点图，用红色
plt.scatter(x2, y2, color='r', label='scatter plot')

plt.title("组合图")
plt.legend(loc='best')  # 显示图例
plt.show()
