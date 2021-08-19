from gurobipy import *
m = Model("LP model")

# 定义变量
x1 = m.addVar(lb=0, ub=150, vtype=GRB.INTEGER, name='x1')
x2 = m.addVar(lb=0, ub=150, vtype=GRB.INTEGER, name='x2')
x3 = m.addVar(lb=0, ub=150, vtype=GRB.INTEGER, name='x3')
x4 = m.addVar(lb=0, ub=150, vtype=GRB.INTEGER, name='x4')
x5 = m.addVar(lb=0, ub=150, vtype=GRB.INTEGER, name='x5')
x6 = m.addVar(lb=0, ub=150, vtype=GRB.INTEGER, name='x6')
x7 = m.addVar(lb=0, ub=150, vtype=GRB.INTEGER, name='x7')
x8 = m.addVar(lb=0, ub=150, vtype=GRB.INTEGER, name='x8')

# 添加约束
m.addConstr(2*x1 + x2 + x3 + x4 >= 100)
m.addConstr(2*x2 + x3 + 3*x5 + 2*x6 + x7 >=150)
m.addConstr(x1 + x3 + 3*x4 + 2*x6 + 3*x7 + 5*x8 >=100)

# 添加目标函数
m.setObjective(5*x1 + 6*x2 + 23*x3 + 5*x4 + 24*x5 + 6*x6 +23*x7 + 5*x8, GRB.MINIMIZE)

# 求解
m.optimize()
print('最优值：', m.objVal)
for v in m.getVars():
print('参数', v.varName, '=', v.x)
