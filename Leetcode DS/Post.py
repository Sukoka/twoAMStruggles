'''
Find Postorder from given inorder and preorder
'''
def SearchinInorder(inorder,p,size):
    for i in range(size):
        #return the index where root is at in inorder
        if inorder[i]==p:
            return i

def PrintPostOrder(inorder,preorder,n):
    #Left==>right==>root
    root=SearchinInorder(inorder,preorder[0],n)

    #the root has left children
    #LEFT
    if root!=0:
        PrintPostOrder(inorder,preorder[1:n],root)

    #root is not the last element which means root has right children
    #RIGHT
    if root!=n-1:  
        PrintPostOrder(inorder[root+1:n],preorder[root+1:n],n-root-1)

    #ROOT
    print(preorder[0])

inorder=[4,2,5,1,3,6]
preorder=[1,2,4,5,3,6]
n=len(inorder)
PrintPostOrder(inorder,preorder,n)