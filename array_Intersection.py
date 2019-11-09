
def arrIntersection(nums1,nums2):
    nums1 = set(nums1)
    nums2 = set(nums2)
    myO = set()
    if len(nums1) < len(nums2):
        short = nums1
        long = nums2
    else:
        short = nums2
        long = nums1

    for i in short:
        if i in long:
            myO.add(i)

    return list(myO)

nums1 = [1,2,2,1]; nums2 = [2,2]
print(arrIntersection(nums1,nums2))

nums1 = [4,9,5]; nums2 = [9,4,9,8,4]
print(arrIntersection(nums1,nums2))
