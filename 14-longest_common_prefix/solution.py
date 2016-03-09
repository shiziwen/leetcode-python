class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) <= 1:
            return strs[0] if len(strs) == 1 else ""
        
        index = 0
        minl = min([len(s) for s in strs])
        
        while index < minl:
            for i in range(1, len(strs)):
                if strs[i][index] != strs[i-1][index]:
                    return strs[0][:index]
            index = index + 1
        return strs[0][:index]
