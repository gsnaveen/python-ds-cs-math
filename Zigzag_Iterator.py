myinput = [
    [1,2,3],
    [4,5,6,7],
    [8,9],
    [10,11,12,13]
    
          ]
start = 0
myOutput = []

myLenList = []
for i in myinput:myLenList.append(len(i))

myLenList.sort()
for i in myLenList:
    if start != i :
        for j in range(start,i):
            for k in myinput:
                if j < len(k):  myOutput.append(k[j])
        start = i   

print(myOutput)
#[1, 4, 8, 10, 2, 5, 9, 11, 3, 6, 12, 7, 13]
