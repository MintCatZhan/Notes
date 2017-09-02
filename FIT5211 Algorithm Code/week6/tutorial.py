
def measureHeight(root):

    if root.hasNoChild or root == None:
        return 0
    else:
        height = 0
        # left child node
        leftHeight = measureHeight(root.leftChild) + 1
        rightHeight = measureHeight(root.rightChild) + 1
        return leftHeight if leftHeight >= rightHeight else rightHeight
