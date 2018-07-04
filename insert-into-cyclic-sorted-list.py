class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class Solution:
    def insertValue(self,Node,ToInsert):
        while Node.next:
            if ToInsert.val > Node.val and ToInsert.val < Node.next.val:
                Node.next,ToInsert.next = ToInsert, Node.next
                break
        return Node
                
if __name__ == '__main__':
    #creating a Cyclic linklist
    a = Node(1)
    a.next = Node(3)
    a.next.next = Node(4)  
    a.next.next.next = a
    
    a = Solution().insertValue(a,Node(2))
    counter = 0
    
    while a.next:
        if a.val == 1 :
            counter += 1
            if counter == 2 : break
        print(a.val)
        a = a.next
