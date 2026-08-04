class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mydict = {}
        n = len(nums)
        for el in nums:
            mydict[el] = mydict.get(el, 0)+1
        
        for el in mydict:
            if mydict[el]>(n//2):
                return el
        