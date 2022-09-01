'''
PRINT THE LONGEST PATH FROM THE LEAF TO LEAF
'''
class Node:
    def __init__(self,item):
        self.item=item
        self.left=None
        self.right=None

#height lheight rheight diameter
def height(root):
    global k,dia,lh,rh
    if root is None:
        return 0

    leftH=height(root.left)
    rightH=height(root.right)

    #setting the diameter
    if (dia<leftH+rightH+1):
        dia=leftH+rightH+1
        k=root
        lh=leftH
        rh=rightH

    return max(leftH,rightH)+1

def realPrint(arr,len,f):

    if f==0: #print the left side but in reverse(cuz it's stored from the root)
        for i in range(len-1,-1,-1):
            print(arr[i], end=' ')

    elif (f==1):
        for i in range(len):
            print(arr[i], end=' ')


def printPath(root,path,height,pathlen):
    global f
    if root is None:
        return 0

    path[pathlen]=root.item
    pathlen=+1

    #if you reach the leaf==> figure the path that leads to it
    if(root.left==None and root.right==None):
        #path len equals height of either of the subtrees and the flag is either of the right or left
        if (pathlen==height and (f==0 or f==1)):
            realPrint(path,height,f)
            f=2

    #haven't reached leaf yet
    else:
        printPath(root.left,path,height,pathlen)
        printPath(root.right,path,height,pathlen)

def diameter(root):
    global k,lh,rh,f,pathlen,dia
    if root is None:
        return 0

    h=height(root)
    #array to store the path of the leaf to root in the left side
    lPath=[0 for i in range(100)]
    printPath(k.left,lPath,lh,0)
    print(k.item, end=' ')

    rPath=[0 for i in range(100)]
    f=1  #print rPath if flag is  1
    printPath(k.right,rPath,rh,0)

'''
k as root
lh and rh as height
flag being flag
dia as diameter
'''

k,lh,rh,f,pathlen= None,0,0,0,0
dia=0-10**19
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.left = Node(6)
root.left.right.right = Node(7)
root.left.left.right = Node(8)
root.left.left.right.left = Node(9)
 
diameter(root)