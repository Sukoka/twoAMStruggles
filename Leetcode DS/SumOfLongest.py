'''
SUM OF THE LONGEST PATH FROM ROOT TO LEAF NODE
IF SAME LENGTH==>TAKE THE BIGGER SUM
'''
class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def findRealSum(root,sum,len,maxlen,maxSum):
    if not root:
        if(maxlen[0]<len):
            maxlen[0]=len
            maxSum[0]=sum
        elif(maxlen[0]==len and maxSum[0]<sum):
            maxSum[0]=sum
        return

    findRealSum(root.left, sum+ root.val, len+1, maxlen, maxSum)

    findRealSum(root.right, sum+ root.val, len+1, maxlen, maxSum)


def findSum(root):
    if root is None:
        return 0
    
    maxLen=[0]
    maxSum=[-999999999999]

    findRealSum(root,0,0,maxLen,maxSum)

    return maxSum[0]

root=Node(4)
root.left=Node(2)
root.right=Node(5)
root.left.left=Node(7)
root.left.right=Node(1)
root.right.left=Node(2)
root.right.right=Node(3)
root.left.right.left=Node(6)

sum=findSum(root)
print(sum)