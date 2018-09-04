# Python program to detect cycle in a graph
from collections import defaultdict
 
class Graph():
    def __init__(self):
        self.graph = defaultdict(list)
        self.nodes = set()
 
    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.nodes.add(u)
        self.nodes.add(v)
        
    def isCycleUtil(self,node,visited,recursed):
        
        visited[node] = True
        recursed[node] = True
        
        for neg in self.graph[node]:
            if visited[neg] == False:
                if self.isCycleUtil(neg,visited,recursed) == True:
                    return True
            elif recursed[neg] == True:
                return True
        
        recursed[node] = False
        return False
   
    
    
    def isCyclic(self):
        
        visited = dict(zip(self.nodes, [False] * len(self.nodes)))
        recursed = dict(zip(self.nodes, [False] * len(self.nodes)))
        
        for node in self.nodes:
             if visited[node] == False:
                if self.isCycleUtil(node,visited,recursed) == True:
                    return True
                
        return False
                
g = Graph()
g.addEdge("a","b")
g.addEdge("a","c")
g.addEdge("c","d")
g.addEdge("c","e")
g.addEdge("b","bb")
g.addEdge("b","bbb")
g.addEdge("b","a")
 
if g.isCyclic() == 1:
    print("Graph has a cycle")
else:
    print("Graph has no cycle")
