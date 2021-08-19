import numpy as np

# 邻接矩阵
M = 99999
graph = np.array([
    [0, 1, 3, M, M, M],
    [1, 0, 2, 8, M, M],
    [3, 2, 0, 7, 3, M],
    [M, 8, 7, 0, 5, 6],
    [M, M, 3, 5, 0, 6],
    [M, M, M, 6, 6, 0]])

# 邻接矩阵转边集数组
edge_list = []
for i in range(graph.shape[0]):
    for j in range(graph.shape[0]):
        if graph[i][j] < M:
            edge_list.append([i, j, graph[i][j]])
edge_list.sort(key=lambda a: a[2])

# 最小生成树
group = [[i] for i in range(graph.shape[0])]
res = []
for edge in edge_list:
    for i in range(len(group)):
        if edge[0] in group[i]:
            m = i
        if edge[1] in group[i]:
            n = i
    if m != n:
        res.append(edge)
        group[m] = group[m] + group[n]
        group[n] = []

print("最小生成树是：", res)
# 最小生成树是： [[0, 1, 1], [1, 2, 2], [2, 4, 3], [3, 4, 5], [3, 5, 6]]
