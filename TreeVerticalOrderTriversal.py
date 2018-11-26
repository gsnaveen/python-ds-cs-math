from collections import defaultdict

class Node():

	def __init__ (self,value):
		self.data = value
		self.left = None
		self.right = None


def vertical(node,level,data):

	if node:
		data[level].append(node.data)

	if node.left:
		vertical(node.left,level -1 ,data)

	if node.right:
		vertical(node.right,level +1 ,data)


if __name__ == '__main__':
	 #  	1
     #    /    \
     #   2      3
     #  / \    / \
     # 4   5  6   7
     #         \   \
     #          8   9 

	a = Node(1)
	a.left = Node(2)
	a.left.left = Node(4)
	a.left.right = Node(5)
	a.right = Node(3)
	a.right.left = Node(6)
	a.right.left.right = Node(8)
	# a.right.left.right.right = Node(88)
	a.right.right = Node(7)
	a.right.right.right = Node(9)

	data = defaultdict(list)
	vertical(a,0,data)
	for key in sorted(data.keys()):
		print(data[key])

# 4
# 2
# 1 5 6
# 3 8
# 7
# 9 
