from math import *

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

    # question 3a, brute-force algorithm
    # return the pair of points which have smallest pairwise distance
    def closetPairOfPointsBruteForce(self):
        l = list(self.items)

        distance = []
        resPairDict = {}
        i = 0 # the index num of first point
        while i < len(l):
            j = i # the index num of second point
            while j < len(l):
                # add the key-value pair to the dict, it looks like  "i, j": distance
                distance.append(l[i].distance_Manhattan(l[j]))
                resPairDict[l[i].distance_Manhattan(l[j])] = str(i) + ', ' + str(j)

        distance.sort() # sort the distance
        resStr = resPairDict[distance[0]] # get the element from dict by the first element in sorted distance list, that is the closest one
        resArr = resStr.split(', ', 1) # split the value
        p1 = l[int(resArr[0])] # get the 'i' here, then get the l[i] element, that is the first point
        p2 = l[int(resArr[1])] # get the 'j' here, then get the l[j] element, that is the second point
        return [p1, p2] # return the pair of closet points, in list format


    def closePairOfPointsDandC(self):
        return



