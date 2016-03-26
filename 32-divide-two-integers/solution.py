class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        INT_MAX = 2147483647
        if divisor == 0:
            return INT_MAX
        
        flag = 0
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            flag =1
            if abs(dividend) < abs(divisor):
                return 0
        
        a = abs(dividend)
        b = abs(divisor)
        sum = 0
        count = 0
        res = 0
        
        while a >= b:
            count = 1
            sum = b
            while sum + sum <= a:
                count += count 
                sum += sum
            a -= sum
            res += count
        
        if flag:
            res = 0 - res
        
        if res > INT_MAX:
            res = INT_MAX
            
        return res
            
