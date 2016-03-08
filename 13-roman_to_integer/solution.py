class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roval = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        ans = 0
        for i in range(len(s)):
            if i + 1 < len(s) and roval[s[i]] < roval[s[i+1]]:
                ans -= roval[s[i]]
            else:
                ans += roval[s[i]]
        return ans
