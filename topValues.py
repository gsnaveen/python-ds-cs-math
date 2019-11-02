import heapq
val = [1,2,3,4,5,6,7,8,9]
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
