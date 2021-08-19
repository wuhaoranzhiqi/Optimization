import gurobipy as grb

# 创建tuplelist对象
tl = grb.tuplelist([(1, 2), (1, 3), (2, 3), (2, 5)])

# 取出第一个值是1的元素
print(tl.select(1, '*'))
# 输出
# <gurobi.tuplelist (2 tuples, 2 values each):
#  ( 1 , 2 )
#  ( 1 , 3 )

# 取出第二个值是3的元素
print(tl.select('*', 3))
# 输出
# <gurobi.tuplelist (2 tuples, 2 values each):
#  ( 1 , 3 )
#  ( 2 , 3 )

# -----------------------------------------------------------------------
# 添加一个元素
tl.append((3, 5))
print(tl.select(3, '*'))
# 输出 <gurobi.tuplelist (1 tuples, 2 values each):
#  ( 3 , 5 )

# 使用迭代的方式实现select功能
print(tl.select(1, '*'))
# 输出 <gurobi.tuplelist (2 tuples, 2 values each):
#  ( 1 , 2 )
#  ( 1 , 3 )

# 对应的迭代语法是这样的
print([(x, y) for x, y in tl if x == 1])
