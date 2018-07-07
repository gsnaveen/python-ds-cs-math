#Python program to print topological sorting of a DAG
from collections import defaultdict
class Graph(object):
    def __init__(self,V):
        self.graph = defaultdict(list)
        self.vertices = V
    
    def addedge(self,v,t):
        self.graph[v].append(t)
    
    def gettopologicalSortUtil(self,v,visited,stack):
            visited[v] = True
            for i in self.graph[v]:
                if visited[i] == False:
                    self.gettopologicalSortUtil(i,visited,stack)
            stack.insert(0,v)
            
    def gettopologicalSort(self):
        visited = [False]*self.vertices
        stack = []
        for i in range(self.vertices):
            #print(self.graph[i])
            if visited[i] == False:
                self.gettopologicalSortUtil(i,visited,stack)
        print(stack)

g = Graph(6)
g.addedge(5, 2);
g.addedge(5, 0);
g.addedge(2, 3);
g.addedge(3, 1);
g.addedge(4, 0);
g.addedge(4, 1);
g.vertices
g.gettopologicalSort()   
