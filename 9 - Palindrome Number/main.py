class Solution:
    def isPalindrome(self, x: int) -> bool:
        # begin = 0
        # last = len(str(x))
        # input_ = str(x)
        
        # if x < 0 or (x % 10 == 0 and x != 0):
            # return false
        x = str(x)
        return x == x[::-1]
