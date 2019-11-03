
#Moving even number to the left 

myArr = [21,22,28,23,25,28,99]
length = len(myArr)
print(myArr)    
i = j =  0
while i < length and j < length:
    
    if myArr[j] % 2 == 0:
        myArr[i] , myArr[j] = myArr[j], myArr[i]
        i += 1
    j += 1
    
print(myArr)  


+++++++++++++++++++++++++++++++++++++++++++++

pointer = 0

for index, value in enumerate(val):

    if value % 2 == 0:
        val[pointer], val[index] =  val[index], val[pointer]
        pointer += 1


print(val)
