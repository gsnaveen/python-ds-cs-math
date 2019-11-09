class solution:

    def findPeakElement(self,nums) -> int:
        index = float('-inf');value = 0
        la = len(nums)
        for i in range(1,la -1):
            if  (nums[i] > nums[i -1]) and (nums[i] > nums[i + 1]):
                value = max(value,nums[i])
                if value == nums[i]:
                    index = i

        return (index,value)


if __name__ == '__main__':
    a = solution()

    nums = [1,2,3,1]
    print(a.findPeakElement(nums))

    nums = [1, 2, 1, 3, 5, 6, 4]
    print(a.findPeakElement(nums))
