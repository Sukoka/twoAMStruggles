'''
VALIDATE IF A BINARY TREE IS A BST OR NOT
METHOD 2. THROUGH INORDER TRAVERSAL
BUT AVOIDING THE AUXILIARY ARRAY(THE ONE TO STORE INORDER) FOR SPACE EFFICIENCY
'''

class Node:
    def __init__(self, item):
        self.item= item
        self.left=None
        self.right=None

#where you do the inorder traversal and keep track of  the previous node
def isBSTUtil(root,prev):
    if root is None:
        return True

    #LEFT   ROOT    RIGHT
    if(root!=None):
        if(isBSTUtil(root.left,prev)):
            return False
        
        #prev is not None and current val<previous  value
        #return False(since inorder is in ascending order)
        if(prev!=None and root.item<=prev.item):
            return False
        
        prev=root #current node becomes previous node
        return (isBSTUtil(root.right,prev))

def isBST(root):
    prev=None   #keeping track of the elements in the inorder traversal
    return isBSTUtil(root,prev)


#CONSTRUCTION PROCESS
root = Node(3)
root.left = Node(2)
root.right = Node(5)
root.right.left = Node(1)
root.right.right = Node(4)

if (isBST(root)):
    print('The Tree is a valid BST')
else:
    print('The tree is not a BST')

