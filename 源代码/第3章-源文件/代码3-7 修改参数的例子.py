import gurobipy as grb

# 读取模型文件
model_file = 'xxx.lp'
m = grb.read(model_file)

# 参数设定1：设定优化器求解时间限定为2秒
m.Params.timeLimit = 2

# 复制模型
bestModel = m.copy()
bestModel.optimize()

# 修改模型参数比较不同参数下的求解结果
for i in range(1, 4):
    m.reset()  # 将所有参数重置为默认值
    m.Params.MIPFocus = i  # 参数设定2：修改 MIPFocus 参数
    m.optimize()
    if bestModel.MIPGap > m.MIPGap:
        bestModel, m = m, bestModel  # swap models

# 最后将运行参数修改为默认值，重新运行模型
del m
bestModel.Params.timeLimit = "default"
bestModel.optimize()
print('Solved with MIPFocus: %d' % bestModel.Params.MIPFocus)
