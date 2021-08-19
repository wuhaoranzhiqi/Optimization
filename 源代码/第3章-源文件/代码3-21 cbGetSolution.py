import gurobipy as grb
model = grb.Model()

# 在MIP问题中查询变量在新可行解中的值
def mycallback(model, where):
    if where == grb.GRB.Callback.MIPSOL:
        print(model.cbGetSolution(model._vars))

model._vars = model.getVars()
model.optimize(mycallback)
