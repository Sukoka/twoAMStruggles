'''
FIND THE DIAMETER OF A BINARY TREE
DIAMETER IS THE LARGEST OF
1. D OF RIGHT STREE
2. D OF LEFT STREE
3. LONGEST PATH FROM THE LEAF NODES THROUGH THE ROOT NODE
'''
class Node:
    def __init__(self,item):
        self.item=item
        self.left=None
        self.right=None


def height(root):
    if root is None:
        return 0
    return max(height(root.left),height(root.right))+1

def diameter(root):
    if root is None:
        return 0
    lheight=height(root.left)
    rheight=height(root.right)

    ldia=diameter(root.left)
    rdia=diameter(root.right)

    #check the above properties
    return max(max(ldia,rdia),lheight+rheight+1)


#construction
root=Node(1)
root.left=Node(2)
root.left.left=Node(4)
root.left.right=Node(5)
root.right=Node(3)

d=diameter(root)
print('The diameter is', d)