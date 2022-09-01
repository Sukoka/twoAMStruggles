'''
CHECK IF GIVEN BINARY TREE IS A HEAP OR NOT
1.IT MUST BE A COMPLETE BINARY TREE
2. CONSIDERING IT AS A MAX-HEAP==>THE NODE MUST BE GREATER THAN ITS CHILD NODES
'''
class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

    def CountNum(self,root):
        if root is None:
            return 0
        else:
            return 1+self.CountNum(root.left)+self.CountNum(root.right)

    def isComplete(self,root,i,count):
        if root is None:
            return True
        if i>=count:
            return False
        return(self.isComplete(root.left,2*i+1,count) and self.isComplete(root.right,2*i+2,count))

    def heap_Property(self,root):
        #no child case
        if root.left is None and root.right is None:
            return True

        #single(left child)case
        if root.right is None:
            return root.val>=root.left.val  #current must be > than left

        else:   #both children case
            if(root.val>=root.left.val and root.val>=root.right.val):
                return (self.heap_Property(root.left) and self.heap_Property(root.right))
            else:
                return False    #since it is a maxHeap

    def checkHeap(self):
        count=self.CountNum(self)
        if((self.isComplete(self,0,count) and self.heap_Property(self))):
            return True
        else:
            return False

root=Node(5)
root.left=Node(4)
root.right=Node(3)
root.left.left=Node(2)

if root.checkHeap():
    print('Heap')
else:
    print('Not a Heap')