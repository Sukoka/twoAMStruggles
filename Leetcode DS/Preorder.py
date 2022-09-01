'''
ITERATIVE PREORDER TRAVERSAL
'''
class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def iterative(root):
    if root is None:
        return None

    stack=[]
    stack.append(root)
    while (len(stack)!=0):
        node=stack.pop()
        print(node.val)

        #put right first so that left can be on top of the stack
        if (node.right!=None):
            stack.append(node.right)
        if (node.left!=None):
            stack.append(node.left)

root=Node(10)
root.left=Node(8)
root.left.left=Node(3)
root.left.right=Node(5)
root.right=Node(2)
root.right.left=Node(2)

iterative(root)