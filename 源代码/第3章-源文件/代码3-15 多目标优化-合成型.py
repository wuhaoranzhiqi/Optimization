# 合成型
import gurobipy as grb

model = grb.Model()

x = model.addVar(name='x')
y = model.addVar(name='y')

# 添加第1个目标
model.setObjectiveN(x + 2 * y, index=0, weight=3, name='obj1')
# 添加第2个目标
model.setObjectiveN(x - 3 * y, index=1, weight=0.5, name='obj2')
