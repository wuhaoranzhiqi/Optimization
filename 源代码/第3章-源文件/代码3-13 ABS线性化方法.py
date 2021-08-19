import gurobipy as grb

m = grb.Model()
x = m.addVar(lb=-10, name='x')
y = m.addVar(name='y')
m.addConstr(y == grb.abs_(x), name='C_abs')
m.addConstr(x>=-5, name='C_2')
m.addConstr(x <= 3, name='C_3')

m.setObjective(y, -1)  # 求最大
m.optimize()
print("y=", y.X)
print("x=", x.X)
# 输出
# y= 5.0
# x= -5.0
