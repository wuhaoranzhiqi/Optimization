import gurobipy as grb

# 创建一个系数矩阵，用tuplelist格式存储
c1 = [(1, 1), (1, 2), (1, 3)]
coeff = grb.tupledict(c1)
coeff[(1, 1)] = 1
coeff[(1, 2)] = 0.3
coeff[(1, 3)] = 0.4

print(vars.prod(coeff, 1, '*'))
# 输出
# <gurobi.LinExpr: d[1,1] + 0.3 d[1,2] + 0.4 d[1,3]>
