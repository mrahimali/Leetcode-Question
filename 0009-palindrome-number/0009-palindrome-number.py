class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 :
            return False
        new_num = 0
        num = x
        while x > 0 :
            rem = x % 10
            new_num = new_num * 10 + rem
            x = x // 10
        
        return new_num == num
        