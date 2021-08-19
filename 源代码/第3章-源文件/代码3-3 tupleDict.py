import gurobipy as grb

model = grb.Model()

# 定义变量的下标
tl = [(1, 1), (1, 2), (1, 3),
      (2, 1), (2, 2), (2, 3),
      (3, 1), (3, 2), (3, 3)]
vars = model.addVars(tl, name="d")

# 基于元素下标的操作
print(sum(vars.select(1, '*')))
# 输出
# <gurobi.LinExpr: d[1,1] + d[1,2] + d[1,3]>
