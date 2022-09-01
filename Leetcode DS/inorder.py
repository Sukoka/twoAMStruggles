''' inorder successor/predecessor'''
'''
STEPS
1. BUILD THE BST
2. IF KEY IS FOUND  
    A. LEFT EXISTS=LEFT PREDECESSOR/ RIGHT OF LEFT PRE
    B. RIGHT EXISTS= RIGHT SUCCESSOR/ LEFT OF RIGHT SUCCESSOR
3. KEY < ROOT
    ROOT AS A SUCESSOR
    LOOK FOR THE LEFT SIDE
4. KEY > ROOT
    ROOT AS A PREDECESSOR
    LOOK FOR THE RIGHT SIDE
'''

class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

#BUILD THE MF
def insert(root,item):
    if root is None:
        return Node(item)
    else:
        if item<root.val:
            root.left= insert(root.left, item)
        elif item>root.val:
            root.right= insert(root.right, item)
    return root

def findPreSuc(root, key):
    #empty case
    if root is None:
        return root

    #found case (the key is included in the tree i guess)
    if root.val==key:
        #predecessor==> max in the left subtree
        if root.left is not None:
            #left child itself could be predecessor
            tmp= root.left
            #if that left child's got right child, that's it
            while(tmp.right):
                tmp= tmp.right
            findPreSuc.pre=tmp

        #successor which is the min child in right subtree
        elif root.right is not None:
            #right child itself could be the successor
            tmp=root.right
            #if she's got a left child, then that's the one
            while(tmp.left):
                tmp=tmp.left
            findPreSuc.suc=tmp

    #the key is not inside the tree but you can squeeze it in in inorder
    if key<root.val:
        #let root as a successor
        findPreSuc.suc= root
        findPreSuc(root.left, key)
    else:
        #if key>root.val go for the right side
        #let root as predecessor
        findPreSuc.pre=root
        findPreSuc(root.right, key)

    



root=Node(50)
insert(root,30)
insert(root,70)
insert(root,20)
insert(root,40)
insert(root,60)
insert(root,80)

#idk the static variable for findPreSuc func:
findPreSuc.pre=None
findPreSuc.suc=None

key=93

findPreSuc(root,key)


if findPreSuc.pre is not None:
    print('Predecessor of the', key , 'is', findPreSuc.pre.val)
else:
    print('No predecessor, which means the key is the leftmost node')

if findPreSuc.suc is not None:
    print('Successor of the', key, 'is', findPreSuc.suc.val)
else:
    print('No succesor, which means the key is  the rightmost node')
    

        