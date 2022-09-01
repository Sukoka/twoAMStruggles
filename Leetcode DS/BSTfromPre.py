'''
CONSTRUCT BST FROM THE PREORDER SEQUENCE
TIME COMPLEXITY 0(N) METHOD
#SETTING THE RANGE IN WHICH 
# [-INFINITY, ROOT] LEFT
# [ROOT, + INFINITY] RIGHT
'''

#a way to represent infinity as an integer
#python allows float to represent infinity
max= float('inf')
min= float('-inf')

class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

#get the current pointer
def getPreIndex():
    return constructBSTree.preIndex

def updatePreIndex():
    constructBSTree.preIndex+=1
    
def constructBSTree(arr, key, min, max, n):
    if getPreIndex()>=n:
        return None

    root = None
    if key>min and key<max:
        #set the first element as the root node
        root= Node(key)
        #move the fucking pointer
        updatePreIndex()

        if getPreIndex()< n:
            #construct the left with nodes which fall between [-INFINITY, ROOT]

            #arr, root as the second element
            #start=min, end=the current root,
            #size n
            root.left=constructBSTree(arr, arr[getPreIndex()],min,key,n)

        if getPreIndex()< n:
            #construct the right with nodes from
            #[ROOT, + INFINITY]
            root.right=constructBSTree(arr, arr[getPreIndex()],key,max,n)
    return root

def constructBST(arr):
    constructBSTree.preIndex=0  #kinda like a pointer
    n= len(arr)
    return constructBSTree(arr,arr[0],min, max, n)

def inorder(root):
    if root:
        inorder(root.left)
        print(str(root.val))
        inorder(root.right)

arr=[15,10,8,12,20,16,25]
root=constructBST(arr)
print('Inorder Output')
inorder(root)
