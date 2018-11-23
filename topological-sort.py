#Python program to print topological sorting of a DAG
from collections import defaultdict

class solution():

	def __init__(self):
		self.graph = defaultdict(list)

	def addedge(self,v,d):
		self.graph[v].append(d)
		if d not in self.graph.keys():
			self.graph[d]


	def topologicalsort(self):

		visited = {}
		stack = []

		for key in self.graph.keys():
			visited[key] = False

		print(visited)
		print(self.graph)

		for key in self.graph.keys():

			if visited[key] == False:
				self.checkconected(key,visited,stack)

		return stack

	def checkconected(self,key,visited,stack):
		visited[key] = True

		for connected in self.graph[key]:
			if visited[connected] == False:
				self.checkconected(connected,visited,stack)

		stack.insert(0,key)





if __name__ == '__main__':
	
	a = solution()

	a.addedge('a','c')
	a.addedge('b','c')
	a.addedge('b','d')
	a.addedge('c','e')
	a.addedge('e','h')
	a.addedge('e','f')
	a.addedge('d','f')
	# a.addedge('e','h')
	a.addedge('f','g')			
	print(a.topologicalsort())

	#['b', 'd', 'a', 'c', 'e', 'h', 'f', 'g']
