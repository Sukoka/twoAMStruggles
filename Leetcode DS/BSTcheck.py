'''
CHECK IF GIVEN INORDER,PREORDER AND POSTORDER ARE OF THE SAME BINARY TREE
ALGO++++
1.BUILD BINARY TREE FROM TWO OF THE TRAVERSALS
2. TRAVERSE THE CONSTRUCTED TREE WITH THE REMAINING ORDER AND MATCH IT WITH THE GIVEN ORDER
'''
class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

preIndex=0

def search(inOrder,tNode,str,end):
    for i in range(str,end+1):
        if tNode.val==inOrder[i]:
            return i


def buildBT(inOrder,preOrder,str,end):
    global preIndex
    if str>end:
        return None

    tNode=Node(preOrder[preIndex])
    preIndex += 1
    if str==end:    #no child case
        return tNode
    
    inIndex=search(inOrder,tNode,str,end)

    tNode.left=buildBT(inOrder,preOrder,str,inIndex-1)
    tNode.right=buildBT(inOrder,preOrder,inIndex+1,end)

    return tNode

def checkPostOrder(root,postOrder,index):
    #Left Right Root
    if root is None:
        return index

    index=checkPostOrder(root.left,postOrder,index) #Left
    index=checkPostOrder(root.right,postOrder,index)

    if root.val==postOrder[index]:
        index+=1
    else:
        return -1
    
    return index

#Given orders 
inOrder = [4, 2, 5, 1, 3]
preOrder = [1, 2, 4, 5, 3]
postOrder = [4, 5, 2, 3, 1]

n=len(inOrder)
root=buildBT(inOrder,preOrder,0,n-1)

#check if the constructed post order is equal to the given postOrder
index=checkPostOrder(root,postOrder,0)
if index==n:
    print('Traversal of the same tree')
else:
    print('Different Tree')