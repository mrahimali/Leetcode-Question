class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        s = (n*(n+1))//2
        sm = 0
        for el in nums:
            sm = sm + el
        mis = s - sm
        return mis