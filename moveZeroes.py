class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        numZeros = False
        for i in range(len(nums)):
            
            if nums[i] != 0:
                j = i
                while i > 0 and j > 0:
                    
                    if nums[j -1] == 0:
                        nums[j -1],nums[j] = nums[j],nums[j -1 ]
                        
                    j -= 1

if __name__ == "__main__":
    nums = [0,1,0,3,12]
    Solution().moveZeroes(nums)
    print(nums)
