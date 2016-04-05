class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        num = len(nums)
        res = set()
        dict = {}
        if num < 4:
            return []
        
        nums.sort()
        for i in range(num):
            for j in range(i+1, num):
                if (nums[i] + nums[j]) not in dict:
                    dict[nums[i] + nums[j]] = [(i, j)]
                else:
                    dict[nums[i] + nums[j]].append((i,j))
        
        for m in range(num):
            for n in range(m+1, num-2):
                p = target - nums[m] - nums[n]
                if p in dict:
                    for k in dict[p]:
                        if k[0] > n:
                            res.add((nums[m], nums[n], nums[k[0]], nums[k[1]]))
        
        return [list(i) for i in res]
