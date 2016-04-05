class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows > len(s):
            return s
        tmp = [[] for i in range(numRows)]
        row, step = 0, 1
        for c in s:
            tmp[row] += c
            if row == 0:
                step = 1
            elif row == numRows - 1:
                step = -1
            row += step
        return ''.join(reduce(operator.add, tmp))
