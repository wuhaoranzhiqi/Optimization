import pandas as pd
from pandas import DataFrame
import numpy as np
# 定义线性规划求解函数
def lp_solver(matrix: DataFrame):
    """
    输入线性规划的矩阵，根据单纯形法求解线性规划模型
     max cx
    s.t. ax<=b
    矩阵形式是：
             b    x1    x2   x3   x4   x5
    obj    0.0  70.0  30.0  0.0  0.0  0.0
    x3   540.0   3.0   9.0  1.0  0.0  0.0
    x4   450.0   5.0   5.0  0.0  1.0  0.0
    x5   720.0   9.0   3.0  0.0  0.0  1.0
    第1行是目标函数的系数
    第2-4行是约束方程的系数
    第1列是约束方程的常数项
    obj-b 交叉，即第1行第1列的元素是目标函数的负值
    x3,x4,x5 是松弛变量，也是初始可行解
    :param matrix:
    :return:
    """
    # 检验数是否大于0
    c = matrix.iloc[0, 1:]
    while c.max() > 0:
        # 选择入基变量，目标函数系数最大的变量入基
        c = matrix.iloc[0, 1:]
        in_x = c.idxmax()
        in_x_v = c[in_x]  # 入基变量的系数
        # 选择出基变量
        # 选择正的最小比值对应的变量出基 min( b列/入基变量列)
        b = matrix.iloc[1:, 0]
        in_x_a = matrix.iloc[1:][in_x]  # 选择入基变量对应的列
        out_x = (b / in_x_a).idxmin()  # 得到出基变量
        # 旋转操作
        matrix.loc[out_x, :] = matrix.loc[out_x, :] / matrix.loc[out_x, in_x]
        for idx in matrix.index:
            if idx != out_x:
                matrix.loc[idx, :] = matrix.loc[idx, :] - matrix.loc[out_x, :] * matrix.loc[idx, in_x]
        # 索引替换（入基出基变量名称替换）
        index = matrix.index.tolist()
        i = index.index(out_x)
        index[i] = in_x
        matrix.index = index
    # 打印结果
    print("最终的最优单纯形法是：")
    print(matrix)
    print("目标函数值是：", - matrix.iloc[0, 0])
    print("最优决策变量是：")
    x_count = (matrix.shape[1] - 1) - (matrix.shape[0] - 1)
    X = matrix.iloc[0, 1:].index.tolist()[: x_count]
    for xi in X:
        print(xi, '=', matrix.loc[xi, 'b'])


# 主程序代码
def main():
    # 约束方程系数矩阵，包含常数项
    matrix = pd.DataFrame(
        np.array([
            [0, 70, 30, 0, 0, 0],
            [540, 3, 9, 1, 0, 0],
            [450, 5, 5, 0, 1, 0],
            [720, 9, 3, 0, 0, 1]]),
        index=['obj', 'x3', 'x4', 'x5'],
        columns=['b', 'x1', 'x2', 'x3', 'x4', 'x5'])

    # 调用前面定义的函数求解
    lp_solver(matrix)

# 输出
# 最终的最优单纯形法是：
#           b   x1   x2   x3   x4        x5
# obj -5700.0  0.0  0.0  0.0 -2.0 -6.666667
# x3    180.0  0.0  0.0  1.0 -2.4  1.000000
# x2     15.0  0.0  1.0  0.0  0.3 -0.166667
# x1     75.0  1.0  0.0  0.0 -0.1  0.166667
# 目标函数值是： 5700.0
# 最优决策变量是：
# x1 = 75.0
# x2 = 15.0