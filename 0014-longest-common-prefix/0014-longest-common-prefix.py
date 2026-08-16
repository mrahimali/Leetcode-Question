class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        n = len(strs)
        fword = strs[0]
        nf = len(fword)

        for i in range(0, nf):
            cw = fword[0:i+1]
            for j in range(0,n):
                if strs[j].startswith(cw):
                    continue
                else:
                    return fword[0:i]

        return fword

