def dp(weight, count, weights, costs):
    """动态规划求解01背包问题"""
    preline, curline = [0] * (weight + 1), [0] * (weight + 1)
    for i in range(count):
        for j in range(weight + 1):
            if weights[i] <= j:
                curline[j] = max(preline[j], costs[i] + preline[j - weights[i]])
        preline = curline[:]
    return curline[weight]

# 求解
count = 5   # 物品数量
weight = 10 # 背包总重量
costs = [6, 3, 5, 4, 6] # 每件物品的价值
weights = [2, 2, 6, 5, 4]   # 每件物品的重量
print(dp(weight, count, weights, costs))
# 输出 15
