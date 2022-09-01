'''
Construct Bst from given preorder and inorder 
1. The first element of preorder is the fucking root
2. Look for that element in the inorder array
3. Mark that position and make elements to the left as the left subtree and those in the right the right subtree
'''

class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

#where the work is done
def buildTree(preorder,inorder,start,end):
    if start>end:
        return None

    #set the root as the first element of preorder
    root=Node(preorder[buildTree.preIndex])
    buildTree.preIndex=+1   #increment the index

    #no children case
    if start==end:
        return root

    #looking for that element from preorder in inorder array
    inIndex= searchinIndex(inorder,start,end,root.val)
    

    #construct the left and right recursively
    endleft=inIndex-1
    startright=inIndex+1

    root.left=buildTree(preorder,inorder,start,endleft)
    root.right=buildTree(preorder,inorder,startright,end)

    return root



def searchinIndex(inorder,start,end,data):
    for i in range(start,end+1):
        if inorder[i]==data:
            return i


def printInorder(root):
    if root is None:
        return 

    #left=>root=>right
    printInorder(root.left)
    print(str(root.val))
    printInorder(root.right)



#how you point the preorder elements
buildTree.preIndex=0
preorder=[1,2,4,3,5,7,8,6]
inorder=[4,2,1,3,5,8,3,6]
n=len(inorder)-1

root= buildTree(preorder,inorder,0,n)

print("Output in Inorder fashion")
printInorder(root)


        