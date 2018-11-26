class Node():

	def __init__ (self,value):
		self.data = value
		self.left = None
		self.right = None


def paths(node,path,container):

	if node:
		if path == "":
			path = str(node.data)
		else:
			path += "->" + str(node.data)
	else:
		container.add(path)
		return

	paths(node.left,path,container)
	paths(node.right,path,container)
	
def paths2(node,path,container):

	if node:
		if path == "":
			path = str(node.data)
		else:
			path += "->" + str(node.data)

	if node.left == None and node.right == None:
		container.append(path)
	else:
		if node.left: paths2(node.left,path,container)
		if node.right: paths2(node.right,path,container)




if __name__ == '__main__':

	a = Node(10)
	a.left = Node(9)
	a.left.left = Node(7)
	a.left.right = Node(22)
	a.right = Node(11)
	a.right.left = Node(110)
	a.right.right = Node(111)

#Using a set
	container = set()
	paths(a,"",container)
	print(container)
  
 #Using a list
	container = []
	paths2(a,"",container)
	print(container)
