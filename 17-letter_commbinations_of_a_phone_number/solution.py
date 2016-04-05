class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # print digits
        if len(digits) == 0:
            return []
        self.dlist = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        self.res = []
        tmp = []
        self.combination(digits, 0, tmp)
        return self.res
        
    def combination(self, digits, index, tmp):
        if index == len(digits):
            self.res.append("".join(tmp))
            # print 'res is %s' % self.res
            return
        for c in self.dlist[ord(digits[index]) - ord('0')]:
            tmp.append(c)
            # print '1-tmp is %s' % tmp
            self.combination(digits, index + 1, tmp)
            tmp.pop()
            # print '2-tmp is %s' % tmp

if __name__ == '__main__':
    s = Solution()
    print s.letterCombinations("23")

