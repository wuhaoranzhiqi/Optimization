import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns

sns.set_style("whitegrid")
mpl.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

# 固定随机数种子
np.random.seed(1234)

# 一些参数
city_num = 10  # 城市的数量
size = 50  # 种群大小，即粒子的个数
r1 = 0.7  # pbest-xi 的保留概率
r2 = 0.8  # gbest-xi 的保留概率
iter_num = 1000  # 算法最大迭代次数
fitneess_value_list = []  # 每一步迭代的最优解

# 随机生成city_num个城市的坐标，注意是不放回抽样
X = np.random.choice(list(range(1, 100)), size=city_num, replace=False)
Y = np.random.choice(list(range(1, 100)), size=city_num, replace=False)

# 计算城市之间的距离
def calculate_distance(X, Y):
    """
    计算城市两辆之间的欧式距离，结果用numpy矩阵存储
    :param X: 城市的X坐标，np.array数组
    :param Y: 城市的Y坐标，np.array数组
    """
    distance_matrix = np.zeros((city_num, city_num))
    for i in range(city_num):
        for j in range(city_num):
            if i == j:
                continue
            dis = np.sqrt((X[i] - X[j]) ** 2 + (Y[i] - Y[j]) ** 2)  # 欧式距离计算
            distance_matrix[i][j] = dis
    return distance_matrix

def fitness_func(distance_matrix, xi):
    """
    适应度函数，计算目标函数值.
    :param distance: 城市的距离矩阵
    :param xi: PSO的一个解
    :return: 目标函数值，即总距离
    """
    total_distance = 0
    for i in range(1, city_num):
        start = xi[i - 1]
        end = xi[i]
        total_distance += distance_matrix[start][end]
    total_distance += distance_matrix[end][xi[0]]  # 从最后一个城市回到出发城市
    return total_distance

def plot_tsp(gbest):
    """绘制最优解的图形"""
    plt.scatter(X, Y, color='r')
    for i in range(1, city_num):
        start_x, start_y = X[gbest[i - 1]], Y[gbest[i - 1]]
        end_x, end_y = X[gbest[i]], Y[gbest[i]]
        plt.plot([start_x, end_x], [start_y, end_y], color='b', alpha=0.8)
    start_x, start_y = X[gbest[0]], Y[gbest[0]]
    plt.plot([start_x, end_x], [start_y, end_y], color='b', alpha=0.8)

def get_ss(xbest, xi, r):
    """
    计算交换序列，即 x2 经过交换序列ss得到x1，对应PSO速度更新公式的：
    r1(pbest-xi) 和 r2(gbest-xi)
    :param xbest: pbest 或者 gbest
    :param xi: 例子当前解
    :return:
    """
    velocity_ss = []
    for i in range(len(xi)):
        if xi[i] != xbest[i]:
            j = np.where(xi == xbest[i])[0][0]
            so = (i, j, r)  # 得到交换子
            velocity_ss.append(so)
            xi[i], xi[j] = xi[j], xi[i]  # 执行交换操作
    return velocity_ss

def do_ss(xi, ss):
    """
    执行交换操作
    :param xi:
    :param ss: 由交换子组成的交换序列
    :return:
    """
    for i, j, r in ss:
        rand = np.random.random()
        if rand <= r:
            xi[i], xi[j] = xi[j], xi[i]
    return xi

# 计算城市之间的距离矩阵
distance_matrix = calculate_distance(X, Y)

# 初始化种群的各个粒子的位置，作为个体的历史最优解pbest
# 用一个 50*10 的矩阵表示种群，每行表示一个粒子, 每一行是0-9不重复随机数，表示城市访问的顺序
XX = np.zeros((size, city_num), dtype=np.int)
for i in range(size):
    XX[i] = np.random.choice(list(range(city_num)), size=city_num, replace=False)

# 计算每个粒子对应适应度
pbest = XX
pbest_fitness = np.zeros((size, 1))
for i in range(size):
    pbest_fitness[i] = fitness_func(distance_matrix, xi=XX[i])

# 计算全局适应度和对应的解gbest
gbest = XX[pbest_fitness.argmin()]
gbest_fitness = pbest_fitness.min()

# 记录算法迭代效果
fitneess_value_list.append(gbest_fitness)

# 下面开始迭代
for i in range(iter_num):
    for j in range(size):  # 对每个粒子迭代
        pbesti = pbest[j].copy()  # 此处要用copy，不然出现浅拷贝问题
        xi = XX[j].copy()
        # 计算交换序列，即 v = r1(pbest-xi) + r2(gbest-xi)
        ss1 = get_ss(pbesti, xi, r1)
        ss2 = get_ss(gbest, xi, r2)
        ss = ss1 + ss2
        # 执行交换操作，即 x = x + v
        xi = do_ss(xi, ss)
        # 判断是否更优
        fitness_new = fitness_func(distance_matrix, xi)
        fitness_old = pbest_fitness[j]
        if fitness_new < fitness_old:
            pbest_fitness[j] = fitness_new
            pbest[j] = xi
    # 判断全局是否更优
    gbest_fitness_new = pbest_fitness.min()
    gbest_new = pbest[pbest_fitness.argmin()]
    if gbest_fitness_new < gbest_fitness:
        gbest_fitness = gbest_fitness_new
        gbest = gbest_new
    # 加入到列表
    fitneess_value_list.append(gbest_fitness)

# 打印迭代的结果
print('迭代最优结果是：', gbest_fitness)
print('迭代最优变量是：', gbest)
# 迭代最优结果是： 230.344
# 迭代最优变量是： [5 8 2 3 6 1 7 0 4 9]

# 绘制TSP路径图
plot_tsp(gbest)
plt.title('TSP路径规划结果')
