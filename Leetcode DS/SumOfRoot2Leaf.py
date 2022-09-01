'''
print all the root to leaf path sum of the given Binary Tree
USING RECURSION O(N)
TIPS
-USE DFS TO TRACE FROM ROOT TO LEAF NODES
'''
class Node:
	def __init__(self, x):
		
		self.item = x
		self.left = None
		self.right = None

pathSum=[]

def DFS(root,sum):
    if root is None:
        return
    sum+=root.item
    
    #if it reaches the leaf
    if(root.left==None and root.right==None):
        pathSum.append(sum)
    else:
        DFS(root.left,sum)
        DFS(root.right,sum)

def findSumPath(root):
    if root is None:
        return []

    DFS(root,0)
    for num in pathSum:
        print(num, end=' ')
    

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.left = Node(6)
root.left.right.right = Node(7)
root.left.left.right = Node(8)
root.left.left.right.left = Node(9)

findSumPath(root)
	
	
