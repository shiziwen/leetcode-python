
"""
reference：http://yucoding.blogspot.com/2013/01/leetcode-question-50-median-of-two.html
"""

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        lenA = len(nums1)
        lenB = len(nums2)
        middle = (lenA + lenB) / 2
        
        if (lenA + lenB) % 2 == 1:
            return self.findKth(nums1, nums2, (lenA + lenB) / 2 + 1)
        else:
            return (self.findKth(nums1, nums2, (lenA + lenB) / 2) + self.findKth(nums1, nums2, (lenA + lenB) / 2 + 1)) * 0.5
        
    
    def findKth(self, A, B, K):
        """
        查找A，B数组中，第K大数
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        lenA = len(A)
        lenB = len(B)
        
        if lenA == 0 and lenB == 0:
            return 0
        if lenA > lenB:
            return self.findKth(B, A, K)
        if lenA == 0:
            return B[K - 1]
        if K == 1:
            return min(A[0], B[0])
        pa = min(K/2, lenA)
        pb = K - pa
        
        if A[pa - 1] <= B[pb - 1]:
            return self.findKth(A[pa::], B, K - pa)
        return self.findKth(A, B[pb::], K - pb)
        

