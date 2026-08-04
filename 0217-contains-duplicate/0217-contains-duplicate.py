class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mydict = {}
        for el in nums:
            mydict[el] = mydict.get(el, 0)+1

        for el in mydict:
            if mydict[el]>=2:
                return True
        return False
        