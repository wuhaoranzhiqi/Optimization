import gurobipy as grb

m = grb.Model()

# 定义变量
d11 = m.addVar(lb=0, vtype=grb.GRB.CONTINUOUS, name='d11')
d12 = m.addVar(lb=0, vtype=grb.GRB.CONTINUOUS, name='d12')
d21 = m.addVar(lb=0, vtype=grb.GRB.CONTINUOUS, name='d21')
d22 = m.addVar(lb=0, vtype=grb.GRB.CONTINUOUS, name='d22')
d31 = m.addVar(lb=0, vtype=grb.GRB.CONTINUOUS, name='d31')
d32 = m.addVar(lb=0, vtype=grb.GRB.CONTINUOUS, name='d32')
x1 = m.addVar(lb=0, vtype=grb.GRB.CONTINUOUS, name='x1')
x2 = m.addVar(lb=0, vtype=grb.GRB.CONTINUOUS, name='x2')
x3 = m.addVar(lb=0, vtype=grb.GRB.CONTINUOUS, name='x3')

# 添加约束
m.addConstr(2 * x1 + x2 + x3 == 11)
m.addConstr(x1 - x2 + d11 - d12 == 0)
m.addConstr(x1 + 2 * x2 + d21 - d22 == 10)
m.addConstr(8 * x1 + 10 * x2 + d31 - d32 == 56)

# 添加目标
# 此处priority的值只要目标1比目标2大，目标2比目标3大即可，具体可查看官方文档
m.setObjectiveN(d12, index=0, priority=9, name='obj1')
m.setObjectiveN(d21 + d22, index=1, priority=6, name='obj2')
m.setObjectiveN(d31, index=2, priority=3, name='obj3')

# 求解
m.optimize()

# 查看变量值
for v in m.getVars():
    print(v.varName, '=', v.x)
# x1 = 2
# x2 = 4

# 查看各个目标函数值
for i in range(3):
    m.setParam(grb.GRB.Param.ObjNumber, i)
    print('Obj%d = ' % (i + 1), m.ObjNVal)
# Obj1 =  0.0
# Obj2 =  0.0
# Obj3 =  0.0
# 查看最终的目标函数值
print('8 * x1 + 10 * x2 =', 8 * 2 + 10 * 4)
# 8 * x1 + 10 * x2 = 56
