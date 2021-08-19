# 线性代数
import numpy as np

A = np.array([
    [1, -2, 1],
    [0, 2, -8],
    [-4, 5, 9]
])
B = np.array([0, -8, 9])

result = np.linalg.solve(A, B)
print('x=', result[0])
print('y=', result[1])
print('z=', result[2])
# 输出
# x= -29.0  y= -16.0  z= -3.0
