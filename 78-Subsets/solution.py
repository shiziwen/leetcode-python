class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(depth, start, vlist):
            res.append(vlist)
            if depth == len(nums):
                return
            for i in range(start, len(nums)):
                dfs(depth+1, i+1, vlist+[nums[i]])
        
        res = []
        dfs(0, 0, [])
        
        return res
