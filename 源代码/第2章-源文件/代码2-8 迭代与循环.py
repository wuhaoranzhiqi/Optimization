# 集合迭代
a = [1, 2, 3, 4, 5]

def my_func(x):
    print('do some on ', x)
    return x + 1

# 迭代版本
b = [my_func(x) for x in a]
print(b)  # 输出 [2, 3, 4, 5, 6]

# 循环版本
b2 = []
for x in a:
    t = x + 1
    b2.append(t)
print(b2)  # 同样输出 [2, 3, 4, 5, 6]
