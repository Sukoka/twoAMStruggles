# Helper function that allocates a new
# node with the given data and NULL left
# and right pointers.
class newNode:
# Constructor to create a new node
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None


def largestBST(node):
	Min = [999999999999] 
	Max = [-999999999999] 
	max_size = [0] # For size of the largest BST
	is_bst = [0]
	
	largestBSTUtil(node, Min,Max, max_size, is_bst)
	return max_size[0]


#returns size
def largestBSTUtil(node, min_ref, max_ref,
						max_size, is_bst):
	if node == None:
		is_bst[0] = 1 # An empty tree is BST
		return 0 # Size of the BST is 0
	
	Min = 999999999999
	left_flag = False	#bst or not
	right_flag = False
	ls, rs = 0, 0 
	
	#operation for the left subtree	
	max_ref[0] = -999999999999	#max value in the left subtree
	ls = largestBSTUtil(node.left, min_ref, max_ref,
						max_size, is_bst)
						#updates the size
	if is_bst[0] == 1 and node.data > max_ref[0]:
		#check if its bst or not
		left_flag = True
	
	# Before updating min_ref[0], store the min
	# value in left subtree. So that we have the
	# correct minimum value for this subtree
	Min = min_ref[0]
	min_ref[0] = 999999999999
	rs = largestBSTUtil(node.right, min_ref, max_ref,
						max_size, is_bst)
	if is_bst[0] == 1 and node.data < min_ref[0]:
		right_flag = True
	
	# Update min and max values for the
	# parent recursive calls
	if Min < min_ref[0]:
		min_ref[0] = Min
	if node.data < min_ref[0]: # For leaf nodes
		min_ref[0] = node.data
	if node.data > max_ref[0]:
		max_ref[0] = node.data
	
	
	if left_flag and right_flag:
		if ls + rs + 1 > max_size[0]:
			max_size[0] = ls + rs + 1
		return ls + rs + 1
	else:
		return 0

# Driver Code
if __name__ == '__main__':
	
	# Let us construct the following Tree
	#	 50
	# /	 \
	# 10	 60
	# / \	 / \
	# 5 20 55 70
	#		 /	 / \
	#	 45	 65 80
	root = newNode(50)
	root.left	 = newNode(10)
	root.right	 = newNode(60)
	root.left.left = newNode(5)
	root.left.right = newNode(20)
	root.right.left = newNode(55)
	root.right.left.left = newNode(45)
	root.right.right = newNode(70)
	root.right.right.left = newNode(65)
	root.right.right.right = newNode(80)

# The complete tree is not BST as 45 is in
# right subtree of 50. The following subtree
# is the largest BST
#	 60
# / \
# 55	 70
# /	 / \
# 45	 65 80

print("Size of the largest BST is",
				largestBST(root))
				
# This code is contributed by PranchalK
