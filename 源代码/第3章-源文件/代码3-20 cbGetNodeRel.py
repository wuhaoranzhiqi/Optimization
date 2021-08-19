import gurobipy as grb
model = grb.Model()

# 查询变量在当前节点的松弛解
def mycallback(model, where):
    if where == grb.GRB.Callback.MIPNODE and \
            model.cbGet(grb.GRB.Callback.MIPNODE_STATUS) == grb.GRB.OPTIMAL:
        print(model.cbGetNodeRel(model._vars))

model._vars = model.getVars()
model.optimize(mycallback)
