from collections import defaultdict

class solution():
	clone = defaultdict(list)

	def __init__(self):
		self.graph = defaultdict(list)

	def addedge(self,v,d):
		self.graph[v].append(d)
		if d not in self.graph.keys():
			self.graph[d]

	def clonegraph(self):

		
		for node in self.graph.keys():

			if node not in self.clone.keys():
				self.clone[node]

			for neighbour in self.graph[node]:
				if neighbour not in self.clone.keys():
					self.clone[neighbour]
				self.clone[node].append(neighbour)

		print(self.clone)



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
	# print(a.graph)
	a.clonegraph()

	#['b', 'd', 'a', 'c', 'e', 'h', 'f', 'g']
