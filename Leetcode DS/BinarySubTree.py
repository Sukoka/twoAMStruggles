'''
CHECK IF A BINARY TREE IS A SUBTREE OF ANOTHER SUBTREE OR NOT
TIME COMPLEXITY 0(N)
OTHER METHOD REQUIRES MATCHING EACH ELEMENTS IN BOTH TREES WHICH TAKES 0(N^2) TIME
'''
class Node:
    #build this shit
    def __init__(self,val):
        self.left= None
        self.right= None
        self.val=val

def storeInorder(root,inorder):
    if root is None:
        return None
    #LEFT ROOT RIGHT
    storeInorder(root.left,inorder)
    inorder.append(root.val)
    storeInorder(root.right,inorder)

def storePreorder(root,preorder):
    if root is None:
        return None
    #ROOT LEFT RIGHT
    preorder.append(root.val)
    storePreorder(root.left,preorder)
    storePreorder(root.right,preorder)

def isSubtree(tree,subtree):
    if tree==subtree:
        return True
    #the original tree cannot be empty
    if tree is None:
        return False
    #every null tree is a subtree of a tree so
    if subtree is None:
        return True
    
    #store the traversals of both trees
    t=[]
    s=[]

    storeInorder(tree,t)
    storeInorder(subtree,s)

    if (set(s).issubset(set(t)))==False:
        return False
    
    t.clear()
    s.clear()
    
    storePreorder(tree,t)
    storePreorder(subtree,s)

    if (set(s).issubset(set(t)))==False:
        return False

    return True

#original tree
T = Node(26)
T.right = Node(3)
T.right.right  = Node(3)
T.left = Node(10)
T.left.left = Node(4)
T.left.left.right = Node(30)
T.left.right = Node(6)

#subtree
S = Node(10)
S.right = Node(6)
S.left = Node(4)
S.left.right = Node(30)

if (isSubtree(T,S)):
    print('It is a subtree')
else:
    print('It is not a subtree')