'''
CHECK IF BINARY TREE IS HEIGHT BALANCED OR NOT
1. IF THE DIFFERENCE OF HEIGHT BETWEEN THE LEFT AND RIGHT IS NOT MORE THAN 1, IT  IS HEIGHT BALANCED
'''
class Node:
    def __init__(self, item):
        self.item= item
        self.left=None
        self.right=None

class Height:
    def __init__(self):
        self.height=0

def height(root):
    if root is None:
        return 0
    return max(height(root.left), height(root.right))+1


#the function that'll check if the tree is balanced
def isBalanced(root):
    #if the root is empty it is balanced cuz it never had the chance to be imbalanced
    if not root:
        return True

    #obj of the Height class and access the class variable
    lh=Height()
    rh=Height()

    #update the Height attribute via height function 
    lh.height=height(root.left)
    rh.height=height(root.right)

    #check if left and right subtrees are balanced
    l=isBalanced(root.left)
    r=isBalanced(root.right)

    #if absolute val of lheight-rheight is not more than 1 &&
    #if left and right subtrees are balanced
    if(abs(lh.height-rh.height)<=1):
        return l and r
    
    return False

#building process
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(8)

if isBalanced(root):
    print('The tree is height balanced')
else:
    print('The tree is not balanced')