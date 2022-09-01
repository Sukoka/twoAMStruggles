'''
PRINT THE LONGEST PATH FROM ROOT TO LEAF
'''
class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def root2leaf(root):
    if root == None:
        return []

    leftTree=root2leaf(root.left)
    rightTree=root2leaf(root.right)

    if(len(leftTree)>len(rightTree)):
        leftTree.append(root.val)

    else:
        rightTree.append(root.val)

    if len(leftTree) > len(rightTree):
        return leftTree
 
    return rightTree

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.left = Node(6)
root.left.right.right = Node(7)
root.left.left.right = Node(8)
root.left.left.right.left = Node(9)

ans=root2leaf(root)
n=len(ans)
#print the last element which is root
print(ans[n-1],end=' ')
for i in range(n-2,-1,-1):
    print(ans[i], end=' ')