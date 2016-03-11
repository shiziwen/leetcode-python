class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res = None
        for i in range(0, len(nums)):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if res is None or abs(sum - target) < abs(res - target):
                    res = sum
                if sum <= target:
                    l += 1
                else:
                    r -= 1
        return res

