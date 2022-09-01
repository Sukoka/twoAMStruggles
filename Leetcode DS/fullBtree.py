'''
CHECK IF A BINARY TREE IS A FULL BINARY TREE OR NOT
FULL BINARY TREE PROPERTIES
1. ZERO OR TWO CHILDRE
'''
class Node:
    #build this shit
    def __init__(self,item):
        self.left= None
        self.right= None
        self.val=item

def isFullBtree(root):
    #tree empty case
    if root is None:
        return True

    #left no child, right no child
    if root.left is None and root.right is None:
        return True
    
    #either or both sides have child
    if root.left is not None and root.right is not None:
        return(isFullBtree(root.left) and isFullBtree(root.right))
    return False


root= Node('A')
root.left= Node('B')
root.right= Node('C')
root.left.left= Node('D')
root.left.right= Node('E')
root.right.left= Node('F')
root.right.right= Node('G')

if isFullBtree(root):
    print('This is a full binary tree yayyy')
else:
    print('This is not a full binary tree')
