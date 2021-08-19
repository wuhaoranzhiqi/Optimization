# python 字典：dict
da = {'a': 123, 'b': 456, 'c': 789}  # 创建一个简单的字典，由3个映射构成
db = {'a': [1,2,3], 'b': [4,5,6]}    # 这是一个复杂的字典，值是list结构

print('字典da的映射数量：', len(da))        # 输出3
print('字典da，key=b的映射值为：', da.get('b'))  # 输出456
print('键d是否存在字典da的键集合中：', 'd' in da)    # 输出False（假）

# 查看所有映射关系
for key, value in da.items():
    print(key, '=' , value)
# a = 123
# b = 456
# c = 789

# 添加或删除映射关系
da['d'] = 10    # 添加
da.pop('a')     # 删除
print(da)
# 输出 {'b': 456, 'c': 789, 'd': 10}
