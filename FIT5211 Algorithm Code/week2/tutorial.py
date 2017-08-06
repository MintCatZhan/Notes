
import time


def printSquareNum():
    txt = input('input a number: ')
    num = int(txt)

    print("The square number is: ", num * num)

# printSquareNum()

def find(L, x):

    if len(L) == 0:
        print("should not be an empty list")
        return

    if x is None:
        print("x is null, not acceptable")

    if isinstance(x, int):
        for l in L:
            if l == x:
                print("foud")
                return
    else:
        print("wrong data type, should be an integer")
        return

    print("not found")
    return

# find([1,32, "fd",2],2 )


def getFiboIteratively(n):
    cursor1 = 1
    cursor2 = 2
    i = 1

    while i < n:
        temp = cursor2
        cursor2 = cursor1 + cursor2
        cursor1 = temp
        i += 1

    print(cursor1)

# getFiboIteratively(5)


def getFiboRecursion(n):
    if n <= 2:
        return n
    else:
        return getFiboRecursion(n - 1) + getFiboRecursion(n - 2)

# print("The result is: ",getFiboRecursion(10), "Using: ", time.process_time())


def memoize(f):
    memo = {}

    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper


# fib = memoize(getFiboRecursion)

# print("The fib is(memo): ", fib(10), "Using: ", time.process_time())

class Queue():
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)



def repeatx2(queue):
    result = Queue()
    while not queue.isEmpty():
        value = queue.dequeue()
        result.enqueue(value)
        result.enqueue(value)

    return result

def printQuere(queue):
    while not queue.isEmpty():
        print(queue.dequeue())

t = Queue()
t.enqueue(1)
t.enqueue(2)
t.enqueue(3)
# printQuere(repeatx2(t))


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

def symmetery(queue):
    s = Stack()
    r = Queue()

    while not queue.isEmpty():
        v = queue.dequeue()
        s.push(v)
        r.enqueue(v)

    while not s.isEmpty():
        r.enqueue(s.pop())

    return r
    # while

printQuere(symmetery(t))

