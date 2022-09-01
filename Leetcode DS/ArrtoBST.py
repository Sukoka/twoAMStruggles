'''
SORTED ARRAY TO BALANCED BST
INPUT: ARRAY
1. FIND THE MID OF THAT ARRAY AND MAKE IT THE ROOT
2. RECURSIVELY CONSTRUCT THE LEFT AND RIGHT SUBTREES BY PARTING THE MIDDLE
'''

class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None


def sortedArrtoBST(arr):
    if not arr:
        return None
    
    #look for the mid of that array
    #this is the index 
    mid= (len(arr))/2
    m=int(mid)

    #set the root to the mid of the array
    root= Node(arr[m])

    #Build the left and right Stree by recursively putting the array to halve
    root.left=sortedArrtoBST(arr[:m])

    root.right=sortedArrtoBST(arr[m+1:])

    return root

#for output
def preorder(root):
    if root is None:
        return None

    print(str(root.val))
    preorder(root.left)
    preorder(root.right)


arr=[-10,-3,0,5,9]
root= sortedArrtoBST(arr)

print('Output in Preorder Fashion')
preorder(root)



        