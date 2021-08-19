import gurobipy as grb
model = grb.Model()

# 添加lazy cut
def mycallback(model, where):
    if where == grb.GRB.Callback.MIPSOL:
        sol = model.cbGetSolution([model._vars[0], model._vars[1]])
        if sol[0] + sol[1] > 1.1:
            model.cbLazy(model._vars[0] + model._vars[1] <= 1)

model._vars = model.getVars()
model.Params.lazyConstraints = 1
model.optimize(mycallback)
