import math
import networkx
import gurobipy as grb

def vrp(V, c, m, q, Q):
    """
    求解VRP问题
    :param V: 节点的列表
    :param c: c[i,j] 表示i->j的距离
    :param m: 车辆数量
    :param q: q[i] 表示客户i的需求量
    :param Q: 车辆的容量
    :return:
    """

    def vrp_callback(model, where):
        # 添加约束以消除不可行的解决方案
        if where != grb.GRB.callback.MIPSOL:
            return
        edges = []
        for (i, j) in x:
            if model.cbGetSolution(x[i, j]) > 0.5:
                if i != V[0] and j != V[0]:
                    edges.append((i, j))
        G = networkx.Graph()
        G.add_edges_from(edges)
        Components = networkx.connected_components(G)
        for S in Components:
            S_card = len(S)
            q_sum = sum(q[i] for i in S)
            NS = int(math.ceil(float(q_sum) / Q))
            S_edges = [(i, j) for i in S for j in S if i < j and (i, j) in edges]
            if S_card >= 3 and (len(S_edges) >= S_card or NS > 1):
                model.cbLazy(grb.quicksum(x[i, j] for i in S for j in S if j > i) <= S_card - NS)
                print("adding cut for", S_edges)
        return

    model = grb.Model("vrp")
    x = {}
    for i in V:
        for j in V:
            if j > i and i == V[0]:  # depot
                x[i, j] = model.addVar(ub=2, vtype="I", name="x(%s,%s)" % (i, j))
            elif j > i:
                x[i, j] = model.addVar(ub=1, vtype="I", name="x(%s,%s)" % (i, j))
    model.update()

    model.addConstr(grb.quicksum(x[V[0], j] for j in V[1:]) == 2 * m, "DegreeDepot")
    for i in V[1:]:
        model.addConstr(grb.quicksum(x[j, i] for j in V if j < i) +
                        grb.quicksum(x[i, j] for j in V if j > i) == 2, "Degree(%s)" % i)

    model.setObjective(grb.quicksum(c[i][j] * x[i, j] for i in V for j in V if j > i), grb.GRB.MINIMIZE)

    model.update()
    model.__data = x
    return model, vrp_callback

def make_data():
    """生成数据"""
    # 节点的编号
    V = range(17)
    # 每个节点的需求量，0表示起始节点没有需求
    q = [0, 1, 1, 2, 4, 2, 4, 8, 8, 1, 2, 1, 2, 4, 4, 8, 8]
    # 车辆的数量m以及每辆车的容量Q
    m = 4
    Q = 15
    c = [
    [0, 548, 776, 696, 582, 274, 502, 194, 308, 194, 536, 502, 388, 354, 468, 776, 662],
    [548, 0, 684, 308, 194, 502, 730, 354, 696, 742, 1084, 594, 480, 674, 1016, 868, 1210],
    [776, 684, 0, 992, 878, 502, 274, 810, 468, 742, 400, 1278, 1164, 1130, 788, 1552, 754],
    [696, 308, 992, 0, 114, 650, 878, 502, 844, 890, 1232, 514, 628, 822, 1164, 560, 1358],
    [582, 194, 878, 114, 0, 536, 764, 388, 730, 776, 1118, 400, 514, 708, 1050, 674, 1244],
    [274, 502, 502, 650, 536, 0, 228, 308, 194, 240, 582, 776, 662, 628, 514, 1050, 708],
    [502, 730, 274, 878, 764, 228, 0, 536, 194, 468, 354, 1004, 890, 856, 514, 1278, 480],
    [194, 354, 810, 502, 388, 308, 536, 0, 342, 388, 730, 468, 354, 320, 662, 742, 856],
    [308, 696, 468, 844, 730, 194, 194, 342, 0, 274, 388, 810, 696, 662, 320, 1084, 514],
    [194, 742, 742, 890, 776, 240, 468, 388, 274, 0, 342, 536, 422, 388, 274, 810, 468],
    [536, 1084, 400, 1232, 1118, 582, 354, 730, 388, 342, 0, 878, 764, 730, 388, 1152, 354],
    [502, 594, 1278, 514, 400, 776, 1004, 468, 810, 536, 878, 0, 114, 308, 650, 274, 844],
    [388, 480, 1164, 628, 514, 662, 890, 354, 696, 422, 764, 114, 0, 194, 536, 388, 730],
    [354, 674, 1130, 822, 708, 628, 856, 320, 662, 388, 730, 308, 194, 0, 342, 422, 536],
    [468, 1016, 788, 1164, 1050, 514, 514, 662, 320, 274, 388, 650, 536, 342, 0, 764, 194],
    [776, 868, 1552, 560, 674, 1050, 1278, 742, 1084, 810, 1152, 274, 388, 422, 764, 0, 798],
    [662, 1210, 754, 1358, 1244, 708, 480, 856, 514, 468, 354, 844, 730, 536, 194, 798, 0]]
    return V, c, q, m, Q

def main():
    V, c, q, m, Q = make_data()
    model, vrp_callback = vrp(V, c, m, q, Q)

    model.params.DualReductions = 0
    model.params.LazyConstraints = 1
    model.optimize(vrp_callback)
    x = model.__data

    edges = []
    for (i, j) in x:
        if x[i, j].X > .5:
            if i != V[0] and j != V[0]:
                edges.append((i, j))

    print("最优解是:", model.ObjVal)
    print("最优路径是:")
    print(sorted(edges))
    # [(1, 4), (1, 7), (2, 6), (2, 8), (3, 4), (5, 6), (9, 14), (10, 16), (11, 12), (11, 15), (13, 15), (14, 16)]
