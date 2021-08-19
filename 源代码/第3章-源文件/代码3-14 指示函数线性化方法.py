import gurobipy as grb

model = grb.Model()
x = model.addVar(name='x')
y = model.addVar(name='y')
model.addConstr((y == 1) >> (x > 0), name='indicator')
