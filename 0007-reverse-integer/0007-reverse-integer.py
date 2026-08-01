class Solution:
    def reverse(self, x: int) -> int:
        n = x
        if n<0:
            n = -1*n
        new_num = 0
        while n>0:
            rem = n%10
            new_num = new_num * 10 + rem
            n = n//10
        
        if new_num >((2**31)-1) or new_num <= -2**31:
            return 0
        if x < 0:
            return -1*new_num
        return new_num
        