import math #importing math library to perform math function like square
import random #importing ramdom library to create random coordinates
from random import randint
from random import shuffle


class Partition():
    # creating function constructor to define empty partition
    def __init__(self):
        self.partition = []

        # creating function to display the List of clusters
    def display(self):
        print("The partitions are: ", self.partition)

        # generating new partition, which also means a new spanning tree

    def MakeSet(self, point):
        # set the point parent to the point itself
        point.parent = point
        # set initial rank of point to 0
        point.rank = 0

    # merging two clusters, which also means merging the spanning tree
    def Union(self, x, y):
        xRoot = self.Find(x)
        yRoot = self.Find(y)

        if xRoot.rank > yRoot.rank:
            yRoot.parent = xRoot

        elif xRoot.rank < yRoot.rank:
            xRoot.parent = yRoot

        # Unless x and y are already in same set, merge them
        elif xRoot != yRoot:
            yRoot.parent = xRoot
            xRoot.rank = xRoot.rank + 1

    # finding the cluster to which a point belongs
    def Find(self, x):
        if x.parent == x:
            return x
        else:
            x.parent = self.Find(x.parent)
            return x.parent

    # get partition size
    def PartitionSize(self):
        return len(self.partition)

    # creating function to perform Kruskal's algorithm,minimum-spanning-tree algorithm in order to find
    # the points of the least possible distance that connects any two trees in the forest
    def kruskal(self, coordinates, shortestDistance):
        # running for loop to get each coordinate
        for coordinate in coordinates:
            # creating a spanning tree for each coordinate
            self.MakeSet(coordinate)

        # initialising a set to store the minimum_spanning_tree
        minimum_spanning_tree = set()
        # sorting the list of the shortest distance respective to their coordinates
        shortestDistance.sort()
        # for loop to get the distance for the respective coordinates
        for info in shortestDistance:
            dist, point1, point2 = info
            # calling function Find() and comparing to avoid creating cycle in tree
            if self.Find(point1) != self.Find(point2):
                # combining the trees
                self.Union(point1, point2)
                minimum_spanning_tree.add((dist, point1.displayPoint(), point2.displayPoint()))

        return minimum_spanning_tree

    # clustering the data into k clusters and returning the center points of the clusters
    def k_clustering(self, data_pts, k):

        # see if two lists have the same elements
        def lists_are_same(la, lb):
            out = False
            for item in la:
                if item not in lb:
                    out = False
                    break
                else:
                    out = True
            return out

        # distance between (x,y) points a and b
        def distance(a, b):
            # using euclidean distance between points a and b
            return math.sqrt(abs(a[0] - b[0]) ** 2 + abs(a[1] - b[1]) ** 2)

        # return the average of a one-dimensional list (e.g., [1, 2, 3])
        def average(a):
            return sum(a) / float(len(a))

        # setting k=1 to return at least one cluster is k is less than zero
        if k < 1:
            k = 1

        # Randomly generate k clusters with regards to cluster centers

        # put all of the data points into clusters
        self.partition = data_pts[:]
        # put the data points in random order
        shuffle(self.partition)
        # only keep the first k random clusters
        self.partition = self.partition[0:k]

        old_partitions, new_partitions = {}, {}
        for item in self.partition:
            old_partitions[item] = []  # every cluster has a list of points associated with it. Initially, it's 0

        while 1:  # just keep going forever, until our break condition is met
            tmp = {}
            for k in old_partitions:  # create an editable version of the old_clusters dictionary
                tmp[k] = []

            # Associate each point with the closest cluster center.
            # for each (x,y) data point
            for point in data_pts:
                min_clust = None
                # absurdly large, should be larger than the maximum distance for most data sets
                min_dist = 1000000000
                # for every possible closest cluster
                for pc in tmp:
                    pc_dist = distance(point, pc)
                    if pc_dist < min_dist:  # if this cluster is the closest, have it be the closest
                        min_dist = pc_dist
                        min_clust = pc
                # add each point to its closest cluster's list of associated points
                tmp[min_clust].append(point)

            # Recompute the new cluster centers
            for k in tmp:
                associated = tmp[k]
                xs = [pt[0] for pt in associated]  # build up a list of x's
                ys = [pt[1] for pt in associated]  # build up a list of y's
                x = average(xs)  # x coordinate of new cluster
                y = average(ys)  # y coordinate of new cluster
                new_partitions[(x,
                                y)] = associated  # these are the points the center was built off of, they're *probably* still associated

            if lists_are_same(old_partitions.keys(),
                              new_partitions.keys()):  # if we've reached equilibrium, return the points
                return old_partitions.keys()

            else:  # old_clusters = new_clusters, and clear new_clusters.
                old_partitions = new_partitions
                new_partitions = {}

        print(self.coordinates)
        # http://stackoverflow.com/questions/8607670/get-point-ids-after-clustering-using-python


