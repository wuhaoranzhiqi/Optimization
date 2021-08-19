from ortools.graph import pywrapgraph

# 定义从 start->end 的弧的容量
# 即 start_node[i] -> end_node[i] = capacities[i]
start_nodes = [1, 1, 1, 2, 4, 4, 3, 3, 5]
end_nodes = [2, 4, 3, 6, 6, 5, 4, 5, 6]
capacities = [70, 90, 100, 80, 100, 40, 40, 70, 90]
# 创建简单流
max_flow = pywrapgraph.SimpleMaxFlow()
# 添加节点和弧的约束
for i in range(len(start_nodes)):
    max_flow.AddArcWithCapacity(start_nodes[i], end_nodes[i], capacities[i])

# 求解 1->6 的最大流
if max_flow.Solve(1, 6) == max_flow.OPTIMAL:
    print('最大流是：', max_flow.OptimalFlow())
    print('   边    流量 / 边的最大流量')
    for i in range(max_flow.NumArcs()):
        print('%1s -> %1s   %3s  / %3s' % (
            max_flow.Tail(i),
            max_flow.Head(i),
            max_flow.Flow(i),
            max_flow.Capacity(i)))

# 结果如下：
# 最大流是： 260
#    边    流量 / 边的最大流量
# 1 -> 2    70  /  70
# 1 -> 4    90  /  90
# 1 -> 3   100  / 100
# 2 -> 6    70  /  80
# 4 -> 6   100  / 100
# 4 -> 5    30  /  40
# 3 -> 4    40  /  40
# 3 -> 5    60  /  70
# 5 -> 6    90  /  90
