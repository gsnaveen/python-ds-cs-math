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


x = 10

# Function call
arr = [ 2, 3, 4, 7, 10, 40 ]
assert binarySearch(arr, 0, len(arr ) -1, x) == 4
arr = [ 2, 3, 4, 7, 10]
assert binarySearch(arr, 0, len(arr ) -1, x) == 4
arr = [ 2, 3, 4, 7, 10, 40,50 ]
assert binarySearch(arr, 0, len(arr ) -1, x) == 4
arr = [ 10, 40 ]
assert binarySearch(arr, 0, len(arr ) -1, x) == 0
