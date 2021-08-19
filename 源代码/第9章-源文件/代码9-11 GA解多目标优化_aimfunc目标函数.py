# 目标函数 aimfuc.py
# 在使用时，请将文件名修改为 aimfunc.py，和main.py放在同一目录下
import numpy as np

def aimfuc(Phen, LegV):
    x1 = Phen[:, 0];
    x2 = Phen[:, 1]
    fun1 = x1 ** 4 - 10 * x1 ** 2 + x1 * x2 + x2 ** 4 - x1 ** 2 * x2 ** 2
    fun2 = x2 ** 4 - x1 ** 2 * x2 ** 2 + x1 ** 4 + x1 * x2
    # 对矩阵进行转置使得目标函数矩阵符合geatpy数据结构
    return [np.vstack([fun1, fun2]).T, LegV]