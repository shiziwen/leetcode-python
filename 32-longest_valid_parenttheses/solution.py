class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack, maxLen = [-1], 0
        for i in xrange(len(s)):
            if s[i] == ')' and stack[-1] != -1 and s[stack[-1]] == '(':
                stack.pop()
                maxLen = max(maxLen, i - stack[-1])
            else:
                stack.append(i)
        return maxLen
