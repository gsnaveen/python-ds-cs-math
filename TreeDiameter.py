class Node():

	def __init__ (self,value):
		self.data = value
		self.left = None
		self.right = None


def diameter(node,level):

	if node: level += 1 

	if node.left and node.right:
		return max(diameter(node.left,level),diameter(node.right,level))
	elif node.left:
		return diameter(node.left,level)
	elif node.right:
		return diameter(node.right,level)

	return level


if __name__ == '__main__':

	b= Node(10)
	b.left = Node(9)
	b.left.left = Node(7)
	b.left.left.left = Node(22)

	a = Node(10)
	a.left = Node(9)
	a.left.left = Node(7)
	a.left.right = Node(22)
	a.right = Node(11)
	a.right.left = Node(110)
	a.right.right = Node(111)
	a.right.right.left = Node(112)
	a.right.right.left.right = Node(113)

	assert diameter(a,0) == 5
	assert diameter(b,0) == 4
