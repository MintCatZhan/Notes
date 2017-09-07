from math import *
import sys
import random

# question 1 point ADT class with an added method of return Manhattan distance
class Point:
    def __int__(self, x, y):
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


# question 2 point set ADT class
class PointSet:
    def __int__(self, list):
        self.items = set(list)

    def insert(self, x):
        self.items.add(x)

    def delete(self, x):
        self.items.remove(x)

    # (BF)
    def closetPointBF(self, l):
        result = [None] * 2
        if len(l) < 2:
            result[0] = l[0]
            tempPoint = Point()
            tempPoint.x = sys.maxsize
            tempPoint.y = sys.maxsize
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

    # question 3b, divide-and-conquer algorithm
    # return the pair of points which have smallest pairwise distance
    def closePairOfPointsDandC(self, l):
        # brute force if the num of points is not much
        if len(l) <= 10:
            return self.closetPointBF(l)
        else:
            # get the mid point of all points by their Xs
            minX = sys.maxsize # initial min X big enough
            maxX = -sys.maxsize - 1 # initial max X small enough
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

            sorted(leftList,key = lambda p:p.x)
            sorted(rightList, key = lambda p: p.x)

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
            sorted(midList, key = lambda p:p.y)

            # get possible pair of points from leftMidLineList and rightMidLineList
            if len(midList) < 10 and len(midList) >= 2:
                if midList[0].distance_Manhattan(midList[1]) < minDist \
                        and midList[0].distance_Manhattan(midList[1]) != 0:
                    result = midList
            else:
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

# You can increment the stack depth allowed - with this, deeper recursive calls will be possible, like this:
#
# import sys
# sys.setrecursionlimit(10000) # 10000 is an example, try with different values
#
# But I'd advise you to first try to optimize your code, for instance, using iteration instead of recursion.

# plt.plot(xAxis, yAxis, 'ro')
# plt.title('Manhattan Distance')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.axis([0, 100, 0, 100])
# plt.show()



# #### ****** if 2 points have totally same X and Y axis, seem them as one point
def test():
    ps = PointSet()
    ll = []
    xAxis = []
    yAxis = []
    for i in range(2000):
        p = Point()
        p.x = random.randint(1, 2000)
        p.y = random.randint(1, 2000)
        xAxis.append(p.x)
        yAxis.append(p.y)
        # print("adding points:", p.x, "y: ", p.y)
        ll.append(p)
    ps.items = ll
    print("setted ps.items")
    # r = ps.closetPointBF(ps.items)
    r = ps.closePairOfPointsDandC(ps.items)
    print("bf closet: p1x--> ", r[0].x, "p1.y-->", r[0].y, "p2.x-->", r[1].x, "p2.y-->", r[1].y)

if __name__=='__main__':
    from timeit import Timer
    t = Timer(lambda: test())
    print(t.timeit(number=100))

# 1. how to use timeit, cuz there are some self-defined classes are going to be used in the timeit stmt
# 2. about the runtime recurrence relation, cuz im using the build-in func, that is "sorted" func, how to evaluate its relation ???how can i know this??
