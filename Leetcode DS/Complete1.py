'''
CHECK IF BINARY TREE IS COMPLETE OR NOT(USING RECURSIVE METHOD)
ALGORITHM+++
TOOK BINARY TREE IN ARRAY REPRESENTATION
LEFT= 2i+1, RIGHT=2i+2 AND ROOT AS i(0)
IF index you got is > num of elements in this array==>Not a complete binary tree
'''
class Node:
    def __init__(self, item):
        self.item= item
        self.left=None
        self.right=None

def CountNum(root):
    if root is None:
        return 0
    return 1+CountNum(root.left)+CountNum(root.right)

def isCompleteBT(root,i,count):
    if root is None:
        return True
    if i>count:
        return False
    return(isCompleteBT(root,2*i+1,count) and isCompleteBT(root,2*i+2,count))

root=Node(5)
root.left=Node(3)
root.right=Node(7)
root.left.left=Node(2)
root.left.right=Node(4)
root.right.right=Node(8)

count=CountNum(root)
i=0 #set the index
if isCompleteBT(root,i,count):
    print('This is a complete binary tree')
else:
    print('This is not a complete binary tree')