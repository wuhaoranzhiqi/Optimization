# 3D曲线图
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

# 生成画布
fig = plt.figure()
ax = fig.gca(projection='3d')  # 指定为3D图形

# 生成(x,y,z)数据
theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
z = np.linspace(-2, 2, 100)
r = z ** 2 + 1
x = r * np.sin(theta)
y = r * np.cos(theta)

# 绘制图形
ax.plot(x, y, z)  # 曲线图和2D一样使用plot函数
plt.show()
