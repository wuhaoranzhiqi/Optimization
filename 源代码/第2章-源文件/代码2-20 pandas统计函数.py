import pandas as pd

df = pd.DataFrame(data=[
    ['x1', '张三', 177, 92, 1.5, '2019/3/23'],
    ['x2', '李四', 151, 84, 2.3, '2019/3/24'],
    ['x3', '王五', 167, 80, 3.2, '2019/3/25'],
    ['x4', '韩六', 175, 77, 1.2, '2019/3/26'],
    ['x5', '赵七', 153, 87, 1.8, '2019/3/27']
],
    columns=['学号', '姓名', '身高', '语文成绩', '学分', '日期']
)

# 查看dataframe的维度
print('dataframe的维度是：', df.shape)
# 输出 (5, 6)

# 从dataframe中拆出一个series
# 即dataframe中的一列就是一个series
high = df['身高']
print(high)
# 输出
# 0    177
# 1    151
# 2    167
# 3    175
# 4    153
# Name: 身高, dtype: int64

# 最大值最小值
df['身高'].max()  # 输出 177
df['身高'].min()  # 输出 151

# 均值和标准差
df['身高'].mean()  # 输出 164.6
df['身高'].std()   # 输出 12.1161

# 分位数：90% 的分位数
df['身高'].quantile(q=0.9)  # 输出 176.2

# 累计值
df['身高'].cumsum()
# 输出
# 0    177
# 1    328
# 2    495
# 3    670
# 4    823
# Name: 身高, dtype: int64

# 相关系数
df[['身高', '语文成绩']].corr(method='pearson')
# 输出
#             身高      语文成绩
# 身高    1.000000    -0.063232
# 语文成绩 -0.063232  1.000000

# 协方差
df[['身高', '语文成绩']].cov()
# 输出
#          身高  语文成绩
# 身高    146.8   -4.5
# 语文成绩   -4.5  34.5
