'''
KTH SMALLEST ELEMENT IN A BINARY SEARCH TREE WITH O(N) SPACE AND TIME COMPLEXITY
//SPACE CAN BE OPTIMIZED TO O(1) USING MORRIS TRAVERSAL
//ALSO THERE'S A 0(H) TIME COMPLEXITY SOLUTION
'''
class Node:
    def __init__(self, item):
        self.item= item
        self.left=None
        self.right=None

def kthSmallest(root):
    global k
    if root is None:
        return None
    
    left=kthSmallest(root.left)
    if left!=None:
        return left
    
    #decrement k and check if k-1==0
    #if you get back to the root
    k-=1
    if k==0:
        return root
    
    return kthSmallest(root.right)

def output(root,k):
    count=0
    result=kthSmallest(root)
    if result:
        print(f"{k}th smallest element is {result.item}")
    else:
        print(f"{k}th smallest element is not found")


root = Node(15)
root.left = Node(10)
root.right = Node(20)
root.left.left = Node(8)
root.left.right = Node(12)
root.right.left = Node(16)
root.right.right = Node(25)

k=3
result=output(root,k)


