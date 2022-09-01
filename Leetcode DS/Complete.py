'''
CHECK IF A BINARY TREE IS COMPLETE TREE OR NOT (USING LEVEL ORDER TRAVERSAL BFS)
+++PROPERTIES+++
THE TREE MUST BE FULL ON ALL LEVELS EXCEPT THE LEAF LEVEL.
ALL LEAVES MUST INCLINE TOWARDS THE LEFT SIDE
        5
       / \
      3   7
     / \   \          #not valid since 7's left kid is none
    2   4   8
'''
class Node:
    def __init__(self, item):
        self.item= item
        self.left=None
        self.right=None

def isCompleteBT(root):
    if root is None:
        return True #empty trees always true

    flag=False
    q=[]    #Build an empty queue
    q.append(root)  #traverse from the root
    while (len(q)>0):
        temp=q.pop(0)
        if temp.left:   #if temp has left subtree
            if flag==True:
                return False
            q.append(temp.left)
        else:
            flag=True   #no left kid==>no full node==>null in output
        if temp.right:  #same level right kid
            if flag==True:
                return False
            q.append(temp.right)
        else:   #no full node==>no complete
            flag=True
    
    return True #after traversing all levels, it is a valid complete tree

root=Node(5)
root.left=Node(3)
root.right=Node(7)
root.left.left=Node(2)
root.left.right=Node(4)
root.right.right=Node(8)

if isCompleteBT(root):
    print('This is a complete binary tree')
else:
    print('This is non-complete binary tree')