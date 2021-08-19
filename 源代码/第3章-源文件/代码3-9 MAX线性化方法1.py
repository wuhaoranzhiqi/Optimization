# 方法1：使用转换后的约束
# 假设 x=4, y=5
import gurobipy as grb

# 创建模型，定义变量
m = grb.Model()
x = m.addVar(name='x')
y = m.addVar(name='y')
z = m.addVar(name='z')
u1 = m.addVar(vtype='B', name='u1')
u2 = m.addVar(vtype='B', name='u2')
u3 = m.addVar(vtype='B', name='u3')
M = 10000

# 添加约束
m.addConstr(x <= z - M * (1 - u1), name='c1')
m.addConstr(y <= z - M * (1 - u2), name='c2')
m.addConstr(3 <= z - M * (1 - u3), name='c3')
m.addConstr(x == 4, name='c4')
m.addConstr(y == 5, name='c5')
m.addConstr(u1 + u2 + u3 >= 1, name='c6')
m.addConstr(x <= z, name='c7')
m.addConstr(y <= z, name='c8')
m.addConstr(3 <= z, name='c8')

# 定义目标函数并求解
m.setObjective(z)
m.optimize()
print("z=", z.X)
# 输出
# z= 5
