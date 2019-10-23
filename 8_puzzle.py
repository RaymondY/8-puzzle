# Astar Algorithm
import re
import time
import copy

# Node class
class Node:
    def __init__(self, statement):
        self.statement = statement  # 状态，list
        self.father = None  # 记录父节点，用于打印过程
        # F = G + H
        self.G = 0
        self.H = 0
# Use "Manhattan Distance" in "H"
    def setH(self, target):
        for i in range(0, 3):
            for j in range(0, 3):
                index = i * 3 + j
                if (index == 8):
                    continue
                else:
                    x = int(target[index]) % 3
                    y = int(target[index]) // 3
                    self.H += abs(x - i) + abs(y - j)

    def setG(self, G):
        self.G = G

    def setFather(self, father):
        self.father = father

    def getFather(self):
        return self.father

    def getG(self):
        return self.G

    def getF(self):
        return self.G + self.H

# Determine if there is a solution by 'odd and even sequence
def getReverse(statement):
    sum = 0
    for i in range(0, len(statement)):
        for j in range(0, i):
            if (statement[j] > statement[i]):
                sum += 1
        # if(statement[i] == 0):
        #     continue
        # else:
        #     for j in range(0, i):
        #         if(statement[j]>statement[i]):
        #             sum += 1
    return sum  # 奇偶序列结果，判断sum的奇偶性即可

def parityCheck(start, target):
    startReverse = getReverse(start)
    targetReverse = getReverse(target)
    if (startReverse % 2 != targetReverse % 2):
        return False
    else:
        return True

def move(currentNode, startX, startY, targetX, targetY):
    currentNode.statement[startX + startY * 3], currentNode.statement[targetX + targetY * 3] = \
    currentNode.statement[targetX + targetY * 3], currentNode.statement[startX + startY * 3]
    return currentNode

def showBoard(statement):
    for i in range(0,3):
        for j in range(0,3):
            print(statement[i * 3 + j], end = ' ')
        print("\r")
    print("----------")

class Astar:
    def __init__(self, start, target):

        self.target = target
        self.startNode = Node(start)
        self.targetNode = Node(target)
        # self.currentNode = self.startNode
        self.openTable = []
        self.closeTable = []
        self.path = []
        self.step = 0

    def start(self):
        self.startNode.setH(self.target)
        self.startNode.setG(self.step)
        self.openTable.append(self.startNode)

        while True:
            self.currentNode = self.getMinF()
            self.closeTable.append(self.currentNode)
            self.openTable.remove(self.currentNode)
            self.step = self.currentNode.getG()
            # print(self.currentNode.statement)
            self.getAllStateSet()
            # 检查是否找到目标状态
            # 若可以到达目标，即target在openTable中，则结束，此时G即为最少步骤
            if self.nodeInOpenTable(self.targetNode):
                tempNode = self.getNodeFromOpenTable(self.targetNode)
                while True:
                    self.path.append(tempNode)
                    # 根据父亲node倒序找到移动方案
                    if (tempNode.getFather() != None):
                        tempNode = tempNode.getFather()
                    else:
                        return True
            # 以防万一 设置无解情况
            elif (len(self.openTable) == 0):
                return False
            # 否则生成下一步所有能转移的状态集S

    def nodeInOpenTable(self, node):
        for temp in self.openTable:
            if (node.statement == temp.statement):
                return True
        return False

    def nodeInCloseTable(self, node):
        for temp in self.closeTable:
            if (node.statement == temp.statement):
                return True
        return False

    def getMinF(self):
        minNode = self.openTable[0]
        for node in self.openTable:
            if (node.getF() < minNode.getF()):
                minNode = node
        return minNode

    def getNodeFromOpenTable(self, node):
        for tempNode in self.openTable:
            if (tempNode.statement == node.statement):
                return tempNode
        return None

    def getEverySet(self, nextNode):
        # 1. omit
        if not self.nodeInCloseTable(nextNode):
            tempG = self.step
            # 2. 不在openTable，则加入
            if not self.nodeInOpenTable(nextNode):
                nextNode.setG(tempG)
                nextNode.setH(self.target)
                nextNode.setFather(self.currentNode)
                self.openTable.append(nextNode)
            # 3. 在openTable中，计算新的G，若smaller，则update openTable
            else:
                tempNode = self.getNodeFromOpenTable(nextNode)
                if (self.currentNode.getG() + tempG < tempNode.getG()):
                    tempNode.setG(self.currentNode.getG() + tempG)
                    tempNode.setFather(self.currentNode)

    def getAllStateSet(self):
        index = self.currentNode.statement.index("0")
        self.step += 1
        x = index % 3
        y = index // 3

        # 分四种情况累加下一步状态集(移动一步的所有可能构成状态集，四种)
        # 因为是四种情况累加，故应使用四个if
        if (x > 0):
            nextNode = move(copy.deepcopy(self.currentNode), x, y, x - 1, y)  # 空白与左边数字交换
            self.getEverySet(nextNode)
        if (x < 2):
            nextNode = move(copy.deepcopy(self.currentNode), x, y, x + 1, y)  # 空白与右边数字交换
            self.getEverySet(nextNode)
        if (y > 0):
            nextNode = move(copy.deepcopy(self.currentNode), x, y, x, y - 1)  # 空白与上边数字交换
            self.getEverySet(nextNode)
        if (y < 2):
            nextNode = move(copy.deepcopy(self.currentNode), x, y, x, y + 1)  # 空白与下边数字交换
            self.getEverySet(nextNode)

    def showPath(self):
        # 倒序输出即可
        for node in self.path[::-1]:
            showBoard(node.statement)

if __name__ == '__main__':
    inputString = input("请输入按顺序输入起始位置，以空格间隔，以回车结束，最后一位数字后不要有空格。以下为位置序号：\n2, 8, 3\n1, 0, 5\n4, 7, 6\n以下为输入示例：1 8 4 2 3 0 7 5 6\n请输入：\n")
    if re.match("([0-9]\s){8}\d", inputString):

        start = inputString.split()     # 开始状态
        target = ['1', '2', '3', '4', '5', '6', '7', '8', '0']     # 目标状态
        if not parityCheck(start, target):
            print("该情况无解！")
        else:
            startTime = time.time()  # 开始时间
            result = Astar(start, target)
            if result.start():
                print("采用以下方式：")
                result.showPath()
                endTime = time.time()  # 结束时间
                timeCost = endTime - startTime  # 时间消耗
                print("共用%d步" %(result.step))
                print("启发式搜索算法用时%f秒" %(timeCost))
            else:
                print("该情况无解或没算出来？")
    else:
        print("输入格式不正确！")
