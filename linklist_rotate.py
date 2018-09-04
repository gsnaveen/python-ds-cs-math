class ll():
    
    def __init__(self,val):
        self.data = val
        self.next = None

class Solution():
    
    def pll(self,node):
        while node:
            print(node.data)
            node = node.next
            
    def split(self,node, point):
        
        endNode = None
        startNode = node
        nodelast = node
        splitNode = None
        
        while nodelast:
            if nodelast.next != None:
                endNode = nodelast.next
            nodelast = nodelast.next
        
        for i in range(2):
            splitNode = node.next 
        
        node = splitNode.next
        endNode.next = startNode
        splitNode.next = None
            
        return node
    
if __name__ == "__main__":
    
    a = ll(1)
    a.next = ll(2)
    a.next.next = ll(3)
    a.next.next.next = ll(4)
    a.next.next.next.next = ll(5)
    
    sol = Solution()
    
    print("Pre")
    sol.pll(a)
    
    returned = sol.split(a,2)
    
    print("Post")
    sol.pll(returned)
