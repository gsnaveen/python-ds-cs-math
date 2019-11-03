import heapq
val = [1,2,3,4,5,6,7,8,9]
# tuple based queue
# val = [(1,'a'),(2,'b'),(3,'c'),(4,'d'),(5,'e'),(6,'f'),(7,'g'),(8,'h'),(9,'i')]
myStore = []
myQ = heapq

top = 3
counter = 0
for i in val:
    if counter < top:
        myQ.heappush(myStore,i)
        counter += 1
    else:
        myQ.heappushpop(myStore,i)

else:
    for i in range(top) :
        print(myQ.heappop(myStore))
