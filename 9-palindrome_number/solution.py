class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if len(str(x)) == 1:
            return True
        if x < 0:
            return False
        a, b = x, 0
        while a:
            b, a = b * 10 + a % 10, a / 10
        return b == x
