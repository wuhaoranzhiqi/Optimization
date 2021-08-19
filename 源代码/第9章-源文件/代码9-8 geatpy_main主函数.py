# 主函数文件：main.py
import numpy as np
import geatpy as ga

# 导入目标函数
AIM_M = __import__('aimfuc')

# 变量设置
x1 = [-3, 12.1]  # 自变量1的范围
x2 = [4.1, 5.8]  # 自变量2的范围
b1 = [1, 1]  # 自变量1是否包含下界
b2 = [1, 1]  # 自变量2是否包含上界
codes = [0, 0]  # 自变量的编码方式，0表示采用标准二进制编码
precisions = [4, 4]  # 在二进制/格雷码编码中代表自变量的编码精度，当控制变量是二进制/格雷编码时，该参数可控制编码的精度
scales = [0, 0]  # 是否采用对数刻度
ranges = np.vstack([x1, x2]).T  # 生成自变量的范围矩阵
borders = np.vstack([b1, b2]).T  # 生成自变量的边界矩阵
# 生成区域描述器
FieldD = ga.crtfld(ranges, borders, precisions, codes, scales)

# 调用编程模板
[pop_trace, var_trace, times] = ga.sga_new_code_templet(
    AIM_M, 'aimfuc', None, None, FieldD, problem='R', maxormin=-1,
    MAXGEN=1000, NIND=100, SUBPOP=1, GGAP=0.8, selectStyle='sus',
    recombinStyle='xovdp', recopt=None, pm=None, distribute=True,
    drawing=0)

# 最优的目标函数值为：316.946
# 最优的控制变量值为：
# 12.1
# 5.8
# 有效进化代数：1000
# 最优的一代是第 31 代
# 时间已过 1.681 秒
