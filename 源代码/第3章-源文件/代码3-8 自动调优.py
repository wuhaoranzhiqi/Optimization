import gurobipy as grb

# 读取模型
model = grb.read('tune_model.lp')

# 将返回最优参数组合数设置为1
model.Params.tuneResults = 1

# 开始自动调参
model.tune()

# 如果找到最优参数组合数大于0
if model.tuneResultCount > 0:
    # 获取最优参数组合
    # 注意到getTuneResult会覆盖内部默认属性
    # 参数组合按最优到最差降序排序，最好的结果序号是0
    model.getTuneResult(0)
    # 将调参后的参数组合保存到文件
    model.write('tune.prm')
    # 用获取到的最优参数组合再次求解模型
    model.optimize()
