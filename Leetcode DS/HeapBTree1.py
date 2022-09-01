'''
CHECK IF BINARY TREE IS HEAP BINARY TREE OR NOT(ITERATIVE METHOD, LEVEL TRAVERSAL)
'''
class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def is_HeapBTree(root):
    if root is None:
        return True
    flag=False
    q=[]
    q.append(root)
    while(len(q)>0):
        temp=q.pop(0)
        if temp.left!=None:
            if flag==True or temp.val<temp.left.val:
                return False
            q.append(temp.left)
        else:
            flag=True #no left kid==>no complete
        
        if temp.right!=None:
            if flag==True or temp.val<temp.right.val:
                return False
            q.append(temp.right)
        else:
            flag=True
    return True
root=Node(10)
root.left=Node(9)
root.right=Node(8)
root.left.left=Node(7)
root.left.right=Node(6)
root.right.right=Node(5)

if is_HeapBTree(root):
    print('Heap binary Tree')
else:
    print('Not heap binary tree')