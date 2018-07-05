class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = 1
        for i in range(1,len(nums)):
            if nums[i-1] != nums[i]: 
                nums[counter] = nums[i]
                counter += 1
        return nums
    
if __name__ == '__main__':
    nums = [0,0,1,1,1,2,2,3,3,4]
    #nums = [1,1,1]
    print(Solution().removeDuplicates(nums))
