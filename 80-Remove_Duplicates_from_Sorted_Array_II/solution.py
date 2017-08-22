class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tmp_nums = []
        count_dup = 0
        tmp_num = None
        for num in nums:
            if num != tmp_num:
                tmp_nums.append(num)
                tmp_num = num
                count_dup = 1
            else:
                if count_dup < 2:
                    tmp_nums.append(num)
                    count_dup += 1
                else:
                    continue
        i = 0
        for num in tmp_nums:
            nums[i] = num
            i += 1
        
        return i
       
