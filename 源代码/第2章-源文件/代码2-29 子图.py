import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False

fig = plt.figure(figsize=(10, 10))  # 指定画布大小

ax1 = fig.add_subplot(2, 2, 1)  # 添加一个子图，返回子图句柄
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
ax4 = fig.add_subplot(2, 2, 4)

# 子图1绘制sin图形
x = np.linspace(start=0, stop=30, num=300)
y = np.sin(x)
ax1.plot(x, y)
ax1.set_title('子图1')

# 子图2绘制散点图
x = np.random.randint(low=2, high=10, size=10)
y = np.random.randint(low=2, high=10, size=10)
ax2.scatter(x, y)  # 绘制散点图
ax2.set_title('子图2')

# 子图3绘制直方图
x = np.random.normal(loc=0, scale=1, size=1000)
ax3.hist(x=x, bins=50)
ax3.set_title('子图3')

# 子图4绘制组合图
x1 = np.linspace(start=0, stop=30, num=300)
y1 = np.sin(x1)
x2 = np.random.randint(low=0, high=10, size=10)
y2 = np.random.randint(low=0, high=10, size=10) / 10

# 绘制组合图
ax4.plot(x1, y1, color='b', label='line plot')
ax4.scatter(x2, y2, color='r', label='scatter plot')
ax4.set_title('子图4')

# 最后显示图形
plt.show()
