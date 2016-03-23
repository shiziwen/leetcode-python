class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        m = len(haystack)
        n = len(needle)
        
        for i in range(m + 1 - n):
            match = True
            for j in range(n):
                if haystack[i + j] != needle[j]:
                    match = False
                    break
            if match:
                return i
        return -1
        
