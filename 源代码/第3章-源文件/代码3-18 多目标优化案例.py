import gurobipy as grb
import numpy as np

# 设定工人数和工作数量
N = 10
np.random.seed(1234)  # 固定随机数种子，这样每次产生的随机数一样

# 用随机数初始化时间矩阵Tij和成本矩阵Cij
# i+1, j+1 是为了序号从1开始编号
Tij = {(i + 1, j + 1): np.random.randint(0, 100) for i in range(N) for j in range(N)}
Cij = {(i + 1, j + 1): np.random.randint(0, 100) for i in range(N) for j in range(N)}

# 定义 model
m = grb.Model('MultiObj')

# 添加变量，x是tupledict类型，可以方便使用select,sum,prod函数
# 同时可以加快创建变量的效率
# x 是0-1类型变量，xij=1 表示第i个工人被分配到第j个工作中
x = m.addVars(Tij.keys(), vtype=grb.GRB.BINARY, name='x')

# 添加约束
# tupledict的sum函数使用
# 第一个约束表示一个工作只能分配给一个工人
# 第二个约束表示一个工人只做一个工作
m.addConstrs((x.sum('*', j + 1) == 1 for j in range(N)), 'C1')
m.addConstrs((x.sum(i + 1, '*') == 1 for i in range(N)), 'C2')

# 多目标方式1：Blend合成型
# 设置多目标 权重
# x.prod(Tij)表示工人分配矩阵Xij和时间矩阵Tij通过相同的索引ij进行相乘
# 这也是Gurobi扩展tupledict的原因
# 第二个目标函数取符号是为了保证两个目标的优化方向一致
# m.setObjectiveN(x.prod(Tij),  index=0, weight=0.1, name='obj1')
# m.setObjectiveN(-x.prod(Cij), index=1, weight=0.5, name='obj2')

# 多目标方式2：Hierarchical分层型
m.setObjectiveN(x.prod(Tij), index=0, priority=1, abstol=0, reltol=0, name='obj1')
m.setObjectiveN(-x.prod(Cij), index=1, priority=2, abstol=100, reltol=0, name='obj2')

# 启动求解
m.optimize()

# 获得求解结果
# x[i].x 表示获取某个变量的值
for i in Tij.keys():
    if x[i].x > 0.9:
        print("工人 %d 分配工作 %d" % (i[0], i[1]))

# 获取目标函数值
for i in range(2):
    m.setParam(grb.GRB.Param.ObjNumber, i)
    print('Obj%d = ' % (i + 1), m.ObjNVal)

# 输出结果
# Obj1 =  373.0
# Obj2 =  -768.0

# 工人 1 分配工作 8
# 工人 2 分配工作 10
# 工人 3 分配工作 9
# 工人 4 分配工作 3
# 工人 5 分配工作 2
# 工人 6 分配工作 4
# 工人 7 分配工作 5
# 工人 8 分配工作 7
# 工人 9 分配工作 1
# 工人 10 分配工作 6
