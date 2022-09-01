'''
LONGEST PATH FROM LEAF TO LEAF
'''
class Node:
    def __init__(self,item):
        self.item=item
        self.left=None
        self.right=None


def height(root):
    global k,lh,rh,ans
    if root is None:
        return 0

    left=height(root.left)
    right=height(root.right)
    if(ans<left+right+1):
        ans=left+right+1
        k=root
        lh=left
        rh=right

    return 1+max(left,right)

def diameter(root):
    global k,lh,rh,ans,pathlen,f
    if root is None:
        return 0
    
    h=height(root)
    lPath=[0 for i in range(100)]
    configPath(k.left,lPath,0,lh)
    print(root.item,end=' ')

    f=1
    rPath=[0 for i in range(100)]
    configPath(k.right,rPath,0,rh)
    

#configuring all elements along the path
def configPath(root,pathArr,pathlen,len):
    global f
    if root is None:
        return 
    #initializing the array with respective path (left|right)
    pathArr[pathlen]=root.item
    pathlen=+1

    #leaf node situation
    if (root.left==None and root.right==None):
        if (pathlen==len and (f==0 or f==1)):
            printPath(pathArr,len,f)
            f=2
    else:
        configPath(root.left,pathArr,pathlen,len)
        configPath(root.right,pathArr,pathlen,len)

    

def printPath(pathArr,len,f):
    if f==0:    #left
        for i in range(len-1,-1,-1):    #reverse since elements are stored from the root for  the left path
            print(pathArr[i],end=' ')
    elif f==1:
        for i in range(len):
            print(pathArr[i],end=' ')


if __name__ == '__main__':
    k,lh,rh,ans,pathlen,f=None,0,0,0-10*19,0,0

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


