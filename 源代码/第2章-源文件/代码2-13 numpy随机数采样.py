from numpy import random

random.seed(1234)

# 有放回随机采样
samples = [1, 2, 3, 4, 5, 6, 7, 8, 9]
random.choice(samples, size=5, replace=True)
# 输出 array([4, 3, 4, 2, 4])

# 无放回随机采样
random.choice(samples, size=5, replace=False)
# 输出 array([9, 1, 6, 8, 3])

# 打乱样本的顺序，以产生随机数的效果
samples = [1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(samples)
print(samples)
# 输出 [4, 3, 9, 7, 1, 5, 6, 8, 2]
