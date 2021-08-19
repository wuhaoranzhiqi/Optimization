import gurobipy as grb

model = grb.Model()

# 定义整数变量
x1 = model.addVar(vtype=grb.GRB.INTEGER, name='x1')
x2 = model.addVar(vtype=grb.GRB.INTEGER, name='x2')

# 添加约束
model.addConstr(2 * x1 + 3 * x2 <= 14)
model.addConstr(4 * x1 + 2 * x2 <= 18)
model.addConstr(x1 >= 0)
model.addConstr(x2 >= 0)

# 定义目标函数
model.setObjective(3 * x1 + 2 * x2, sense=grb.GRB.MAXIMIZE)

# 求解
model.optimize()
print("目标函数值：", model.objVal)
for v in model.getVars():
    print('参数', v.varName, '=', v.x)

# 目标函数值： 14.0
# 参数 x1 = 4.0
# 参数 x2 = 1.0
