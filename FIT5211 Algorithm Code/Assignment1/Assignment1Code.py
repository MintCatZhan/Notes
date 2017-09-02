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
    #
    # # question 3a, brute-force algorithm
    # # return the pair of points which have smallest pairwise distance
    # def closetPairOfPointsBruteForce(self):
    #     l = list(self.items)
    #
    #     distance = []
    #     resPairDict = {}
    #     i = 0 # the index num of first point
    #     while i < len(l):
    #         j = i # the index num of second point
    #         while j < len(l):
    #             # add the key-value pair to the dict, it looks like  "i, j": distance
    #             distance.append(l[i].distance_Manhattan(l[j]))
    #             resPairDict[l[i].distance_Manhattan(l[j])] = str(i) + ', ' + str(j)
    #
    #     distance.sort() # sort the distance
    #     resStr = resPairDict[distance[0]] # get the element from dict by the first element in sorted distance list, that is the closest one
    #     resArr = resStr.split(', ', 1) # split the value
    #     p1 = l[int(resArr[0])] # get the 'i' here, then get the l[i] element, that is the first point
    #     p2 = l[int(resArr[1])] # get the 'j' here, then get the l[j] element, that is the second point
    #     return [p1, p2] # return the pair of closet points, in list format


    # easier way(BF) -- need to test
    def closetPointBF(self):
        l = list(self.items)
        result = [None] * 2
        dmin = sys.maxsize
        i = 0
        while i < len(l) - 1:
            j = i + 1
            while j < len(l):
                tmpmin = l[i].distance_Manhattan(l[j])
                if tmpmin < dmin:
                    dmin = tmpmin
                    result[0] = l[i]
                    result[1] = l[j]
                j = j + 1
            i = i + 1

        return result


    # question 3b, divide-and-conquer algorithm
    # return the pair of points which have smallest pairwise distance
    def closePairOfPointsDandC(self, l):
        # brute force if the num of points is not much
        result = [None] * 2
        if len(l) <= 10:
            dmin = sys.maxsize
            i = 0
            while i < len(l) - 1:
                j = i + 1
                while j < len(l):
                    tmpmin = l[i].distance_Manhattan(l[j])
                    if tmpmin < dmin:
                        dmin = tmpmin
                        result[0] = l[i]
                        result[1] = l[j]
                    j = j + 1
                i = i + 1
            return result
        else:
            # get the mid point of all points by their Xs
            minX = sys.maxsize # initial min X big enough
            maxX = -sys.maxsize - 1 # initial max X small enough
            i = 0
            while i < len(l):
                if l[i].x < minX:
                    minX = l[i].x
                if l[i].x > maxX:
                    maxX = l[i].x
                i = i + 1
            midX = (minX + maxX) // 2

            # split into 2 different list
            leftList = []
            rightList = []
            for point in l:
                if point.x <= midX:
                    leftList.append(point)
                else:
                    rightList.append(point)

            self.sortListByPointAxis(leftList, 1)
            self.sortListByPointAxis(rightList, 1)

            # get the pair of points that are closest from left half and right half
            leftResult = self.closePairOfPointsDandC(leftList)
            rightResult = self.closePairOfPointsDandC(rightList)

            # get the minmum distance of two sides
            dist1 = leftResult[0].distance_Manhattan(leftResult[1])
            dist2 = rightResult[0].distance_Manhattan(rightResult[1])
            if dist1 <= dist2:
                minDist = dist1
                result = leftResult
            else:
                minDist = dist2
                result = rightResult

            leftMidLineList = []
            rightMidLineList = []
            for point in leftList:
                if midX - point.x < minDist:
                    leftMidLineList.append(point)
            for point in rightList:
                if point.x - midX < minDist:
                    rightMidLineList.append(point)
            self.sortListByPointAxis(leftMidLineList, 0)
            self.sortListByPointAxis(rightMidLineList, 0)

            # get possible pair of points from leftMidLineList and rightMidLineList
            d = sys.maxsize
            z = 0
            y = 0
            while z < len(leftMidLineList):
                while y < len(rightMidLineList):
                    if abs(leftMidLineList[z].y - rightMidLineList[y].y) < minDist:
                        tmp = leftMidLineList[z].distance_Manhattan(rightMidLineList[y])
                        if tmp < d:
                            print("leftMidLineList[z] = ", leftMidLineList[z])
                            result[0] = leftMidLineList[z]
                            print("rightMidLineList[y] = ", rightMidLineList[y])
                            result[1] = rightMidLineList[y]
                        else:
                            print("result[0] = ", result[0])
                            print("result[1] = ", result[1])
                    y = y + 1
                z = z + 1

            return result


    def sortListByPointAxis(self, list, axis):
        if axis == 1:
            self.mergeSortByXaxis(list)
        else:
            self.mergeSortByYaxis(list)

    def mergeSortByXaxis(self, list):
        if (len(list) > 1):
            mid = len(list) // 2
            left = list[:mid]
            right = list[mid:]

            self.mergeSortByXaxis(left)
            self.mergeSortByXaxis(right)

            i = 0
            j = 0
            k = 0

            while i < len(left) and j < len(right):
                if left[i].x < right[j].x:
                    list[k] = left[i]
                    i = i + 1
                else:
                    list[k] = right[j]
                    j = j + 1
                k = k + 1

            while i < len(left):
                list[k] = left[i]
                i = i + 1
                k = k + 1

            while j < len(right):
                list[k] = right[j]
                j = j + 1
                k = k + 1

    def mergeSortByYaxis(self, list):
        if (len(list) > 1):
            mid = len(list) // 2
            left = list[:mid]
            right = list[mid:]

            self.mergeSortByYaxis(left)
            self.mergeSortByYaxis(right)

            i = 0
            j = 0
            k = 0

            while i < len(left) and j < len(right):
                if left[i].y < right[j].y:
                    list[k] = left[i]
                    i = i + 1
                else:
                    list[k] = right[j]
                    j = j + 1
                k = k + 1

            while i < len(left):
                list[k] = left[i]
                i = i + 1
                k = k + 1

            while j < len(right):
                list[k] = right[j]
                j = j + 1
                k = k + 1


ps = PointSet()
ll = []

for i in range(1000):
    p = Point()
    p.x = random.randint(1,1011)
    p.y = random.randint(1,1011)
    print("adding points:", p.x, "y: ", p.y)
    ll.append(p)

ps.items = ll
print("setted ps.items")
# r = ps.closetPointBF()
r = ps.closePairOfPointsDandC(ps.items)
print("bf closet: p1x--> ", r[0].x, "p1.y-->", r[0].y, "p2.x-->",r[1].x, "p2.y-->", r[1].y)
