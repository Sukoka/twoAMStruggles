'''
MAXIMUM SUM TREE WITH NO ADJACENT LEVEL
ROOT==>TAKE GRANDCHILD LEVEL
CHILD==>SKIP THE ADJACENT LEVEL
'''
class Node:
    def __init__(self,item):
        self.item=item
        self.left=None
        self.right=None

def getRealSum(root):
    if root is None:
        return 0
    sum=root.item

    if (root.left):
        sum+=getRealSum(root.left.left)+getRealSum(root.left.right)

    if(root.right):
        sum+=getRealSum(root.right.left)+getRealSum(root.right.right)

    return sum

def getSum(root):
    if root is None:
        return 0

    return max(getRealSum(root),getRealSum(root.left)+getRealSum(root.right))

root=Node(5)
root.left=Node(3)
root.right=Node(7)
root.left.left=Node(2)
root.left.right=Node(4)
root.right.right=Node(8)
root.right.right.left=Node(3)
root.right.right.right=Node(9)

sum=getSum(root)
print('Biggest Sum calculated from no adjacent level:', sum)