# 3D散点图
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

# 生成画布
fig = plt.figure()
ax = fig.gca(projection='3d')  # 指定为3D图形

# 绘制红色点100个
x1 = np.random.random(100) * 20
y1 = np.random.random(100) * 20
z1 = x1 + y1
ax.scatter(x1, y1, z1, c='r', marker='o')

# 绘制蓝色点100个
x2 = np.random.random(100) * 20
y2 = np.random.random(100) * 20
z2 = x2 + y2
ax.scatter(x2, y2, z2, c='b', marker='^')

plt.show()
