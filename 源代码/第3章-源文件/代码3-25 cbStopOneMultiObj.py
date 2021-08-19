import gurobipy as grb
model = grb.Model()

# 停止多目标优化过程
import time

def mycallback(model, where):
    if where == grb.GRB.Callback.MULTIOBJ:
        # 获取当前目标函数值
        model._objcnt = model.cbGet(grb.GRB.Callback.MULTIOBJ_OBJCNT)
        # 重置开始计时时间
        model._starttime = time.time()
    # 判断是否退出搜索
    elif time.time() - model._starttime > BIG or solution is good_enough:
        # 停止搜索
        model.cbStopOneMultiObj(model._objcnt)


model._objcnt = 0
model._starttime = time.time()
model.optimize(mycallback)
