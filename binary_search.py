def binarySearch(arr,l,r,x):

    if l <= r:

        mid = l + (r -l)//2
        midval = arr[mid]

        if midval == x:
            return mid
        elif x < midval:
            return binarySearch(arr,l,mid -1,x)
        elif x > midval:
            return binarySearch(arr,mid + 1, r,x)
    else:
        return -1

# Searching the rotated sorted list
def binarySearchR(arr,l,r,x):

    pivot = findPivot(arr)

    if arr[pivot + 1] <= x and arr[r] >= x:
        l = pivot + 1
        returnVal = binarySearch(arr, l, r, x)
        return returnVal
    elif arr[l] <= x and arr[pivot] >= x:
        r = pivot
        return binarySearch(arr, l, r, x)

# Finding a Pivot
def findPivot(arr):
    for i in range(1,len(arr)):
        if arr[i -1 ] > arr[i]:
            return i -1

# Function call
arr = [4,5,6,7,0,1,2]; x= target =0
print(binarySearchR(arr, 0, len(arr ) -1, x))



# Function call
x=10
arr = [ 2, 3, 4, 7, 10, 40 ]
assert binarySearch(arr, 0, len(arr ) -1, x) == 4
arr = [ 2, 3, 4, 7, 10]
assert binarySearch(arr, 0, len(arr ) -1, x) == 4
arr = [ 2, 3, 4, 7, 10, 40,50 ]
assert binarySearch(arr, 0, len(arr ) -1, x) == 4
arr = [ 10, 40 ]
assert binarySearch(arr, 0, len(arr ) -1, x) == 0
