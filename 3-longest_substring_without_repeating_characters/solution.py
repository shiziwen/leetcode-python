class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        res = 0
        cur = 0
        d = {}
        for i, v in enumerate(s):
            if v not in d:
                cur += 1
            else:
                cur = min(i - d[v], cur + 1)
            d[v] = i
            res = max(res, cur)
        return res
