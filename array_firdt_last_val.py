
def fl(arr,target):

    la = len(arr)
    start = end = None
    for i in range(la):
        if arr[i] == target:
            start = i
            break

    for i in range(la -1,-1,-1):
        if arr[i] == target:
            end = i
            break

    if start and end:
        return [start,end]
    else:
        return [-1,-1]

nums = [5,7,7,8,8,10]
target = 8

print(fl(nums,target))
