
# res = list()
#
#
# def merger(x, y):
#     if len(x) == 0 & len(y) == 0:
#         return []
#     elif len(x) == 0:
#         y1 = y[0]
#         res.append(y1)
#         merger(x, removeHead(y))
#     elif len(y) == 0:
#         x1 = x[0]
#         res.append(x1)
#         merger(removeHead(x), y)
#     else:
#         if x[0] >= y[0]:
#             res.append(y[0])
#             res.append(x[0])
#         else:
#             res.append(x[0])
#             res.append(y[0])
#         merger(removeHead(x), removeHead(y))
#
#
#
# def removeHead(x):
#     if len(x) == 0:
#         return x
#     else:
#         return x[1:]