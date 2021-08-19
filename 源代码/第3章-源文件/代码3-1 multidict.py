import gurobipy as grb

# mutidict 用法
student, chinese, math, english = grb.multidict({
    'student1': [1, 2, 3],
    'student2': [2, 3, 4],
    'student3': [3, 4, 5],
    'student4': [4, 5, 6]
})

print(student)  # 字典的键
# 输出
# ['student1', 'student2', 'student3', 'student4']

print(chinese)  # 语文成绩的字典
# 输出
# {'student1': 1, 'student2': 2, 'student3': 3, 'student4': 4}

print(math)  # 数学成绩的字典
# 输出
# {'student1': 2, 'student2': 3, 'student3': 4, 'student4': 5}

print(english)  # 英语成绩的字典
# 输出
# {'student1': 3, 'student2': 4, 'student3': 5, 'student4': 6}
