# 主函数main.py
import numpy as np
import geatpy as ga

AIM_M = __import__('aimfuc')
# 变量设置
ranges = np.array([[-5, -5], [5, 5]])  # 生成自变量的范围矩阵
borders = np.array([[1, 1], [1, 1]])  # 生成自变量的边界矩阵（1表示变量的区间是闭区间）
precisions = [1, 1]  # 根据crtfld的函数特性，这里需要设置精度为任意正值，否则在生成区域描述器时会默认为整数编码，并对变量范围作出一定调整
FieldDR = ga.crtfld(ranges, borders, precisions)  # 生成区域描述器
# 调用编程模板
[ObjV, NDSet, NDSetObjV, times] = ga.moea_nsga2_templet(
    AIM_M, 'aimfuc', None, None, FieldDR, 'R', maxormin=1,
    MAXGEN=500, MAXSIZE=200, NIND=25, SUBPOP=1, GGAP=1,
    selectStyle='tour', recombinStyle='xovdp', recopt=0.9, pm=0.6,
    distribute=True, drawing=1)

print('其中一个最优解是', ObjV[0])
# 用时：3.41090 秒
# 帕累托前沿点个数：200 个
# 单位时间找到帕累托前沿点个数：58 个
# 其中一个最优解是 [ 90.081716   132.51084595]
