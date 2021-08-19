import numpy as np

# 创建一个二维数组
a = np.array([[1,2,3],
              [4,5,6]])

print('数组的维度是：', a.shape)  # 输出 (2, 3)

# 创建全是0或1的二维数组
a_one = np.ones((2,3))
print('创建全是1的数组：\n', a_one)
# 创建全是1的数组：
#  [[1. 1. 1.]
#  [1. 1. 1.]]

a_zero = np.zeros((2,3))
print('创建全是0的数组：\n', a_zero)
# 创建全是0的数组：
#  [[0. 0. 0.]
#  [0. 0. 0.]]

