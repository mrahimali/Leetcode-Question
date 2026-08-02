class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = 0
        n = len(nums)
        i = 0
        while i<n:
            if nums[k]==0 and nums[i]!=0:
                nums[k], nums[i] = nums[i], nums[k]
                k+=1
            if nums[k]!=0:
                k+=1
            i+=1
        
        return nums
        