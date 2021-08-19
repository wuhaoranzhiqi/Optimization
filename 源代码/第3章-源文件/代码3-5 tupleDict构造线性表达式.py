import gurobipy as grb

# tupledict类型的变量快速创建约束条件
import gurobipy as grb

m = grb.Model()
x = m.addVars(3, 4, vtype=grb.GRB.BINARY, name="x")
m.addConstrs((x.sum(i, '*') <= 1 for i in range(3)), name="con")
m.update()
m.write("tupledict_vars.lp")

# 将会创建如下的约束：
# con[0]: x[0, 0] + x[0, 1] + x[0, 2] + x[0, 3] <= 1
# con[1]: x[1, 0] + x[1, 1] + x[1, 2] + x[1, 3] <= 1
# con[2]: x[2, 0] + x[2, 1] + x[2, 2] + x[2, 3] <= 1
