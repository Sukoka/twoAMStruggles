'''
PREORDER USING MORRIS TRAVERSAL
//ALGO ALMOST THE SAME AS INORDER
'''
class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def Morris(root):
    current=root
    while current is not None:
        if current.left==None:
            yield current.val
            current=current.right
        else:
            predecessor=current.left
            if predecessor.right!=None and predecessor.right!=current:
                predecessor=predecessor.right

            #already has a link and is pointing to the current
            if predecessor.right==current:
                predecessor.right=None  #delete the virtual link
                current=current.right

            #doesn't have a link and pre.right is null
            else:
                predecessor.right=current   
                #creating a virtual link with the pre to the current
                yield current.val   #root
                current=current.left    #left cuz preorder

root=Node('A')
root.left=Node('D')
root.left.left=Node('H')
root.left.right=Node('L')
root.left.right.left=Node('P')
root.right=Node('Z')
root.right.right=Node('C')
root.right.right.right=Node('E')

print('Preorder Traversal using Morris Traversal')
Morris(root)
for m in Morris(root):
    print(m)

