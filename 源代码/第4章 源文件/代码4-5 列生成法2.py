import gurobipy as grb

model = grb.Model()

# 添加变量
a1 = model.addVar(vtype=grb.GRB.INTEGER, name='a1')
a2 = model.addVar(vtype=grb.GRB.INTEGER, name='a2')
a3 = model.addVar(vtype=grb.GRB.INTEGER, name='a3')
a4 = model.addVar(vtype=grb.GRB.INTEGER, name='a4')

# 添加约束
model.addConstr(3 * a1 + 7 * a2 + 9 * a3 + 16 * a4 <= 20)
# 目标函数
model.setObjective(1 - 0.166666 * a1 - 0.5 * a2 - 0.5 * a3 - a4, grb.GRB.MINIMIZE)
# 求解
model.optimize()
print('目标函数值是：', model.objVal)
for v in model.getVars():
    print(v.varName, '=', v.x)
# 输出
# 目标函数值是： -0.333
# a1 = 2.0
# a2 = 2.0
# a3 = -0.0
# a4 = 0.0
