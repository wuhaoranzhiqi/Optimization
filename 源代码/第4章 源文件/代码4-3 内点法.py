import numpy as np
import time

def gradient(x1, x2, t):
    """计算目标函数在x处的一阶导数（雅克比矩阵）"""
    j1 = -70 * t + 3 / (-3 * x1 - 9 * x2 + 540) + 5 / (-5 * x1 - 5 * x2 + 450) + 9 / (-9 * x1 - 3 * x2 + 720) - 1 / x1
    j2 = -30 * t + 9 / (-3 * x1 - 9 * x2 + 540) + 5 / (-5 * x1 - 5 * x2 + 450) + 3 / (-9 * x1 - 3 * x2 + 720) - 1 / x2
    return np.asmatrix([j1, j2]).T

def hessian(x1, x2):
    """计算目标函数在x处的二阶导数（海塞矩阵）"""
    x1, x2 = float(x1), float(x2)
    h11 = 9 / (3 * x1 + x2 - 240) ** 2 + (x1 + 3 * x2 - 180) ** (-2) + (x1 + x2 - 90) ** (-2) + x1 ** (-2)
    h12 = 3 / (3 * x1 + x2 - 240) ** 2 + 3 / (x1 + 3 * x2 - 180) ** 2 + (x1 + x2 - 90) ** (-2)
    h21 = 3 / (3 * x1 + x2 - 240) ** 2 + 3 / (x1 + 3 * x2 - 180) ** 2 + (x1 + x2 - 90) ** (-2)
    h22 = (3 * x1 + x2 - 240) ** (-2) + 9 / (x1 + 3 * x2 - 180) ** 2 + (x1 + x2 - 90) ** (-2) + x2 ** (-2)
    return np.asmatrix([[h11, h12], [h21, h22]])

def invertible(H):
    """求海塞矩阵的逆矩阵"""
    H_1 = np.linalg.inv(H)
    return H_1

def main():
    x = np.asmatrix(np.array([10, 10])).T  # x 是牛顿法的初始迭代值
    t = 0.00001  # t 是指示函数的中的t
    eps = 0.01  # 迭代停止的误差
    iter_cnt = 0  # 记录迭代的次数
    while iter_cnt < 20:
        iter_cnt += 1
        J = gradient(x[0, 0], x[1, 0], t)
        H = hessian(x[0, 0], x[1, 0])
        H_1 = np.linalg.inv(H)  # 还塞矩阵的逆
        x_new = x - H_1 * J  # 牛顿法公式
        error = np.linalg.norm(x_new - x)  # 求2范数，判断迭代效果
        print('迭代次数是：%d, x1=%.2f, x2=%.2f, 误差是：%.2f' % (iter_cnt, x_new[0, 0], x_new[1, 0], error))
        x = x_new
        if error < eps:
            break
        time.sleep(1)
    # 打印结果
    print("目标函数值是：%.2f" % float(70 * x[0, 0] + 30 * x[1, 0]))
    # 输出
    # 目标函数值是：2021.17
