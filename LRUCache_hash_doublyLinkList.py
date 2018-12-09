#Node with key and data to cache
#value = FileName
#dataValue = object that needs to be cached.
import logging
from datetime import datetime

class Node():
	def __init__(self,value,dataValue):
		self.value = value
		self.data = dataValue
		self.head = None
		self.tail = None

class Network():
	fileSystem = { 1:1111,
					2:2222,
					3:3333,
					4:4444,
					5:5555,
					6:6666,
					7:7777,
					8:8888,
					9:9999,
					10:10101010
	}

#Doubly linklist 
class doublylinklist():
	dll_head = None
	dll_tail = None
	cacheKey = {}
	currentCacheSize = 0

	def __init__(self,size):

		self.cacheSize = size
		self.network = Network()

	def getItem(self,item):
		#Check if item exist in the cache
		cache = self.cacheKey.get(item,None)

		if not cache:
			# If not then fetch the item and add
			cache = self.fetchItem(item)
			self.additem(item,cache)
		else:
			logging.info("Cache Served " + str(cache.value) + " - " + str(cache.data))
			self.touch(item)

		return cache

	def fetchItem(self,item):
		#Fetching data from the netowrk drive
		return self.network.fileSystem[item]


	def additem(self, value,dataValue):
		# for determining if cache needs to be cleared
		if 	self.currentCacheSize >= self.cacheSize:
			self.droptail()
			self.additemtoCache(value,dataValue)
		else:
			self.additemtoCache(value,dataValue)
			self.currentCacheSize += 1	

	def additemtoCache(self,value,dataValue):
		node = Node(value,dataValue)
		self.cacheKey[value] = node
		if not self.dll_head:
			self.dll_head = self.dll_tail = node
			self.dll_head.tail =  self.dll_tail
			self.dll_tail.head = self.dll_head
			self.dll_head.head = None
		else:
			node.tail = self.dll_head
			self.dll_head.head = node
			self.dll_head = node

	def touch(self,value):
		# print(value)
		node = self.cacheKey[value]
		# print(node.value,node.data)

		if node == self.dll_head:
			pass
		elif node == self.dll_tail:

			node.head.tail = None
			self.dll_tail = node.head

			self.dll_head.head = node
			node.tail = self.dll_head
			node.head = None
			self.dll_head = node
			pass
		else:
			node.head.tail, node.tail.head = node.tail, node.head
			node.head = None
			self.dll_head.head = node
			node.tail = self.dll_head
			self.dll_head = node

	def remove(self,value):
		# deleteing any in between values
		node = self.cacheKey[value]
		node.head.tail, node.tail.head = node.tail, node.head
		del self.cacheKey[value]
		# self.cacheKey.pop(value,'None')

	def droptail(self):
		#Dropping the tail for clearng space for new data
		value = self.dll_tail.value
		logging.info("drop tail " + "- "+ str(value))
		node = self.cacheKey[value]
		node.head.tail = None
		self.dll_tail = node.head
		del self.cacheKey[value]

	def printfromHead(self):
		tracker = self.dll_head
		while  tracker:
			print(tracker.value,tracker.data)
			tracker = tracker.tail

	def printfromTail(self):
		tracker = self.dll_tail
		while tracker:
			print(tracker.value,tracker.data)
			tracker = tracker.head

if __name__ == '__main__':

	logFileName = "LRUCache"+"_"+datetime.now().strftime("%Y-%m-%d--%H-%M") +".log"
	logging.basicConfig(filename=logFileName,level=logging.INFO)

	dll = doublylinklist(5)
	dll.getItem(1);	dll.getItem(2);	dll.getItem(3);	dll.getItem(3)
	dll.getItem(4);	dll.getItem(5);	dll.getItem(6);	dll.getItem(7)
	dll.getItem(3);	dll.getItem(1)	
	# print(dll.cacheKey)
	print("from Head")
	dll.printfromHead()
	print("from tail")
	dll.printfromTail()
