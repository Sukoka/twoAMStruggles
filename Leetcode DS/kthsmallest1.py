'''
KTH SMALLEST ELEMENT IN A 0(H) TIME COMPLEXITY SOLUTION
//IF IT'S A SKEWED TREE THE COMPLEXITY IS  0(N)
'''
class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        self.Lcount=0


def insert(root,x):
    if root is None:
        return Node(x)
    
    if x<root.val:
        root.left=insert(root.left,x)
        #keep track of the left child each left node possess
        root.Lcount+=1
    elif x>root.val:
        root.right=insert(root.right,x)
    return root

def kthsmallest(root,k):
    if root is None:
        return None
    
    count=root.Lcount+1
    if count==k:
        return root

    #if k<root.Lcount+1
    elif count>k:
        return kthsmallest(root.left,k)
    

    #k-count cuz you skip those unnecessary elements
    return kthsmallest(root.right,k-count)

root=None
keys=[20,8,22,4,12,10,14]
for x in keys:
    root=insert(root,x)

k=4
result=kthsmallest(root,k)
if result!=None:
    print(f"{k}th smallest element is {result.val}")
else:
    print(f"{k}th smallest element is not found")