class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mydict = {}
        for i,el in enumerate(nums):
            diff = target - el
            if diff in mydict:
                return [mydict[diff], i]
            mydict[el] = i

        
        