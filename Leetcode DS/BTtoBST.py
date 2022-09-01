'''
Binary tree to BST
'''
class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

#function to store the inorder traversal of the binary tree
def storeInorder(root,inorder):
    if root is None:
        return
    #left root right
    storeInorder(root.left, inorder)#LEFT
    inorder.append(root.val)#ROOT (INORDER AS THE ARRAY)
    storeInorder(root.right,inorder)

#function to know the number of nodes
def countNum(root):
    if root is None:
        return 0
    return countNum(root.left)+countNum(root.right)+1

def printInorder(root):
    if root is None:
        return
    printInorder(root.left)
    print(str(root.val))
    printInorder(root.right)

#function to convert the sorted array into a BST
def arrToBST(root,arr):
    if root is None:
        return
    
    arrToBST(root.left,arr) #update the left subtree first
    root.val=arr[0]
    arr.pop(0)
    arrToBST(root.right,arr)

def binarytreeToBST(root):
    if root is None:
        return
    n=countNum(root)
    arr=[]  #array to store the inorder of the binary tree
    storeInorder(root,arr)
    arr.sort()  #sort the fucking array which is in inorder fashion
    arrToBST(root,arr)


#tree construction
root=Node(10)
root.left=Node(30)
root.right=Node(15)
root.left.left=Node(20)
root.right.right=Node(5)

binarytreeToBST(root)
print('Output BST in inorder')
printInorder(root)

