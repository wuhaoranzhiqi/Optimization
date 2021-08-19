# 为了方便编程，添加虚拟节点 0->1 和虚拟终点 6->7
import gurobipy as grb

# 定义网络
flow = {(0, 1): 99999, (1, 2): 70, (1, 3): 100, (1, 4): 90, (2, 6): 80,
        (3, 4): 40, (3, 5): 70, (4, 5): 40, (4, 6): 100, (5, 6): 90, (6, 7): 99999
        }
# 创建模型
arch, maxflow = grb.multidict(flow)
m = grb.Model("maxflow")
X = m.addVars(arch, name='X')

# 添加约束
for i, j in arch:
    # 对任意网络流不能超过最大流量
    m.addConstr(X[i, j] <= maxflow[i, j])
    if i == 0 or j == 7:
        continue
    else:
        m.addConstr(X.sum(i, '*') == X.sum('*', i))

# 添加目标函数
m.setObjective(X.sum(1, '*'), sense=grb.GRB.MAXIMIZE)
# 求解
m.optimize()
print("目标函数值：", m.objVal)
for i, j in arch:
    print("%d->%d: %d" % (i, j, X[i, j].x))
# 目标函数值： 260.0
# 0->1: 260
# 1->2: 70
# 1->3: 100
# 1->4: 90
# 2->6: 70
# 3->4: 40
# 3->5: 60
# 4->5: 30
# 4->6: 100
# 5->6: 90
