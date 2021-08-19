# 3D曲面图
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

# 生成画布
fig = plt.figure()
ax = fig.gca(projection='3d')  # 指定为3D图形

# 生成数据(x,y,z)
x = np.arange(-5, 5, 0.25)
y = np.arange(-5, 5, 0.25)
x, y = np.meshgrid(x, y)  # 重点，用np.meshgrid生成坐标网格矩阵
z = np.sin(np.sqrt(x ** 2 + y ** 2))

# 使用plot_surface函数
# cmap=cm.coolwarm 是颜色属性
surf = ax.plot_surface(x, y, z, cmap=cm.coolwarm)
plt.show()
