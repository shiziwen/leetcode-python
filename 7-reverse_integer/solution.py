class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        a = 0
        b = x if x > 0 else -x
        while b > 0:
            a = a * 10 + b % 10
            b = b / 10
        if x < 0:
            if x < - (2 ** 31):
                return 0
            else:
                return -a
        else:
            if x > (2 ** 31 - 1):
                return 0
            else:
                return a
