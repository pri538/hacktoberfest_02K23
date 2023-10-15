# Python program to print boundary traversal of binary tree

# A binary tree node has data, pointer to left child
# and a pointer to right child
class Node:
	def __init__(self, key):
		self.data = key
		self.left = None
		self.right = None


def isLeaf(node):
	if node.left == None and node.right == None:
		return True
	return False


def addLeftBound(root, res):
	# Go left left and no left then right but again check from left
	root = root.left
	while(root is not None):
		if isLeaf(root) is not True:
			res.append(root.data)
		if(root.left is not None):
			root = root.left
		else:
			root = root.right


def addRightBound(root, res):
	# Go right right and no right then left but again check from right
	root = root.right
	# As we need the reverse of this for Anticlockwise
	# refer above picture for better understanding
	stk = []
	while(root is not None):
		if isLeaf(root) is not True:
			stk.append(root.data)
		if root.right is not None:
			root = root.right
		else:
			root = root.left

	while(len(stk) != 0):
		res.append(stk.pop(-1))

		
# its kind of preorder
def addLeaves(root, res):
	if root is None:
		return
	if isLeaf(root) is True:
		res.append(root.data) # just store leaf nodes
		return
	addLeaves(root.left, res)
	addLeaves(root.right, res)


def boundary(root, res):
	# Your code here
	if root is None:
		return
	if isLeaf(root) is not True:
		res.append(root.data) # if leaf then its done by addLeaf
	addLeftBound(root, res)
	addLeaves(root, res)
	addRightBound(root, res)


if __name__ == '__main__':
	root = Node(20)
	root.left = Node(8)
	root.left.left = Node(4)
	root.left.right = Node(12)
	root.left.right.left = Node(10)
	root.left.right.right = Node(14)
	root.right = Node(22)
	root.right.right = Node(25)

	res = []
	boundary(root, res)
	for i in res:
		print(i)

# This code is contributed by Yash Agarwal(yashagarwal2852002)
