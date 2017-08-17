# def merger1(a, b, L):
#     if len(a) == 0 and len(b) == 0:
#         L = []
#     elif len(a) == 0:
#         L.append(b[0])
#         merger(a, b[1:], L)
#     elif len(b) == 0:
#         L.append(a[0])
#         merger(a[1:], b, L)
#     else:
#         if a[0] >= b[0]:
#             L.append(b[0])
#             merger(a, b[1:], L)
#         else:
#             L.append(a[0])
#             merger(a[1:], b, L)
#     return L

class List:
    def __init__(self, init=[]):
        self.contents = init

    def cons(self, elem):
        return List(init=[elem] + self.contents)

    def first(self):
        return self.contents[0]

    def rest(self):
        return List(self.contents[1:])

    def is_empty(self):
        return self.contents == []

    def length(self):
        if self.is_empty():
            return 0
        else:
            return 1 + self.rest().length()

    def find(self, x):
        if self.is_empty():
            return False
        else:
            return self.first() == x or self.rest().find(x)

    def list_max(self):
        if self.length() == 1:
            return self.first()
        else:
            return max(self.first(), self.rest().list_max())

    def total(self):
        if self.is_empty():
            return 0
        else:
            return self.first() + self.rest().total()

    def last(self):
        if self.length() == 0:
            return None
        if self.length() == 1:
            return self.first()
        else:
            return self.rest().last()


def merge( x, y):
    if x.is_empty():
        return y

    if y.is_empty():
        return x
    if x.first() < y.first():
        res = merge(x.rest(), y).cons(x.first())
    else:
        res = merge(x, y.rest()).cons(y.first())
    return res



def mergeSort(alist):
    if alist.length() > 1:
        mid = alist.length() // 2
        leftHalf = List(alist.contents[:mid])
        rightHalf = List(alist.contents[mid:])

        leftHalf = mergeSort(leftHalf)
        rightHalf = mergeSort(rightHalf)
        alist = merge(leftHalf, rightHalf)

    return alist

res = mergeSort(List([54, 26, 93, 17, 77, 31, 44, 55, 20]))
print(res.contents)