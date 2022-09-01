'''
VALIDATE IF A BINARY TREE IS A BST OR NOT
METHOD 1. SET NEGATIVE AND POSITIVE BOUNDS
'''
INT_MAX= float('inf')
INT_MIN= float('-inf')

class Node:
    def __init__(self, item):
        self.item= item
        self.left=None
        self.right=None

def isBST(root):
    return isBSTUtil(root,INT_MIN, INT_MAX)

def isBSTUtil(root,min,max):
    if root is None:
        return True #empty tree return true

    #min < root < max
    if root.item<min or root.item>max:
        return False

    #check if the left and right subtrees fit in 
    #for left subtree=>the root must be the max and min should be the limit
    #for right subtree=>the root must be the min and max should be the limit
    return (isBSTUtil(root.left,min,root.item-1) and isBSTUtil(root.right,root.item+1,max))
 
#tree construction process
root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(3)

if isBST(root):
    print('This is a valid Binary Search Tree')
else:
    print('This is not a valid binary search tree.')    



        