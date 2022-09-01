'''
KTH SMALLEST ELEMENT IN A BST USING MORRIS TRAVERSAL 
SPACE COMPLEXITY OPTIMIZED TO O(1)
'''
class Node:
    def __init__(self, val):
        self.val= val
        self.left=None
        self.right=None

#kth smallest where u use morris traversal
def kthsmallest(root,k):
    count=0 #keep track of the traversed elements
    kthEle = -9999999999
    curr=root
    while curr is not None:
        if curr.left==None:
            count+=1
            #if count equals the nth element return the val
            if count==k:
                kthEle=curr.val
            curr=curr.right
        else:
            predecessor=curr.left
            if predecessor.right!=None and predecessor.right!=curr:
                predecessor=predecessor.right   #the right of the left
            if predecessor.right==None:
                predecessor.right=curr  #creating the virtual thread
                curr=curr.left
            else:   #if the predecessor.right already connected to the curr
                predecessor.right=None
                count+=1
                if count==k:
                    kthEle=curr.val
                curr=curr.right
    return kthEle
 
def insert(root,k):
    if root is None:
        return Node(k)
    if k<root.val:
        root.left=insert(root.left,k)
    elif k>root.val:
        root.right=insert(root.right,k)

    return root

root=None
keys=[50,30,70,20,40,60,80]
for k in keys:
    root=insert(root,k)

for k in range(1,8):
    print(kthsmallest(root,k))
