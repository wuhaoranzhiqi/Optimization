# 目标函数文件：aimfuc.py
# 在使用时，请将文件名修改为 aimfunc.py，和main.py放在同一目录下
import numpy as np

def aimfuc(Phen, LegV):
    # Phen是表现型矩阵，第一列是x变量，第二列是y变量，行数等于染色体个数
    x = Phen[:, [0]]
    y = Phen[:, [1]]
    a = 2
    pi = 3.14
    # 目标函数
    f = 2 * a + x * x - a * np.cos(2 * pi * x) + y * y - a * np.cos(2 * pi * y)
    # 约束条件
    idx1 = np.where(x + y > 6)[0]
    idx2 = np.where(3 * x - 2 * y > 5)[0]
    # 惩罚方法： 标记非可行解在可行性列向量中对应的值为0，并编写punishing罚函数来修改非可行解的适应度。
    # 也可以不写punishing，因为Geatpy内置的算法模板及内核已经对LegV标记为0的个体的适应度作出了修改。
    # 使用punishing罚函数实质上是对非可行解个体的适应度作进一步的修改
    exIdx = np.unique(np.hstack([idx1, idx2]))
    LegV[exIdx] = 0
    return [f, LegV]

