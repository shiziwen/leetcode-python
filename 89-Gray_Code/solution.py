class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]
    
        ret = self.grayCode(n-1)
        for i in xrange(len(ret)-1, -1, -1):
            ret.append(1<<(n-1) | ret[i])
        
        return ret
