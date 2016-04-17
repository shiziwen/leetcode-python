class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        this_sum = 0
        max_sum = -10000
        
        for i in range( 0, len(nums) ):
            if this_sum < 0:
                this_sum = 0
            this_sum = this_sum + nums[ i ]
            max_sum = max( this_sum, max_sum )

        return max_sum
