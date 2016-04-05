class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.res = []
        tmp = []
        lb = 0
        self.generate_paren_dfs(lb, 0, n, tmp)
        return self.res
        
    def generate_paren_dfs(self, lb, p, n, tmp):
        if p == n*2:
            self.res.append(''.join(tmp))
            return
        if lb < n:
            tmp.append('(')
            self.generate_paren_dfs(lb+1, p+1, n, tmp)
            tmp.pop()
        if p - lb < lb:
            tmp.append(')')
            self.generate_paren_dfs(lb, p+1, n, tmp)
            tmp.pop()
        
        
