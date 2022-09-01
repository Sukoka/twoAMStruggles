'''
CONSTRUCT ALL POSSIBLE KEYS FROM 1 TO N
'''



class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def preorder(root):
    if root is not None:
        print(root.val)
        preorder(root.left)
        preorder(root.right)

    
def oneToN(start,end):
    trees=[]
    if start>end:
        trees.append(None)
        return trees

    for i in range(start,end+1):
        lTree=oneToN(start,i-1)
        rTree=oneToN(i+1,end)

        for l in range(len(lTree)):
            left=lTree[l]
            for r in range(len(rTree)):
                right=rTree[r]
                root=Node(i)
                root.left=left
                root.right=right
                trees.append(root)
    return trees

construct=oneToN(1,3)
for i in range(len(construct)):
    preorder(construct[i])
    print(' ')

