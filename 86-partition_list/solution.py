# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        small = ListNode(-1)
        big = ListNode(-1)
        
        small_head = small
        big_head = big
        
        p = head
        
        while p:
            if p.val < x:
                small.next = p
                small = small.next
            else:
                big.next = p
                big = big.next
            p = p.next
        
        if small_head.next:
            if big_head.next:
                small.next = big_head.next
                big.next = None
            else:
                small.next = None
            head = small_head.next
        elif big_head.next:
            big.next = None
            head = big_head.next
        
        return head
            
                
