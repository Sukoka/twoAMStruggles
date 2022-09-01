'''
CHECK IF A BST IS A SUMTREE OR NOT
SUMTREE
-LEFT+RIGHT=ROOT
'''
class Node:
    def __init__(self, val):
        self.val= val
        self.left=None
        self.right=None

#where you do the sum
def sum(root):
    if root is None:
        return 0
    return (sum(root.left)+root.val+sum(root.right))

def isSumTree(root):
    #empty case return 1
    #0 False 1 True
    if root==None or root.left==None and root.right==None:
        return 1

    lSum=sum(root.left)
    rSum=sum(root.right)

    if root.val==lSum+rSum and isSumTree(root.left) and isSumTree(root.right):
        return 1
    return 0

#construction
root = Node(26)
root.left= Node(10)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(6)
root.right.right = Node(3)

if isSumTree(root):
    print('It is a sumtree')
else:
    print('It is not a sumtree')