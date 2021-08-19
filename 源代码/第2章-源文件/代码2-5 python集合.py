# python 集合：set
sa = set(['a','b','c','d'])
sb = set(['b','c','f'])

print('元素a是否在集合sa中：', 'a' in sa)  # 输出True

print('交集：', sa & sb)   # 输出  {'c', 'b'}
print('并集：', sa | sb)   # 输出  {'c', 'd', 'b', 'a', 'f'}
print('差集：在sa中而不在sb中的元素：', sa - sb)  # 输出 {'a', 'd'}
print('不同时包含在sa和sb中的元素：', sa ^ sb)  # 输出 {'d', 'a', 'f'}
