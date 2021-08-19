# 目标函数文件：aimfuc.py
# 在使用时，请将文件名修改为 aimfunc.py，和main.py放在同一目录下
import numpy as np

def aimfuc(Phen, LegV):
    # 目标函数
    x = Phen[:, [0]]
    y = Phen[:, [1]]
    f = np.sin(x + y) + (x + y) ** 2 - 1.5 * x + 2.5 * y + 1
    return [f, LegV]