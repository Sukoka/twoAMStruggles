'''
FIND IF THERE'S A PAIR FROM ROOT TO LEAF PATH WHOSE SUM EQUALS THE ROOT'S DATA
'''
class newnode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def findPair(curr,s,root_val):
    if curr is None:
        return False

    val=root_val-curr.val
    if val in s:
        return True
    
    s.add(curr.val)
    
    ans= findPair(curr.left,s,root_val) or findPair(curr.right,s,root_val)
    s.remove(curr.val)
    return ans
    

def isPair(root):
    s=set() #create an empty set
    return findPair(root.left,s,root.val) or findPair(root.right,s,root.val)

root = newnode(8)
root.left = newnode(5)
root.right = newnode(4)
root.left.left = newnode(9)
root.left.right = newnode(7)
root.left.right.left = newnode(1)
root.left.right.right = newnode(12)
root.left.right.right.right = newnode(2)
root.right.right = newnode(11)
root.right.right.left = newnode(3)

print('YASS there\'s a pair') if (isPair(root)) else print('NOO')