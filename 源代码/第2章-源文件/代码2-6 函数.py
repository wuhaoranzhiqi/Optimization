def find_max(a, b, c):
    """
    定义一个函数 find_max, 实现的功能是找到 a, b, c 中的最大值。
    该函数需要输入三个参数，分别是：a,b,c，返回值是三个参数的最大值。
    """
    max_number = None
    if a > b and a > c:
        max_number = a
    elif b > a and b > c:
        max_number = b
    elif c > a and c > b:
        max_number = c
    return max_number


# 使用刚才定义的函数
max_num = find_max(a=1, b=2, c=3)
print('最大的数是：', max_num)
# 输出3

# python内部已经实现了该函数，我们可以直接调用
print('最大的数是：', max([1, 2, 3]))
# 输出3
