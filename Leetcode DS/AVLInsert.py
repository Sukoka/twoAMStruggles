'''
AVl Insertion
1. Perform old fashion bst insertion
2. Update the height of the tree
3. keep track of balanced factor
3. if imbalanced==> rotations
'''




class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        self.height=1

#avl tree that will use the constructor of treeNode
class AVLTree:

    def insert(self, root, key):
        #1. Build the tree recursively
        if root is None:
            return TreeNode(key)
        elif key<root.val:
            root.left=self.insert(root.left, key)
        else:
            root.right=self.insert(root.right,key)

        #update the height
        #max from left or right plus 1 makes up the height
        root.height= 1+ max(self.height(root.left),self.height(root.right))

        #Balancing the tree
        balance=self.balance(root)

        #LL imbalance
        if balance>1 and key<root.left.val:
            return self.rightRotation(root)

        #RR imbalance:
        if balance<-1 and key>root.right.val:
            return self.leftRotation(root)

        #LR imbalance:
        if balance>1 and key>root.left.val:
            root.left= self.rightRotation(root.left)
            return self.leftRotation(root)

        #RL imbalance:
        if balance<-1 and key<root.right.val:
            root.right= self.leftRotation(root.right)
            return self.rightRotation(root)

        return root
  
    def height(self,root):
        if root is None:
            return 0
        return root.height


    def balance(self,root):
        #balance=height of lStree-height of rStree
        if root is None:
            return 0   
            #mark that this is an integer type
            #so return 0 not None

        return self.height(root.left)-self.height(root.right)

    def leftRotation(self,z):
        #RR and RL imbalance needs leftRotation
        y=z.right
        t1=y.left #RL situation

        #Rotation
        y.left=z
        z.right=t1

        #update the height
        z.height= 1+max(self.height(z.left),self.height(z.right))
        y.height= 1+max(self.height(y.left),self.height(y.right))

        return y

    def rightRotation(self,z):
        #LL and LR imbalance needs RightRotation
        y=z.left
        t2=y.right  #LR situation

        #rotation
        y.right=z
        z.left= t2

        #update the height
        z.height= 1+max(self.height(z.left),self.height(z.right))
        y.height= 1+max(self.height(y.left),self.height(y.right))

        return y

    


    def preorder(self, root):
        if root is None:
            return None
        print(str(root.val))
        self.preorder(root.left)
        self.preorder(root.right)



avlTree= AVLTree()
root= None
root= avlTree.insert(root,10)
root= avlTree.insert(root,20)
root= avlTree.insert(root,30)
root= avlTree.insert(root,40)
root= avlTree.insert(root,50)
root= avlTree.insert(root,60)

print('Preorder fashion')
avlTree.preorder(root)