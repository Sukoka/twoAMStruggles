'''
MAXIMUM SUM PATH FROM LEAF TO ROOT
1. IDENTIFY THE MAXIMUM SUM FROM ROOT TO EVERY EXISTING LEAF
2. PICK THE LARGEST SUM AND THEN CONFIGURE THE PATH
'''
class Node:
    def __init__(self,item):
        self.item=item
        self.left=None
        self.right=None

max_Sum=0
target_Leaf=None

def getTargetLeafPath(root,target_leaf):
    if root is None:
        return False

    #if either of root itself || root.left || root.right equals the target leaf
    if (root==target_Leaf) or getTargetLeafPath(root.left,target_Leaf) or getTargetLeafPath(root.right,target_Leaf):
        #print the fucking path
        print(root.item, end=' ')
        return True
    return False

#LOOKING FOR MAXIMUM SUM PATH FROM ROOT TO EVERY LEAF
def getMaxSum(root,curr_sum):
    global max_Sum
    global target_Leaf

    if root is None:
        return 0

    curr_sum=curr_sum+root.item
    #if it reaches the leaf node
    if (root.left==None and root.right==None):
        if(curr_sum>max_Sum):
            max_Sum=curr_sum
            target_Leaf=root
    else:
        getMaxSum(root.left,curr_sum)
        getMaxSum(root.right,curr_sum)

def getMax(root):
    global max_Sum
    global target_Leaf

    if root is None:
        return 0

    max_Sum=-999999
    target_Leaf=None

    #func: for maximum sum path
    getMaxSum(root,0)

    #configuring the exact sum path
    getTargetLeafPath(root,target_Leaf)

    return max_Sum
 
root=Node(5)
root.left=Node(3)
root.right=Node(7)
root.left.left=Node(2)
root.left.right=Node(4)
root.right.right=Node(8)

sum=getMax(root)
print('\nMax sum is:', sum)