import gurobipy as grb
model = grb.Model()
# 查询查询当前单纯形的目标函数值
def mycallback(model, where):
    if where == grb.GRB.Callback.SIMPLEX:
        print(model.cbGet(grb.GRB.Callback.SPX_OBJVAL))

model.optimize(mycallback)
