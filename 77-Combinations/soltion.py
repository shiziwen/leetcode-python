class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k == 1:
            return [[i] for i in range(1, n+1)]
        
        result = []
        if n > k:
            result = [r + [n] for r in self.combine(n-1, k-1)] + self.combine(n-1, k)
        else:
            result = [r + [n] for r in self.combine(n-1, k-1)]
        
        return result
  
        
