'''
INORDER TRAVERSAL USING MORRIS TRAVERSAL
//WITHOUT RECURSION OR THE USE OF STACK
//TIME COMPLEXITY O(N)
//SPACE COMPLEXITY O(1) CUZ IT DOESN'T STORE THE ELEMENT BY CREATING VIRTUAL LINKS
//INSPIRED BY THREADED BINARY TREE

//ALGORITHM//
current=root
while (cur!=None):
    if cur.left==None:
        print current
        cur= current.right
    else:
        predecessor=findPredecessor(current)
        if predecessor.right==None:
            predecessor.right=current
            cur=cur.left
        else: #its not none and is equal to cur
            pre.right=None
            print current
            cur=cur.right

'''
class Node:
    def __init__(self, item):
        self.item= item
        self.left=None
        self.right=None


def Morris(root):
    #let the current as root
    cur=root
    #no left child==>print the curr and set the cur to right of cur
    while (cur!=None):
        if cur.left==None:
            yield cur.item  #basically the leftmost element
            cur=cur.right   #the parent of this child
        #there exists left subtree
        else:   
            predecessor=cur.left   
            while predecessor.right!=None and predecessor.right!=cur:
                predecessor=predecessor.right
            if predecessor.right==None:
                #creating the virtual link
                predecessor.right=cur
                cur=cur.left
            #if predecessor.righht==curr==> delete the virtual link
            else:
                predecessor.right=None  #delete
                yield cur.item   #print cur val
                cur=cur.right

#construction process
root = Node(15)
root.left = Node(10)
root.right = Node(20)
root.left.left = Node(8)
root.left.right = Node(12)
root.right.left = Node(16)
root.right.right = Node(25)

print('Inorder traversal using Morris')
for m in Morris(root):
    print(m)