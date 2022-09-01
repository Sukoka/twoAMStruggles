class Node:
    def __init__(self,key):
        self.val=key
        self.left=None
        self.right= None
    
def insert(root,key):
    if root is None:
        #if there is no root make the key as root
        return Node(key)
    else:
        if root.val==key:
            return root
        elif root.val<key:
            root.right=insert(root.right, key)
        else:
            root.left=insert(root.left, key)
    return root        

def search(root,key):
    if root.val==key or root is None:
        return root
    else:
        if root.val<key:
            #search at right
            return search(root.right,key)
        else:
            return search(root.left, key)

def inorder(root):
    if root:
        inorder(root.left)
        print(str(root.val),'->', end=' ')
        inorder(root.right)

def minVal(root):
    current=root
    if current.left is not None:
        current=current.left
    return current        
    
def delete(root,key):
    if root is None:
        return root
    
    if root.val<key:
        root.right=delete(root.right, key)
    #you need to write the condition for elif pattern
    elif root.val>key:
        root.left=delete(root.left, key)
    #root.val==key(this is the key to be deleted)
    else:
        #one child or no child case
        if root.left is None:
            temp=root.right
            root=None
            return temp
        if root.right is None:
            temp=root.left
            root=None
            return temp

        #two children case
        #look for the min child in right  subchild(inorder successor)
        #or search for the max child in the left subtree(inorder predecessor)
        temp=minVal(root.right)

        #copy the temp value to the node to be deleted
        root.val=temp.val

        #delete the duplicated shit which is the temp value
        #go for root right since you have searched for the right  side (right child of the root being he parent and the key is the duplicant)
        root.right=delete(root.right, temp.val)
    return root


root=Node(50)
root=insert(root, 30)
root=insert(root, 70)
root=insert(root, 20)
root=insert(root, 40)
root=insert(root,60)
root=insert(root, 80)

print('In inorder fashion')
inorder(root)

print('\nSearching 40')
search(root, 40)

print('\nDeleting 20')
delete(root, 20)
print('Output in inorder fashion')
inorder(root)

print('\nDeleting 30')
delete(root, 30)
print('Output in inorder fashion')
inorder(root)

print('\nDeleting 50')
delete(root, 50)
print('Output in inorder fashion')
inorder(root)


        


        