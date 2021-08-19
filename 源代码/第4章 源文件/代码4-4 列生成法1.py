import gurobipy as grb

model = grb.Model()
# 定义变量
z1 = model.addVar(vtype=grb.GRB.CONTINUOUS, name='z1')
z2 = model.addVar(vtype=grb.GRB.CONTINUOUS, name='z2')
z3 = model.addVar(vtype=grb.GRB.CONTINUOUS, name='z3')
z4 = model.addVar(vtype=grb.GRB.CONTINUOUS, name='z4')
# 添加约束
model.addConstr(6 * z1 >= 25)
model.addConstr(2 * z2 >= 30)
model.addConstr(2 * z3 >= 14)
model.addConstr(z4 >= 8)
model.addConstr(z1 >= 0)
model.addConstr(z2 >= 0)
model.addConstr(z3 >= 0)
model.addConstr(z4 >= 0)

# 目标函数
model.setObjective(z1 + z2 + z3 + z4, grb.GRB.MINIMIZE)
# 求解
model.optimize()
# 打印变量
for v in model.getVars():
    print(v.varName, '=', v.x)
# 获取约束的对偶变量的值
dual = model.getAttr(grb.GRB.Attr.Pi, model.getConstrs())
print(dual)
# 输出
# [0.16666, 0.5, 0.5, 1.0, 0.0, 0.0, 0.0, 0.0]
