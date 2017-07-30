# Yuan Zhan 26693267


import math

#1
def isOddorEven():
    txt = input('Please enter an integer number: ')
    n = int(txt)

    if n % 2 == 1:
        print(n, 'is odd')
    else:
        print(n, 'is even')
# isOddorEven()


#2
def computeSquareNum():
    txt = input('Enter the value for n.. ')
    n = int(txt)

    for x in range(n + 1):
        print(x * x)
# computeSquareNum()

#3
def readValueOfx():
    txt = input('Please enter an integer number: ')
    n = int(txt)
    return n


def determineTheParity(n):
    isOdd = False
    if n % 2 == 1:
        isOdd = True
    return isOdd

def displayResult():
    n = readValueOfx()
    isOdd = determineTheParity(n)
    if isOdd:
        print(n, ' is odd')
    else:
        print(n, ' is even')

# displayResult()


#4 recursively
def sum(x):
    if (x == 1):
        return 1
    else:
        return x + sum(x - 1)

def run():
    x = input('input a number: ')
    num = int(x)
    n = sum(num)
    print('The sum is' , n)

# run()


#5
def findMiniValueOfList(list):
    if len(list) == 1:
        return list[0]
    else:
        mini = findMiniValueOfList(list[1:])
        return mini if mini < list[0] else list[0]

def test():
    list = [4, 1, 23, 0, 2, 3]
    miniNum = findMiniValueOfList(list)
    print('The index of minimum value is: ', list.index(miniNum))

# test()


#6
def findThreeElesSumToZero(list):
    if len(list) < 3:
        print('invalid list, less than 3 elements')
    else:
        list.sort()


        # for x in range((len(list)/2) + 1 , len(list)):
        for i in range(len(list) - 2):
            for j in range(i, len(list) - 1):
                for o in range(j, len(list)):
                    if list[i] + list[j] + list[o] == 0:
                        print(list[i], '',  list[j],' ',  list[o])

def test():
    list = [-25, -10, -7, -3, 2, 4, 8, 10]
    findThreeElesSumToZero(list)

# test()

# not efficient , n^3


#7
def sieveOfEra():
    n = int(input('input an Integer: '))
    if n <= 1:
        print('input a number greater than 1')
    else:
        A = range(2, n)

        primes = dict()

        for x in A:
            primes[x] = True

        for i in range(2, int(math.sqrt(n))):
            if primes[i]:
                for j in range(i * i, n, i):
                    primes[j] = False

        for t in primes:
            if primes[t]:
                print(t)
# sieveOfEra()



#8 recursive
def computeMaxNum(list):
    if len(list) == 1:
        return list[0]
    else:
        max = computeMaxNum(list[1:])
        return max if max > list[0] else list[0]

def main():
    list  = eval(input('input a list of nums:'))
    print('the largest number is: ', computeMaxNum(list))

# main()



#9
class Rectangle(object):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def computeArea(self):
        return self.length * self.width

    def computePerimeter(self):
        return 2 * self.length + 2 * self.width

# rec = Rectangle(7, 4)
# print('the area is:' , rec.computeArea())
# print('the perimerter is: ' , rec.computePerimeter())