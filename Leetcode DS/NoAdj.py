'''
MAXIMUM SUM NODES BINARY TREE WITH NO TWO ADJACENT NODES
'''
class Node:
    def __init__(self,item):
        self.item=item
        self.left=None
        self.right=None

def sumOfGrandChildren(root,m):
    sum=0
    #if left kid exists, go for child of left kid(grandchildren) since no two adjacent
    if root.left!=None:
        sum+=getSumUtil(root.left.left,m)+getSumUtil(root.left.right,m)

    if root.right!=None:
        sum+=getSumUtil(root.right.left,m)+getSumUtil(root.right.right,m)

    #if both sides exist, adhere right grandchild's values to the left 
    return sum

def getSumUtil(root,m):
    if root is None:
        return 0
    
    #if root is alrd processed in m dict
    if root in m:
        return m[root]

    #root-grandchild pair
    include= root.item+ sumOfGrandChildren(root,m)

    #children-grandchildchild pair (excluding the root)
    exclude=getSumUtil(root.left,m)+getSumUtil(root.right,m)

    m[root]=max(include,exclude)    #assigning value to 'root' key
    return m[root]

def getSum(root):
    if root is None:
        return 0

    m=dict()
    return getSumUtil(root,m)

root=Node(5)
root.left=Node(3)
root.right=Node(7)
root.left.left=Node(2)
root.left.right=Node(4)
root.right.right=Node(8)

sum=getSum(root)
print('Max sum with no two adjacent nodes is', sum)