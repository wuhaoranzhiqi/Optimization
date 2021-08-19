import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation


# 这是一个卡车类
class car():
    def __init__(self, color):
        self.x = 1
        self.y = 1
        self.color = color

    def move(self):
        """在东南西北四个方向随机选一个方向走一步，然后更新坐标"""
        # 随机移动一步
        self.x = self.x + np.random.randint(low=-1, high=2, size=1)[0]
        self.y = self.y + np.random.randint(low=-1, high=2, size=1)[0]
        # 防止越界
        self.x = self.x if self.x > 0 else 0
        self.x = self.x if self.x < 10 else 10
        self.y = self.y if self.y > 0 else 0
        self.y = self.y if self.y < 10 else 10


# 实例化3辆车
cars = [car(color='r'), car(color='b'), car(color='g')]

# 绘制一张画布
fig = plt.figure()

i = list(range(1, 1000))  # 模拟1000个时间点


# update 是核心函数，在每个时间点操作图形对象
def update(i):
    plt.clf()  # 清空图层
    # 对每辆卡车进行操作
    for c in cars:
        c.move()  # 移动1步
        x = c.x
        y = c.y
        color = c.color
        plt.xlim(0, 10)  # 限制图形区域
        plt.ylim(0, 10)
        plt.scatter(x, y, color=color)  # 绘制卡车
    return


ani = animation.FuncAnimation(fig, update)
plt.show()
