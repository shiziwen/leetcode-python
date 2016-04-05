class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        len_s = len(s)
        if len_s <= 2:
            return '' if s[0] != s[len_s - 1] else s
        
        result = ''
        for i in range(len_s):
            palindrome = self.getPalindrome(s, i, i)
            if len(result) < len(palindrome):
                result = palindrome
            palindrome = self.getPalindrome(s, i, i+1)
            if len(result) < len(palindrome):
                result = palindrome
        return result
        
    def getPalindrome(self, s, start, end):
        """
        循环遍历
        :type s: str
        :type start int
        :type end int
        :rtype: str
        """
        while start >= 0 and end < len(s) and s[start] == s[end]:
            start -= 1
            end += 1
        return s[start+1 : end]

