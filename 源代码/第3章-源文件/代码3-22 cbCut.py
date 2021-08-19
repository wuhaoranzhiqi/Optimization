import gurobipy as grb
model = grb.Model()

# 在求解MIP问题时在节点添加割平面
def mycallback(model, where):
    if where == grb.GRB.Callback.MIPNODE:
        status = model.cbGet(grb.GRB.Callback.MIPNODE_STATUS)
        if status == grb.GRB.OPTIMAL:
            rel = model.cbGetNodeRel([model._vars[0], model._vars[1]])
            if rel[0] + rel[1] > 1.1:
                model.cbCut(model._vars[0] + model._vars[1] <= 1)

model._vars = model.getVars()
model.Params.PreCrush = 1
model.optimize(mycallback)
