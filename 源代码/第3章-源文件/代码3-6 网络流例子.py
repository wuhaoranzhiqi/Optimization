import gurobipy as grb

# 两种商品
commodities = ['Pencils', 'Pens']
# 2个产地+3个目的地
nodes = ['Detroit', 'Denver', 'Boston', 'New York', 'Seattle']

# 网络中每条弧的容量，使用multidict一次性创建多个字典
arcs, capacity = grb.multidict({
    ('Detroit', 'Boston'): 100,
    ('Detroit', 'New York'): 80,
    ('Detroit', 'Seattle'): 120,
    ('Denver', 'Boston'): 120,
    ('Denver', 'New York'): 120,
    ('Denver', 'Seattle'): 120})

# 商品在不同弧上的运输成本，是tupledict形式，可以用select，sum等加快变量选取
cost = {
    ('Pencils', 'Detroit', 'Boston'): 10,
    ('Pencils', 'Detroit', 'New York'): 20,
    ('Pencils', 'Detroit', 'Seattle'): 60,
    ('Pencils', 'Denver', 'Boston'): 40,
    ('Pencils', 'Denver', 'New York'): 40,
    ('Pencils', 'Denver', 'Seattle'): 30,
    ('Pens', 'Detroit', 'Boston'): 20,
    ('Pens', 'Detroit', 'New York'): 20,
    ('Pens', 'Detroit', 'Seattle'): 80,
    ('Pens', 'Denver', 'Boston'): 60,
    ('Pens', 'Denver', 'New York'): 70,
    ('Pens', 'Denver', 'Seattle'): 30}

# 商品在不同节点的流入流出，即需求量
# 正数表示产地，负数表示需求量
# 是tupledict形式，可以用select，sum等加快变量选取
inflow = {
    ('Pencils', 'Detroit'): 50,
    ('Pencils', 'Denver'): 60,
    ('Pencils', 'Boston'): -50,
    ('Pencils', 'New York'): -50,
    ('Pencils', 'Seattle'): -10,
    ('Pens', 'Detroit'): 60,
    ('Pens', 'Denver'): 40,
    ('Pens', 'Boston'): -40,
    ('Pens', 'New York'): -30,
    ('Pens', 'Seattle'): -30}

# 创建模型
m = grb.Model('netflow')

# 创建变量
# flow是tupledict类型的变量，因此可以使用select方法快速筛选
# 键是 ('Pencils', 'Detroit', 'Boston') 格式，可以使用select方法快速筛选，然后出选出来的变量sum求和
# 值是 cost，表示商品从产地到目的地的需求量
# 值还有系数，就是cost
flow = m.addVars(commodities, arcs, obj=cost, name="flow")

# 添加容量约束，使用到了迭代表达式
# 此处迭代中，i是产地，j是目的地
# capacity[i,j] 表示i->j的弧的容量
# flow.sum('*',i,j) 从i->j的所有不同商品的总量求和
m.addConstrs((flow.sum('*', i, j) <= capacity[i, j] for i, j in arcs), "cap")

# 添加节点的流入=流出的约束
# h表示商品， j表示节点包括产地和目的地
# flow.sum(h,'*',j) 表示商品h经过所有所有中间节点到达j后的总数量
# flow.sum(h,j,'*') 表示商品h从j节点流出去的数量
# inflow[h,j] 表示h在j节点的需求量
# 理解起来就是：
# 商品h在节点j，流入-流出 = 需求
# 流出可以表示产地，也可以表示中转节点
m.addConstrs((flow.sum(h, '*', j) + inflow[h, j] == flow.sum(h, j, '*') for h in commodities for j in nodes), "node")

# 求解模型
m.optimize()

# 打印结果
if m.status == grb.GRB.Status.OPTIMAL:
    solution = m.getAttr('x', flow)
    for h in commodities:
        print('\nOptimal flows for %s:' % h)
        for i, j in arcs:
            if solution[h, i, j] > 0:
                print('%s -> %s: %g' % (i, j, solution[h, i, j]))
# 求解结果如下：
# Optimal flows for Pencils:
#     Detroit -> Boston: 50
#     Denver -> New York: 50
#     Denver -> Seattle: 10
#
# Optimal flows for Pens:
#     Detroit -> Boston: 30
#     Detroit -> New York: 30
#     Denver -> Boston: 10
#     Denver -> Seattle: 30
