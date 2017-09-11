from math import *
import sys
import random
import timeit
import matplotlib.pyplot as plt
from timeit import Timer

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_from_origin(self):
        return sqrt(self.x * self.x + self.y * self.y)

    def distance(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return sqrt(dx * dx + dy * dy)

    def translate(self, dx, dy):
        self.x += dx
        self.y += dy

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    # return the Manhattan distance of two points
    # |x_1 - x_2| + |y_1 - y_2|
    def distance_Manhattan(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)

class PointSet:
    def __init__(self):
        self.items = []

    def insert(self, x):
        self.items.append(x)

    def delete(self, x):
        self.items.remove(x)

    def __str__(self):
        content = ""
        for i in self.items:
            content = content + str(i)
        return content

    # question 3.a brute-force
    def closetPointBF(self, l):
        result = [None] * 2
        if len(l) < 2:
            result[0] = l[0]
            tempPoint = Point(sys.maxsize, sys.maxsize)
            result[1] = tempPoint
            return result

        dmin = sys.maxsize
        for i in range(len(l) - 1):
            for j in range(i + 1, len(l)):
                tmpmin = l[i].distance_Manhattan(l[j])
                if tmpmin < dmin and tmpmin != 0:
                    dmin = tmpmin
                    result[0] = l[i]
                    result[1] = l[j]
        return result

    # question 3.b divide-and-conquer
    def closePairOfPointsDandC(self, l):
        # brute force if the num of points is not much
        if len(l) <= 10:
            return self.closetPointBF(l)
        else:
            # get the mid point of all points by their Xs
            minX = sys.maxsize  # initial min X big enough
            maxX = -sys.maxsize - 1  # initial max X small enough
            for p in l:
                if p.x < minX:
                    minX = p.x
                if p.x > maxX:
                    maxX = p.x
            midX = (minX + maxX) // 2

            # split into 2 different list
            leftList = []
            rightList = []
            for point in l:
                if point.x <= midX:
                    leftList.append(point)
                if point.x > midX:
                    rightList.append(point)

            sorted(leftList, key=lambda p: p.x)
            sorted(rightList, key=lambda p: p.x)

            # get the pair of points that are closest from left half and right half
            leftResult = self.closePairOfPointsDandC(leftList)
            rightResult = self.closePairOfPointsDandC(rightList)
            # get the minmum distance of two sides
            dist1 = leftResult[0].distance_Manhattan(leftResult[1])
            dist2 = rightResult[0].distance_Manhattan(rightResult[1])

            minDist = sys.maxsize
            result = [None] * 2

            if dist1 <= dist2 and dist1 != 0:
                minDist = dist1
                result = leftResult
            if dist1 > dist2 and dist2 != 0:
                minDist = dist2
                result = rightResult

            midList = []
            for point in leftList:
                if midX - point.x < minDist:
                    midList.append(point)
            for point in rightList:
                if point.x - midX < minDist:
                    midList.append(point)
            sorted(midList, key=lambda p: p.y)

            # get possible pair of points from leftMidLineList and rightMidLineList
            for i in range(len(midList) - 7):
                for j in range(1, 8):
                    if i + j >= len(midList):
                        break
                    else:
                        tempd = midList[i].distance_Manhattan(midList[i + j])
                        if tempd < minDist and tempd != 0:
                            result[0] = midList[i]
                            result[1] = midList[i + j]
            return result

def testBF():
    ps = PointSet()
    for i in range(1000):
        p = Point(random.randint(1, 2000), random.randint(1, 2000))
        ps.insert(p)
    r = ps.closePairOfPointsDandC(ps.items)
    print(r[0], '', r[1])

if __name__=='__main__':
    from timeit import Timer
    tBF = Timer(lambda: testBF()).timeit(number=10000)