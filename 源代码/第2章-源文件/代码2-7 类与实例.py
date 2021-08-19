# 定义一个类
class cat():
    def __init__(self, color, weight):
        self.color = color
        self.weight = weight

    def catch_mice(self):
        """抓老鼠的方法"""
        print('抓老鼠')

    def eat_mice(self):
        """吃老鼠"""
        print('吃老鼠')


# 类的实例化
my_cat = cat('yello', 10)

# 调用类的方法
my_cat.catch_mice()
# 输出 抓老鼠

my_cat.eat_mice()
# 输出 吃老鼠

# 查看类的属性
print(my_cat.color)
# 输出 yello

print(my_cat.weight)
# 输出 10
