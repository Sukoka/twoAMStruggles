'''
FIND ALL POSSIBLE TREES WITH GIVEN INORDER TRAVERSAL
//SIMILAR TO UNIQUE BST
'''
class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def preorder(root):
    if root is None:
        return
    else:
        print(root.val)
        preorder(root.left)
        preorder(root.right)

def given_Inorder(arr,start,end):
    trees=[]
    if start>end:
        trees.append(None)
        return trees

    #iterating every element as root
    for i in range(start,end+1):
        lTree=given_Inorder(arr,start,i-1)
        rTree=given_Inorder(arr,i+1,end)

        for l in lTree:
            for r in rTree:
                node=Node(arr[i])
                node.left=l
                node.right=r
            trees.append(node)
    
    return trees


inp=[4,5,7]
n=len(inp)
Trees=given_Inorder(inp,0,n-1)
for i in range(len(Trees)):
    preorder(Trees[i])
    print(' ')