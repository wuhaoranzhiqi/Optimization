import gurobipy as grb
model = grb.Model()

# 从当前节点导入解
def mycallback(model, where):
    if where == grb.GRB.Callback.MIPNODE:
        model.cbSetSolution(vars, newsolution)


model.optimize(mycallback)
