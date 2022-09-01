'''
CONVERT THE NORMAL/SKEWED BINARY TREE TO THE BALANCED BST
1. ADD THE NODES OF THE ORIGINAL ONE TO AN ARRAY
2. FROM THAT ARRAY, CONSTRUCT THE BALANCED BST
'''

class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None


def storeInorder(root,nodes):
    if not root:
        return None
    storeInorder(root.left,nodes)
    nodes.append(root.val)
    storeInorder(root.right,nodes)

#where the balanced BST will be constructed
def buildBST(nodes,start,end):

    if start>end:
        return None
    
    #set the mid as the root
    # // is the floor division
    mid= (start+end)//2
    root= nodes[mid]

    #construct the left subtree
    root.left=buildBST(nodes,start,mid-1)
    #construct the right subtree
    root.right=buildBST(nodes,mid+1,end)

    return root

def build(root):
    nodes=[]  #empty arr to store inorder traversal of the skewed tree
    storeInorder(root,nodes)
    n=len(nodes)
    return buildBST(nodes,0,n-1)

def preorder(root):
    if root is None:
        return None

    print(str(root.val))
    preorder(root.left)
    preorder(root.right)


#build a left skewed binary tree
root=Node(10)
root.left= Node(8)
root.left.left= Node(7)
root.left.left.left= Node(6)
root.left.left.left.left= Node(5)
root= build(root)

print('Print in the preorder')
preorder(root)