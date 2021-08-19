import pandas as pd
import numpy as np

# 前后两阶段节点距离，使用dataframe存储
# A->B 的距离
df1 = pd.DataFrame(np.array([[10, 20]]), index=["A"], columns=['B1', 'B2'])
# B->C 的距离
df2 = pd.DataFrame(np.array([[30, 10], [5, 20]]), index=['B1', 'B2'], columns=['C1', 'C2'])
# C->D 的距离
df3 = pd.DataFrame(np.array([[20], [10]]), index=['C1', 'C2'], columns=['D'])


def dp(df_from, df_to):
    """从 df_from 阶段到 df_to 阶段的动态规划求解"""
    from_node = df_to.index
    f = pd.Series()
    g = []
    for j in from_node:
        m1 = df_to.loc[j]  # 例如取B1
        m2 = m1 + df_from  # 则t=[C1, C2]
        m3 = m2.sort_values()
        f[j] = m3[0]  # B1->C 取路径最短的
        g.append(m3.index[0])
    dc = pd.DataFrame()
    dc['v'] = f.values
    dc['n'] = g
    dc.index = f.index
    cv.append(dc)
    if len(start) > 0:
        df = start.pop()
        t = dp(dc['v'], df)  # 这里使用了递归
    else:
        return dc

# 主函数
start = [df1]  # 初始状态
cv = []  # 存储路径
t1 = df3['D']  # 初始状态
h1 = dp(df3['D'], df2)

# 打印路径
for m in range(len(cv)):
    xc = cv.pop()
    x1 = xc.sort_values(by='v')
    print(x1['n'].values[0], end='->')
# 所以最短路径是：
# A->B->C->D
