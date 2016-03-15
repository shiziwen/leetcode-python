class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dict = {'(':')', '{':'}', '[':']'}
        tmp = []
        for c in s:
            if dict.get(c, None):
                tmp.append(c)
            elif len(tmp) == 0 or dict[tmp[-1]] != c:
                return False
            else:
                tmp.pop()
        return True if len(tmp) == 0 else False
