import numpy as np

# 地图
# 1：起点，3：终点，0：可通行，2：障碍物
map = np.array([[0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 2, 0, 0, 0],
                [0, 0, 0, 2, 0, 0, 0],
                [0, 0, 0, 2, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0]])

# 设置起点和终点的坐标
start_point = (2, 1)
end_point = (2, 5)
map[start_point] = 1
map[end_point] = 3

# 已遍历和待遍历列表
global openList
global closeList
openList = []
closeList = []

# 使用类来描述节点，可以存储更多信息
class Node:
    # 描述 a* 算法中的节点数据，包含坐标，父节点，g和h值
    def __init__(self, point, g=0):
        self.point = point  # 自己的坐标
        self.father = None  # 父节点
        self.g = g  # g值，g值在用到的时候会重新算
        self.h = (abs(end_point[0] - point[0]) + abs(end_point[1] - point[1])) * 10  # 计算h值

def get_minF_node():
    """ 获得openlist中F值最小的节点 """
    global openList
    currentNode = openList[0]
    for node in openList:
        if node.g + node.h < currentNode.g + currentNode.h:
            currentNode = node
    return currentNode

def point_in_closeList(point):
    """判断节点是否在clost_list中"""
    global closeList
    for node in closeList:
        if node.point == point:
            return True
    return False

def point_in_openList(point):
    """根据坐标判断节点是否在open_list中，在就取出给节点"""
    global openList
    for node in openList:
        if node.point == point:
            return node
    return None

def end_point_in_closeList():
    """结束判断，终点是否在openList中，有就返回终点"""
    global openList
    for node in openList:
        if node.point == end_point:
            return node
    return None

def is_validate_point(point):
    """判断节点是否越界，以及是否障碍物"""
    if point[0] < 0 or point[0] >= map.shape[0]-1 or point[1]< 0 or point[1] >= map.shape[1] - 1:
        return False
    elif map[point] == 2:
        return False
    else:
        return True

def search_near(minF, offsetX, offsetY):
    """
    搜索节点周围的点
    :param minF:F值最小的节点
    :param offsetX: 坐标偏移量，即上下左右对角移动
    :param offsetY:
    """
    global openList
    new_point = (minF.point[0] + offsetX, minF.point[1] + offsetY)
    # 判断周围的点是否可行
    if not is_validate_point(new_point):
        return
    # 如果在关闭表中，就忽略
    currentPoint = (minF.point[0] + offsetX, minF.point[1] + offsetY)
    if point_in_closeList(currentPoint):
        return
    # 设置单位花费
    if offsetX == 0 or offsetY == 0:
        g = 10
    else:
        g = 14
    # 如果不再openList中，就把它加入openlist
    currentNode = point_in_openList(currentPoint)
    if not currentNode:
        currentNode = Node(currentPoint, g=minF.g + g)
        currentNode.father = minF
        openList.append(currentNode)
        return
    # 如果在openList中，判断minF到当前点的G是否更小
    if minF.g + g < currentNode.g:  # 如果更小，就重新计算g值，并且改变father
        currentNode.g = minF.g + g
        currentNode.father = minF

def a_star():
    global openList
    global closeList
    openList.append(Node(start_point))
    # 2.主循环逻辑
    while True:
        # 找到F值最小的点
        minF = get_minF_node()
        # 把这个点加入closeList中，并且在openList中删除它
        closeList.append(minF)
        openList.remove(minF)
        # 判断这个节点的上下左右节点及对角线节点
        search_near(minF, -1, 0)  # 左边
        search_near(minF, 1, 0)  # 右边
        search_near(minF, 0, 1)  # 上边
        search_near(minF, 0, -1)  # 下边
        search_near(minF, -1, 1)  # 左上角
        search_near(minF, -1, -1)  # 左下角
        search_near(minF, 1, 1)  # 右上角
        search_near(minF, 1, -1)  # 右下角
        # 判断是否终止
        point = end_point_in_closeList()
        # 如果终点在关闭表中，就返回结果
        if point:
            cPoint = point
            pathList = []
            while True:
                if cPoint.father:
                    pathList.append(cPoint.point)
                    cPoint = cPoint.father
                else:
                    # break
                    return list(reversed(pathList))
                    # print('abc')
        if len(openList) == 0:
            return None
            # print('abc')

# 运行
a_star()
# (1, 2)->(0, 3)->(1, 4)->(2, 5)]
